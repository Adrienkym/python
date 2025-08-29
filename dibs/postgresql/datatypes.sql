
CREATE TABLE IF NOT EXISTS student(
    id SERIAL,
    name TEXT,
    email TEXT,
    dob Date, -- PostgreSQL supports the DATE type
    phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);
CREATE TABLE IF NOT EXISTS parent(
    id SERIAL,
    name TEXT,
    email TEXT,
    dob Date, -- PostgreSQL supports the DATE type
    phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);

-- Insert sample data into student table
INSERT INTO student (name, email, dob, phone, created_at, updated_at)
VALUES
('Alice', 'alice@example.com', '2002-02-02', '1111111111', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Bob', 'bob@example.com', '2001-03-03', '2222222222', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Charlie', 'charlie@example.com', '2003-04-04', '3333333333', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
