import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import get_db
from models.user import UserModel
from models.user_movies import UserMoviesModel
from utils.deps import get_current_user
from schemas.user import PasswordChange, UserCreate, UserGet, UserMovieCreate, UserUpdate
from utils.deps import get_current_user

userRoutes = APIRouter()

class MovieWatchedRequest(BaseModel):
    movie_id: int

# GET : récupère un user avec son id
@userRoutes.get("/user/{id}", response_model=UserGet)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Vérifie si un user a vu un film
@userRoutes.get("/user/watched/{movie_id}")
def check_if_user_viewed_movie(movie_id: int, user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    user_movie = db.query(UserMoviesModel).filter(UserMoviesModel.user_id == user.id and UserMoviesModel.movie_id == movie_id).first()
    return {"viewed": user_movie is not None}


# Ajoute un film vu par un utilisateur
@userRoutes.post("/user/watched")
def add_watched_movie(body: MovieWatchedRequest, user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    user_movie =  UserMoviesModel(user_id = user.id, movie_id = body.movie_id)
    db.add(user_movie)
    db.commit()
    db.refresh(user_movie)
    return {"message": "Movie marked as seen by user", "user_movie": user_movie}

# Supprime un film vu par un utilisateur
@userRoutes.delete("/user/watched/{movie_id}")
def deleteWatchedMovie(movie_id: int, user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    user_movie = db.query(UserMoviesModel).filter(UserMoviesModel.user_id == user.id and UserMoviesModel.movie_id == movie_id).first()
    if not user_movie:
        raise HTTPException(status_code=404, detail="This movie is not marked as viewed by the user")
    db.delete(user_movie)
    db.commit()
    return {"message": "The movie has been unmarked as viewed"}

# Retourne la liste des users par username
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
