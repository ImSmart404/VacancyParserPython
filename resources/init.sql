CREATE TABLE user_auth (
    id SERIAL PRIMARY KEY,
    username VARCHAR(250) NOT NULL,
    password VARCHAR(250) NOT NULL,
    UNIQUE (username)
);