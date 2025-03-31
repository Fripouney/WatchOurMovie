from pydantic import BaseModel

class UserCreate(BaseModel):
    admin: str
    username: str
    password: str

class UserGet(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True

class UserGenresCreate(BaseModel):
    genre: str

class UserUpdate(BaseModel):
    username: str

class PasswordChange(BaseModel):
    old_password: str
    new_password: str
