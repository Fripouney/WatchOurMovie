from sqlalchemy import Column, INTEGER, BOOLEAN, ForeignKey
from db import Base

class FriendshipModel(Base):
    __tablename__ = "friends"

    id = Column(INTEGER, primary_key=True, index=True)
    user_id = Column(INTEGER, ForeignKey("users.id"))
    friend_id = Column(INTEGER, ForeignKey("users.id"))
    accepted = Column(BOOLEAN, default=False)
