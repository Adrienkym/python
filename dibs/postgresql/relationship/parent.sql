
-- CREATE TABLE IF NOT EXISTS parent(
--     id BIGSERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(250) UNIQUE NOT NULL
    
-- );

CREATE TABLE IF NOT EXISTS parent_address(
    id BIGSERIAL PRIMARY KEY,
    parent_id BIGSERIAL REFERENCES parent(id),
    county_name VARCHAR(250),
    town VARCHAR(250),
    longitude REAL,
    latitude REAL,
    house_no VARCHAR(200)
);

--INSERT INTO parent (name, email)
--VALUES
--('John Doe', 'john@john.com'),
--('Jane Smith', 'jane@jane.com'),


--INSERT INTO parent_address (county_name, town,
  --  longitude, latitude, house_no)
--VALUES
--('County A', 'Town A' , 12.3456, 65.4321, '123 Main St'),
--('County B', 'Town B', 23.4567, 76.5432, '456 Elm St');