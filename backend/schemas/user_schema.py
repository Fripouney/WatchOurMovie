from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str

class UserGet(BaseModel):
    id: int
    name: str
    password: str