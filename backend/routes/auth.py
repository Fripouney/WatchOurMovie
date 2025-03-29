from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from db import get_db
from schemas.auth import UserLogin, UserRegister, TokenResponse
from models.user import UserModel
from utils.jwt_handler import create_access_token, verify_token
import bcrypt

authRoutes = APIRouter()

# REGISTER
@authRoutes.post("/register", response_model=TokenResponse)
def register(user: UserRegister, db: Session = Depends(get_db)):
    if db.query(UserModel).filter_by(username=user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    new_user = UserModel(username=user.username, password=hashed_pw.decode())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token({"user_id": new_user.id})
    return {"access_token": token}

# LOGIN
@authRoutes.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter_by(username=user.username).first()
    if not db_user or not bcrypt.checkpw(user.password.encode(), db_user.password.encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": db_user.id})
    return {"access_token": token}

# CHANGE PASSWORD
@authRoutes.put("/change-password")
def change_password(new_password: str, authorization: str = Header(...), db: Session = Depends(get_db)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid token format")
    token = authorization.split(" ")[1]
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    user = db.query(UserModel).filter_by(id=payload["user_id"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_pw = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
    user.password = hashed_pw.decode()
    db.commit()
    return {"message": "Password updated"}

# LOGOUT (optionnel, côté client)
@authRoutes.post("/logout")
def logout():
    # JWT est stateless : le logout se gère côté frontend en supprimant le token
    return {"message": "Logout successful"}
