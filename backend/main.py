from sqlalchemy.orm import Session
from db import get_db
from models.user import UserModel
from fastapi import FastAPI
import uvicorn, time, bcrypt
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import authRoutes
from routes.user import userRoutes
from routes.genres import genresRoutes
from routes.friends import friendsRoutes

app = FastAPI()

@app.on_event("startup")
def create_default_users():
    db: Session = next(get_db())

    # Crée l'admin s'il n'existe pas
    admin_exist = db.query(UserModel).filter_by(admin=True).first()
    if not admin_exist:
        hashed_pw = bcrypt.hashpw("123".encode(), bcrypt.gensalt()).decode()
        new_admin = UserModel(username="admin", password=hashed_pw, admin=True)
        db.add(new_admin)
        print("admin created")

    # Crée les utilisateurs user1, user2, user3 s'ils n'existent pas
    for username in ["user1", "user2", "user3"]:
        user_exist = db.query(UserModel).filter_by(username=username).first()
        if not user_exist:
            hashed_pw = bcrypt.hashpw("123".encode(), bcrypt.gensalt()).decode()
            user = UserModel(username=username, password=hashed_pw, admin=False)
            db.add(user)
            print(f"'{username}' created")

    db.commit()

app.include_router(authRoutes)
app.include_router(userRoutes)
app.include_router(genresRoutes)
app.include_router(friendsRoutes)

# Autorise toutes les origines
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app) # localhost:8000


time.sleep(3)

# # création des tables
# Base.metadata.create_all(bind=engine)
