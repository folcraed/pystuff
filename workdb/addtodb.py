# Creates and/or adds to the database

import sqlite3
from sqlite3 import Error

path = "./work.db"


def create_connection(the_path):
    """Create the connection to the database"""
    c_connection = None
    try:
        c_connection = sqlite3.connect(the_path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return c_connection


connection = create_connection(path)


def execute_query(q_connection, query):
    """Creates an access point to work with the data"""
    cursor = q_connection.cursor()
    try:
        cursor.execute(query)
        q_connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Create tables if they don't exist, connect to them if they do
create_employees_table = """
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT
);
"""

execute_query(connection, create_employees_table)


def add_employee():
    """Function to add employee data to the database
    asks the user for the name, then the occupation"""
    new_name = input("Enter the employee's name: ")
    title = input("Enter the employee's title: ")
    create_employee = "INSERT INTO employees (name, position) VALUES ('%s', '%s')" % (
        new_name,
        title,
    )
    execute_query(connection, create_employee)


add_new = input("Do you want to add an employee?: ")

if add_new == "y":
    add_employee()
else:
    exit(0)
