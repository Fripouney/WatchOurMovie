from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models.user_genres import UserGenresModel
from schemas.user import UserGenresCreate

genresRoutes = APIRouter()

# Requête GET : récupère les genres favoris d'un utilisateur
@genresRoutes.get("/user/{id}/genres")
def get_favorite_genres(id: int, db: Session = Depends(get_db)):
    genres = db.query(UserGenresModel).filter_by(user_id=id).all()
    if not genres:
        return {"message": "No favorite genres found", "genres": []}
    return {"message": "Favorite genres retrieved", "genres": [g.genre for g in genres]}

# Requête POST : ajoute un genre favori à un utilisateur
@genresRoutes.post("/user/{id}/genres")
def add_favorite_genre(id: int, genre_data: UserGenresCreate, db: Session = Depends(get_db)):
    existing = db.query(UserGenresModel).filter_by(user_id=id, genre=genre_data.genre).first()
    if existing:
        return {"message": "Genre already in favorites"}

    new_genre = UserGenresModel(user_id=id, genre=genre_data.genre)
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return {"message": "Genre added", "genre": new_genre.genre}

# Requête DELETE : le un genre favori d'un utilisateur
@genresRoutes.delete("/user/{id}/genres")
def remove_favorite_genre(id: int, genre: str, db: Session = Depends(get_db)):
    deleted = db.query(UserGenresModel).filter_by(user_id=id, genre=genre).delete()
    db.commit()
    if deleted:
        return {"message": "Genre removed"}
    return {"message": "Genre not found"}