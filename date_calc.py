# A date calculator for use in genealogy

import datetime
from dateutil.relativedelta import relativedelta


def calc_diff():
    """Takes two user supplied dates and calculates the differences between them."""
    print("Enter the dates as '1899-3-14' (Year, Month, Day) when prompted")

    starting = input("Enter the first date: ")
    STARTDATE = datetime.datetime.strptime(starting, "%Y-%m-%d")

    ending = input("Enter the second date: ")
    ENDDATE = datetime.datetime.strptime(ending, "%Y-%m-%d")
    calculation = relativedelta(ENDDATE, STARTDATE)
    output = str(calculation)
    output = output.strip("relativedelta(")
    output = output.strip(")")

    print()
    print(
        "If the results show '+', the second date is later than the first by that amount."
    )
    print(
        "If the results show '-', the second date is earlier than the first by that amount."
    )
    print()
    print(f"The difference from the first date is: {output}")


def calc_date():
    """Takes a user entered date, prompts for a difference in 'years,months,days' format,
    and calculates the new date by subtracting the difference from the original date.
    """
    print("Enter the starting date as year, month, day as year-month-day.")
    date_entered = input("What is the starting date?: ")
    stdate = datetime.datetime.strptime(date_entered, "%Y-%m-%d")

    print("Now enter the number of years, months and days separated by commas: ")
    print("NOTE all fields must have a number greater than 0, if 0, enter a 1 instead.")
    difference = input("Enter the difference: ")

    m_year, m_month, m_day = difference.split(",")

    newy = int(m_year)
    newm = int(m_month)
    newd = int(m_day)

    differ = relativedelta(years=newy, months=newm, days=newd)
    newyear = (stdate - differ).strftime("%Y-%m-%d")

    print(newyear)


print("What kind of calculation do you want,")
print("(d)ifference between dates, or from (t)imespan?")
print("Enter 'd' for dates, 't' for timespan, anything else to quit.")
print
choice = input("Which option?: ")

if choice == "d":
    calc_diff()
elif choice == "t":
    calc_date()
else:
    print("See you later!")
    exit()
