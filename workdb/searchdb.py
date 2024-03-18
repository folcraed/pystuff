# Searches the employee database of information.

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


def execute_read_query(r_connection, query):
    """Reads the query data from the database"""
    cursor = r_connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def view_employees():
    """Shows a list of all the employees and their jobs"""
    show_all = "SELECT * FROM employees"
    posts = execute_read_query(connection, show_all)
    for employee in posts:
        (num, first, title) = employee
        print(f"Employee {num} is {first} who is company {title}.")


def search_employee_by_name():
    """Searches the database for an employee by their name"""
    employee = input("Which employee are you looking for?: ")
    employee_chosen = (
        "SELECT name, position FROM employees WHERE name = '%s'" % employee
    )
    employee_description = execute_read_query(connection, employee_chosen)
    if len(employee_description) == 0:
        print(f"{employee} doesn't work here.")
    for chosen in employee_description:
        (first, title) = chosen
        print(f"{first} is company {title}.")


def search_employee_by_title():
    """Searches the database for employees by their occupation"""
    employee = input("Which occupation are you looking for?: ")
    employee_chosen = (
        "SELECT name, position FROM employees WHERE position = '%s'" % employee
    )
    employee_description = execute_read_query(connection, employee_chosen)
    if len(employee_description) == 0:
        print(f"There is no {employee} position in this company.")
    for chosen in employee_description:
        (first, title) = chosen
        print(f"{first} is company {title}.")


print()
print("Options are: (a) to see all employees,")
print("(s) to search employees by name, or")
print("(p) to search employees by position")
print("Anything else will exist the program")
print()

start = input("What would you like to do?: ")

if start == "a":
    view_employees()
if start == "s":
    search_employee_by_name()
if start == "p":
    search_employee_by_title()
else:
    exit(0)
