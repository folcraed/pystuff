"""
This was one of the examples from the lesson book that I think would be very
handy for calculating genealogical dates. It will need to be expanded upon,
but is a good starting point, showing how datetime can do date arithmetic.
"""
# TODO I want to expand on this later to use for calculating genealogy dates

import datetime


def addDays(year, month, day, increment):
    startdate = datetime.datetime(year, month, day)
    enddate = startdate + datetime.timedelta(days=increment)
    return enddate.year, enddate.month, enddate.day


y, m, d = addDays(2015, 11, 13, 55)
print(f"{y}/{m}/{d}")
