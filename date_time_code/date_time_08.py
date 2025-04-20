'''
PYTHON LAB: date_time_07.py

 Convert the following datetime into a string
Given:
given_date = datetime(2020, 2, 25)
Expected output:
"2020-02-25 00:00:00"

'''
from datetime import datetime
given_date = datetime(2020, 2, 25)
string_date=given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)