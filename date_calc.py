# A date calculator for use in genealogy

import datetime
from dateutil.relativedelta import relativedelta

# Turns on and off bold text attribute
b_on = "\033[1;31m"
b_off = "\033[0m"


def calc_diff():
    """Takes two user supplied dates and calculates the differences between them."""
    print("\nEnter the dates as '1899-3-14' (Year, Month, Day) when prompted")

    starting = input("Enter the first date: ")
    STARTDATE = datetime.datetime.strptime(starting, "%Y-%m-%d")

    ending = input("\nEnter the second date: ")
    ENDDATE = datetime.datetime.strptime(ending, "%Y-%m-%d")
    calculation = relativedelta(ENDDATE, STARTDATE)
    output = str(calculation)
    output = output.strip("relativedelta(")
    output = output.strip(")")

    print(
        "\nIf the results show '+', the second date is later than the first by that amount."
    )
    print(
        "If the results show '-', the second date is earlier than the first by that amount."
    )

    print(f"\nThe difference from the first date is: {output}")


def future_calc_date():
    """Takes a user entered date, prompts for a difference in 'years,months,days' format,
    and calculates the new date by adding the difference from the original date.
    """
    print("\nEnter the starting date as year, month, day as year-month-day.")
    date_entered = input("\nWhat is the starting date?: ")
    stdate = datetime.datetime.strptime(date_entered, "%Y-%m-%d")

    print("\nNow enter the number of years, months and days separated by commas: ")
    print(
        f"{b_on}NOTE{b_off} all fields must have a number greater than 0, if 0 enter a 1 instead."
    )
    difference = input("\nEnter the difference: ")

    m_year, m_month, m_day = difference.split(",")

    newy = int(m_year)
    newm = int(m_month)
    newd = int(m_day)

    differ = relativedelta(years=newy, months=newm, days=newd)
    newyear = (stdate + differ).strftime("%Y-%m-%d")

    print(f"\nThe date is {newyear}.")


def past_calc_date():
    """Takes a user entered date, prompts for a difference in 'years,months,days' format,
    and calculates the new date by subtracting the difference from the original date.
    """
    print("\nEnter the starting date as year, month, day as year-month-day.")
    date_entered = input("\nWhat is the starting date?: ")
    stdate = datetime.datetime.strptime(date_entered, "%Y-%m-%d")

    print("\nNow enter the number of years, months and days separated by commas: ")
    print(
        f"{b_on}NOTE{b_off} all fields must have a number greater than 0, if 0 enter a 1 instead."
    )

    difference = input("\nEnter the difference: ")

    m_year, m_month, m_day = difference.split(",")

    newy = int(m_year)
    newm = int(m_month)
    newd = int(m_day)

    differ = relativedelta(years=newy, months=newm, days=newd)
    newyear = (stdate - differ).strftime("%Y-%m-%d")

    print(f"\nThe date is {newyear}.")


print("What kind of calculation do you want, enter letter of choice:\n")
print(
    """(d) difference between dates
(f) for span into future
(p) for span into past\n"""
)
choice = input("Which option do you want?: ")

if choice == "d":
    calc_diff()
elif choice == "f":
    future_calc_date()
elif choice == "p":
    past_calc_date()
else:
    print("See you later!")
    exit()
