--syntax: sql
-- doesnt need to uppercase keywords(CREATE can be create)
-- but it is a good practice to do so
-- use IF NOT EXISTS to avoid errors if the table already exists

CREATE TABLE IF NOT EXISTS student(
    id BIGSERIAL PRIMARY KEY,
    name TEXT,
    email TEXT 
);
CREATE TABLE IF NOT EXISTS parent(
    id BIGSERIAL PRIMARY KEY,
    name TEXT,
    email TEXT 
)