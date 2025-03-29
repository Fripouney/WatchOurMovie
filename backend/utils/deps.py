from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from db import get_db
from jwt_handler import verify_token
from models.user import UserModel

def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid token format")
    token = authorization.split(" ")[1]

    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    user = db.query(UserModel).filter_by(id=payload["user_id"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
