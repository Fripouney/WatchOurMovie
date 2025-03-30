from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from db import Base

class UserGenresModel(Base):
    __tablename__ = "user_favorite_genre"

    id = Column(INTEGER, primary_key=True, index=True)
    user_id = Column(INTEGER, ForeignKey("users.id"))
    genre = Column(VARCHAR(50))
