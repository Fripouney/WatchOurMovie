from sqlalchemy.orm import relationship
from models.user import UserModel
from models.user_genres import UserGenresModel
from models.user_movies import UserMoviesModel
from models.friendship import FriendshipModel

UserModel.favorite_genres = relationship(
    UserGenresModel, back_populates="user", cascade="all, delete-orphan"
)
UserModel.viewed_movies = relationship(
    UserMoviesModel, back_populates="user", cascade="all, delete-orphan"
)
UserModel.sent_friend_requests = relationship(
    FriendshipModel,
    back_populates="requester",
    foreign_keys=[FriendshipModel.user_id],
)
UserModel.received_friend_requests = relationship(
    FriendshipModel,
    back_populates="recipient",
    foreign_keys=[FriendshipModel.friend_id],
)

FriendshipModel.requester = relationship(
    UserModel,
    back_populates="sent_friend_requests",
    foreign_keys=[FriendshipModel.user_id],
)
FriendshipModel.recipient = relationship(
    UserModel,
    back_populates="received_friend_requests",
    foreign_keys=[FriendshipModel.friend_id],
)

UserGenresModel.user = relationship(
    UserModel, back_populates="favorite_genres"
)

UserMoviesModel.user = relationship(
    UserModel, back_populates="viewed_movies"
)