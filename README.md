# datafun-05-sql-project - P5: Python and SQL Project

## Overview

This repository integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations

## Project Stucture & Deliverables

- `datafun-05-sql-project`: Project repository
- `README.md`: Provides an overview of the project, as well as instructions for setting up and executing the environment.
- `requirements.txt`: Lists all packages required for the project.
- `vcr_manager.py`: Python file
- SQL files: SQL statements and queries to perform various SQL commands
- Query results: csv files capturing results of all SQL queries


## Environment Setup & How to Install the Project

1. Create a GitHub project repository with a default `README.md.`

2. Clone your repo down to your machine. 

3. Open your project folder in VS Code (if you haven't already).

4. Add a .gitignore with `.vsode/` and `.venv/` and whatever else doesn't need to go in the repo.

5. Create and activate a local virtual environment in `.venv.`
    - `python -m venv .venv`
    - `.\.venv\Scripts\activate`

6. Install your dependencies into your `.venv` (pandas and pyarrow) and freeze into your requirements.txt.
    - `pip install pandas pyarrow`
    - `pip freeze > requirements.txt`

7. Record the commands used in your `README.md.`

8. Git add and commit with a useful message (e.g. "initial commit") and push to GitHub.
    - `git add .`
    - `git commit -m "initial commit"`
    - `git push origin main`


## Project Organization & Data Files
 - create subfolders for SQL statements and data files in the root project repository folder: `datafun-05-sql-project`
 - add related csv data files to the data subfolder

## Start the Project

Create docstring with brief project intro in `vcr_manager.py`

## Import Dependencies
```python
import sqlite3
import pandas as pd
import pathlib
```

## Logging

Implement logging to enhance debugging and maintain a record of program execution.
Configure logging to write to a file named log.txt.
Log the start of the program using logging.info().
Log the end of the program using logging.info().
Log exceptions using logging.exception().
Log other major events using logging.info().
Log the start and end of major functions using logging.debug().

```python
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")
```

## Schema Design & Database Creation
 - Create new SQLite database file.

 - Design schema with at least two related tables, including foregin key constraints.

```markdown
vcrs: id INTEGER PRIMARY KEY, model TEXT, availability BOOLEAN
customers: id INTEGER PRIMARY KEY, name TEXT, contact_info TEXT
rentals: id INTEGER PRIMARY KEY, customer_id INTEGER, vcr_id INTEGER, rental_date DATE, return_date DATE, with foreign keys to customers and vcrs

```

## SQL Operations
Implement SQL statements and queries to perform table creation, data insertion, data querying (with filters, sorting, and joining tables), data aggregation, and record update and deletion.

Include the following SQL files:

1. create_tables.sql - create your database schema.
2. insert_records.sql - insert at least 10 records into each table.
3. update_records.sql - update 1 or more records in a table.
4. delete_records.sql - delete 1 or more records from a table.
5. query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
6. query_filter.sql - use WHERE to filter data based on conditions.
7. query_sorting.sql - use ORDER BY to sort data.
8. query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
9. query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

## Python and SQL Integration
Use Python to interact with the SQL database and execute SQL commands:

```python
import sqlite3

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

```

## Define Main Function
Implement a main() function to execute the project logic.

## Conditional Script Execution
Ensure the main function only executes when the script is run directly, not when imported as a module by using standard boilerplate code.

## Contributing
We welcome contributions to this project. If you have suggestions to improve the project or encounter issues, please open an issue or submit a pull request.

## References & Acknowledgments
Special thanks to [OpenAI](https://openai.com/) for assistance with troubleshooting and script debugging. Additional references used for this project include:

- [Specification for Project 5 SQL Module](https://github.com/denisecase/datafun-05-spec/blob/main/README.md)