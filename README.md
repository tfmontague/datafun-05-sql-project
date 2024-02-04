# datafun-05-sql-project - P5: Python and SQL Project

## Overview

This repository integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations

## Project Stucture

- `datafun-05-sql-project`: Project repository
- `README.md`: Provides an overview of the project, as well as instructions for setting up and executing the environment.
- `requirements.txt`: Lists all packages required for the project.
- `tmontague_sql.py`: Python file


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


## Project Organization
 - create subfolders for SQL statements and data files in the root project repository folder: `datafun-05-sql-project`
 - add related csv data files to the data subfolder

## Start the Project

Create docstring with brief project intro in `tmontague_sql.py`

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


