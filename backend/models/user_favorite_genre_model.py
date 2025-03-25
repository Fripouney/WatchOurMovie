from sqlalchemy import *
from sqlalchemy.orm import relationship
from backend.db import Base

class UserFavoriteGenreModel(Base):
    id = Column(INTEGER, primary_key=True, index=True)
    user_id = Column(INTEGER, ForeignKey("user.id"))
    genre = Column(VARCHAR)
    user = relationship("user")