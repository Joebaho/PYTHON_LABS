'''
PYTHON LAB: date_time_03.py

Subtract a week (7 days) from a given date in Python
given_date = datetime(2020, 2, 25)
expected date:
2020-02-18

'''
given_date = datetime(2020, 2, 25)
from datetime import datetime ,timedelta
print(given_date)
days_to_substract=7
res_date=given_date-timedelta(days_to_substract)
print(res_date)
