'''
PYTHON LAB: date_time_04.py

Print a date in a the following format
given_date = datetime(2020, 2, 25)
expected:
Tuesday 25 February 2020

'''

from datetime import datetime
given_date = datetime(2020, 2, 25)
given_date.strftime("%A %d %b %Y")
