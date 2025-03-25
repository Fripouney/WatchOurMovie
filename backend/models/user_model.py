from sqlalchemy import *
from sqlalchemy.orm import relationship
from backend.db import Base

class UserModel(Base):
    id = Column(INTEGER, primary_key=True, index=True)
    username = Column(VARCHAR)
    password = Column(VARCHAR)
    favorite_genres = relationship("user_favorite_genre")
    viewed_movies = relationship("user_movie")