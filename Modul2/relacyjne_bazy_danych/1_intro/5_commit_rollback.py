'''
Przykład zastosowania commit i rollback

-- Begin transaction
BEGIN TRANSACTION;

-- Create table query
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);

-- Commit transaction to apply changes
COMMIT;

-- Begin another transaction
BEGIN TRANSACTION;

-- Drop table query
DROP TABLE IF EXISTS my_table;

-- Rollback transaction to revert changes
ROLLBACK;
'''