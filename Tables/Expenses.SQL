DROP TABLE IF EXISTS

CREATE TABLE IF NOT EXISTS Expenses (
    Expense_name TEXT,
    Amount INT,
    Type TEXT,
    Day_of_purchase TEXT,
    Additional_note TEXT
);

LOAD DATA