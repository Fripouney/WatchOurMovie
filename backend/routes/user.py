from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.user import UserModel
from schemas.user import UserCreate, UserGet

userRoutes = APIRouter()

# Requête GET : récupère un user
@userRoutes.get("/user/{id}", response_model=UserGet)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Requête POST : crée un user
@userRoutes.post("/user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = UserModel(user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user": new_user}

# Requête DELETE : supprime un utilisateur
@userRoutes.delete("/user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
