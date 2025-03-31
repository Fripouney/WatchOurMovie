from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from db import get_db
from utils.jwt_handler import verify_token
from models.user import UserModel

def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1]
    payload = verify_token(token)
    user_id = payload["user_id"]
    user = db.query(UserModel).filter_by(id=user_id).first()
    return user
