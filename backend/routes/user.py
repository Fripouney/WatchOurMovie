import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.user import UserModel
from schemas.user import PasswordChange, UserCreate, UserGet, UserUpdate
from utils.deps import get_current_user

userRoutes = APIRouter()

# GET : récupère un user avec son id
@userRoutes.get("/user/{id}", response_model=UserGet)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# GET : récupère un user avec son nom
@userRoutes.get("/user/by-username/{username}", response_model=UserGet)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# GET : récupère les infos utilisateur
@userRoutes.get("/me", response_model=UserGet)
def get_current_user_data(current_user: UserModel = Depends(get_current_user)):
    return current_user

# PUT : mets à jour les infos utilisateur
@userRoutes.put("/me", response_model=UserGet)
def update_user_info(data: UserUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    current_user.username = data.username
    db.commit()
    db.refresh(current_user)
    return current_user


# PUT : mets à jour le password utilisateur
@userRoutes.put("/me/password")
def update_password(data: PasswordChange, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    if not bcrypt.checkpw(data.old_password.encode(), current_user.password.encode()):
        raise HTTPException(status_code=400, detail="Mot de passe incorrect")

    current_user.password = bcrypt.hashpw(data.new_password.encode(), bcrypt.gensalt()).decode()
    db.commit()
    return {"message": "Mot de passe mis à jour"}


# POST : crée un user
@userRoutes.post("/user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = UserModel(user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user": new_user}

# DELETE : supprime un utilisateur
@userRoutes.delete("/user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
