import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models.user_movies import UserMoviesModel
from schemas.watch import WatchRequest

watchRoutes = APIRouter()

@watchRoutes.post("/watch/suggestions")
def get_watch_suggestions(data: WatchRequest, db: Session = Depends(get_db)):
    # Récupère tous les films vus par les utilisateurs sélectionnés
    seen = db.query(UserMoviesModel.movie_id).filter(
        UserMoviesModel.user_id.in_(data.users)
    ).distinct().all()

    seen_ids = set(mid for (mid,) in seen)
    available = [mid for mid in data.movies if mid not in seen_ids]

    # Tire au hasard 5 suggestions
    suggestions = random.sample(available, min(6, len(available)))

    return suggestions