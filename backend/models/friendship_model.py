from sqlalchemy import Column, INTEGER, BOOLEAN, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class FriendshipModel(Base):
    __tablename__ = "friends"

    id = Column(INTEGER, primary_key=True, index=True)
    user_id = Column(INTEGER, ForeignKey("users.id"))
    friend_id = Column(INTEGER, ForeignKey("users.id"))
    accepted = Column(BOOLEAN, default=False)

    requester = relationship("UserModel", foreign_keys=[user_id], backref="sent_friend_requests")
    recipient = relationship("UserModel", foreign_keys=[friend_id], backref="received_friend_requests")
