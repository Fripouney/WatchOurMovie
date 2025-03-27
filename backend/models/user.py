from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import relationship
from backend.db import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, index=True)
    username = Column(VARCHAR(40), nullable=False)
    password = Column(VARCHAR(100), nullable=False)

    favorite_genres = relationship("UserFavoriteGenreModel", backref="user", cascade="all, delete-orphan")
    viewed_movies = relationship("UserMovieModel", backref="user", cascade="all, delete-orphan")
