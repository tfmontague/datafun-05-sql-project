"""P5: Project Summary - This Python script demonstrates the ability to interact with a SQL database, including creating a database, 
defining a schema, and executing various SQL commands. Incorporate logging to document the process and provide user feedback. Step-by-steps instructions
for environment setup and installation can be accessed at this repository's README: https://github.com/tfmontague/datafun-05-sql-project/blob/main/README.md

Script Name: VCR Store Manager

Description: This script manages a database for a VCR rental store. It includes functionalities
for managing VCRs, customers, and rental transactions. Logging is utilized for
monitoring and debugging.
"""

# Import Dependencies

import sqlite3
import logging
import pandas as pd
import pathlib
from pathlib import Path


# Logging Configuration - Configure logging to write to a file, appending new logs to the existing file

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")


# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def main():
    create_database()

if __name__ == "__main__":
    main()


# Database Schema Design
'''
vcrs: id INTEGER PRIMARY KEY, model TEXT, availability BOOLEAN
customers: id INTEGER PRIMARY KEY, name TEXT, contact_info TEXT
rentals: id INTEGER PRIMARY KEY, customer_id INTEGER, vcr_id INTEGER, rental_date DATE, return_date DATE, with foreign keys to customers and vcrs
'''

