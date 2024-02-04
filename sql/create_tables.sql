-- SQL file to create database schema

-- Create the 'vcrs' table
CREATE TABLE IF NOT EXISTS vcrs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    availability BOOLEAN NOT NULL
);

-- Create the 'customers' table
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_info TEXT NOT NULL
);

-- Create the 'rentals' table
CREATE TABLE IF NOT EXISTS rentals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    vcr_id INTEGER,
    rental_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (vcr_id) REFERENCES vcrs(id)
);
