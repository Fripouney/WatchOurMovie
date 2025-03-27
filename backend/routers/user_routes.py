from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.user_model import UserModel
from backend.schemas.user_schema import UserCreate, UserGet
from backend.models.user_favorite_genre_model import UserFavoriteGenreModel
from backend.schemas.user_schema import UserFavoriteGenreCreate

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


# Requête PUT : change le mot de passe d'un user
# Voir pour faire une fonction de hash
@userRoutes.put("/user/{id}")
def change_password(id: int, new_password: str, db: Session = Depends(get_db)):
    pass

# Requête DELETE : supprime un utilisateur
@userRoutes.delete("/user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


# Requête GET : récupère les genres favoris d'un utilisateur
@userRoutes.get("/user/{id}/favorite-genre")
def get_favorite_genres(id: int, db: Session = Depends(get_db)):
    genres = db.query(UserFavoriteGenreModel).filter_by(user_id=id).all()
    if not genres:
        return {"message": "No favorite genres found", "genres": []}
    return {"message": "Favorite genres retrieved", "genres": [g.genre for g in genres]}


# Requête DELETE : le un genre favori d'un utilisateur
@userRoutes.delete("/user/{id}/favorite-genre")
def remove_favorite_genre(id: int, genre: str, db: Session = Depends(get_db)):
    deleted = db.query(UserFavoriteGenreModel).filter_by(user_id=id, genre=genre).delete()
    db.commit()
    if deleted:
        return {"message": "Genre removed"}
    return {"message": "Genre not found"}


# Requête POST : ajoute un genre favori à un utilisateur
@userRoutes.post("/user/{id}/favorite-genre")
def add_favorite_genre(id: int, genre_data: UserFavoriteGenreCreate, db: Session = Depends(get_db)):
    existing = db.query(UserFavoriteGenreModel).filter_by(user_id=id, genre=genre_data.genre).first()
    if existing:
        return {"message": "Genre already in favorites"}

    new_genre = UserFavoriteGenreModel(user_id=id, genre=genre_data.genre)
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return {"message": "Genre added", "genre": new_genre.genre}
