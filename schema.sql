DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id integer PRIMARY KEY autoincrement,
    name text NOT NULL,
    image_url text NOT NULL,
    age integer NOT NULL,
    state text NOT NULL,
    gender text NOT NULL,
    language text NOT NULL,
    description text NOT NULL
);

DROP TABLE IF EXISTS interests;
CREATE TABLE interests (
    id integer PRIMARY KEY autoincrement,
    name text NOT NULL,
    image_url text NOT NULL,
    description text NOT NULL
);

DROP TABLE IF EXISTS user_interests;
CREATE TABLE user_interests (
    id integer PRIMARY KEY autoincrement,
    user_id integer NOT NULL,
    interest_id integer NOT NULL
);
