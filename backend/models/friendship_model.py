from sqlalchemy import *
from sqlalchemy.orm import relationship
from backend.db import Base

class FriendshipModel(Base):
    id = Column(INTEGER, primary_key=True, index=True)
    user_id = Column(INTEGER, ForeignKey("user.id"))
    friend_id = Column(INTEGER, ForeignKey("user.id"))
    accepted = Column(BOOLEAN, default=False)
    first_user = relationship("user")
    second_user = relationship("user")
