CREATE TABLE IF NOT EXISTS user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(40),
    password VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS user_favorite_genre (
    user_id SERIAL PRIMARY KEY,
    genre VARCHAR,
    FOREIGN KEY user_id REFERENCES user(id),
);

CREATE TABLE IF NOT EXISTS friends (
    id SERIAL PRIMARY KEY,
    friend_id SERIAL,
    FOREIGN KEY friend_id REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS user_movie (
    id SERIAL PRIMARY KEY,
    user_id SERIAL,
    movie_id INTEGER,
    FOREIGN KEY user_id REFERENCES user(id)
);