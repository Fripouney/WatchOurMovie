from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models.friendship import FriendshipModel
from models.user import UserModel

friendsRoutes = APIRouter()

# Requête GET : récupère les amis d'un utilisateur
@friendsRoutes.get("/user/{id}/friends")
def get_friends(id: int, db: Session = Depends(get_db)):
    sent = db.query(FriendshipModel).filter_by(user_id=id, accepted=True).all()
    received = db.query(FriendshipModel).filter_by(friend_id=id, accepted=True).all()

    friend_ids = [f.friend_id for f in sent] + [f.user_id for f in received]
    friends = db.query(UserModel).filter(UserModel.id.in_(friend_ids)).all()

    return {
        "message": "Friends list retrieved",
        "friends": [{"id": u.id, "username": u.username} for u in friends]
    }

# Requête GET : récupère les demandes d'amis reçues (non acceptées)
@friendsRoutes.get("/user/{id}/friend-requests")
def get_friend_requests(id: int, db: Session = Depends(get_db)):
    pending = db.query(FriendshipModel).filter_by(friend_id=id, accepted=False).all()
    senders = db.query(UserModel).filter(UserModel.id.in_([r.user_id for r in pending])).all()

    return {
        "message": "Pending friend requests retrieved",
        "requests": [{"id": u.id, "username": u.username} for u in senders]
    }

# Requête POST : envoie une demande d'ami
@friendsRoutes.post("/user/{id}/friend")
def send_friend_request(id: int, friend_id: int, db: Session = Depends(get_db)):
    if id == friend_id:
        return {"message": "You can't add yourself as a friend"}

    existing = db.query(FriendshipModel).filter_by(user_id=id, friend_id=friend_id).first()
    if existing:
        return {"message": "Friend request already sent or already friends"}

    new_request = FriendshipModel(user_id=id, friend_id=friend_id, accepted=False)
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return {"message": "Friend request sent"}

# Requête PUT : accepte une demande d'ami
@friendsRoutes.put("/user/{id}/friend/{friend_id}/accept")
def accept_friend_request(id: int, friend_id: int, db: Session = Depends(get_db)):
    request = db.query(FriendshipModel).filter_by(user_id=friend_id, friend_id=id, accepted=False).first()
    if not request:
        return {"message": "No pending friend request found"}
    
    request.accepted = True
    db.commit()
    return {"message": "Friend request accepted"}

# Requête DELETE : supprime un ami ou une demande
@friendsRoutes.delete("/user/{id}/friend/{friend_id}")
def remove_friend(id: int, friend_id: int, db: Session = Depends(get_db)):
    deleted = db.query(FriendshipModel).filter(
        ((FriendshipModel.user_id == id) & (FriendshipModel.friend_id == friend_id)) |
        ((FriendshipModel.user_id == friend_id) & (FriendshipModel.friend_id == id))
    ).delete()
    db.commit()
    if deleted:
        return {"message": "Friendship deleted"}
    return {"message": "No friendship found"}
