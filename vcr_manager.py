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


# Database Schema Design
'''
Outlined in this repository's README
'''


# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

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

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        customers_data_path = pathlib.Path("data", "customers.csv")
        rentals_data_path = pathlib.Path("data", "rentals.csv")
        vcrs_data_path = pathlib.Path("data", "vcrs.csv")
        customers_df = pd.read_csv(customers_data_path)
        rentals_df = pd.read_csv(rentals_data_path)
        vcrs_df = pd.read_csv(vcrs_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            customers_df.to_sql("customers", conn, if_exists="replace", index=False)
            rentals_df.to_sql("rentals", conn, if_exists="replace", index=False)
            vcrs_df.to_sql("vcrs", conn,if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def execute_sql_from_file(db_filepath, sql_file):
    """Function to use Python to interact with the SQL database and execute SQL commands."""
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")


def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    db_filepath = 'project.db'

    # Specify the correct path for SQL files
    base_path = pathlib.Path()  # Gets the current directory path

    # Adjust these paths to point to your actual SQL file locations
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'create_tables.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'insert_records.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'update_records.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'delete_records.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_filter.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_sorting.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_group_by.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_join.sql')

    logging.info("All SQL operations completed successfully")


if __name__ == "__main__":
    main()





