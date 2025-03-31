from pydantic import BaseModel
from typing import List

class WatchRequest(BaseModel):
    users: List[int]
    movies: List[int]
