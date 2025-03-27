from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base
from backend.models.user import UserModel

class UserFavoriteGenreModel(Base):
    __tablename__ = "user_favorite_genre"

    id = Column(INTEGER, primary_key=True, index=True)
    user_id = Column(INTEGER, ForeignKey("users.id"))
    genre = Column(VARCHAR(50))
    user = relationship("UserModel", backref="favorite_genres")
