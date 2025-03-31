from sqlalchemy import Column, INTEGER, ForeignKey
from db import Base

class UserMoviesModel(Base):
    __tablename__ = "user_movie"

    id = Column(INTEGER, primary_key=True, index=True)
    user_id = Column(INTEGER, ForeignKey("users.id"))
    movie_id = Column(INTEGER)
