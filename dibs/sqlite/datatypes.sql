
CREATE TABLE studentsql (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob Text, -- sqlite does not have a date type, so we use TEXT
    phone TEXT,
    created_at Text,
    updated_at Text
);
-- insert sample data into student table
INSERT INTO studentsql (name, email, dob, phone, created_at, updated_at)
VALUES
('Alice', 'alice@alice', '2002-02-02', '1111111111', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Bob', 'bob@bob', '2001-03-03', '2222222222', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Charlie', 'charlie@charlie', '2003-04-04', '3333333333', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
