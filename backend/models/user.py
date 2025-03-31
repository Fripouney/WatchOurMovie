from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN
from db import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, index=True)
    admin = Column(BOOLEAN, default=False)
    username = Column(VARCHAR(40), nullable=False)
    password = Column(VARCHAR(100), nullable=False)
