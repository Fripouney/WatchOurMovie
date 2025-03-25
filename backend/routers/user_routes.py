from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.user_model import UserModel
from backend.schemas.user_schema import UserCreate, UserGet

userRoutes = APIRouter()

# Requête GET : recup un user
@userRoutes.get("/users/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(UserModel).filter(UserModel.id == id).first()

# Requête POST : crée un user
@userRoutes.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = UserModel(user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Requête PUT : change le mot de passe d'un user
# Voir pour faire une fonction de hash
@userRoutes.put("/users/{id}")
def change_password(id: int, new_password: str, db: Session = Depends(get_db)):
    pass

# Requête DELETE : supprime un utilisateur
@userRoutes.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    db.query(UserModel).filter(UserModel.id == id).delete()
    db.commit()