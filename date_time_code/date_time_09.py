'''
PYTHON LAB: date_time_09.py

Calculate the date 4 months from the current date
Given:
#2020-02-25
given_date = datetime(2020, 2, 25).date()
Expected output:
2020-06-25

'''
from datetime import datetime, timedelta

def add_months(given_date, months_to_add):
    new_month = given_date.month + months_to_add
    new_year = given_date.year + (new_month // 12)
    new_month = new_month % 12 or 12
    last_day_of_new_month = datetime(new_year, new_month % 12 or 12, 1).date() - timedelta(days=1)
    return last_day_of_new_month.replace(day=min(given_date.day, last_day_of_new_month.day))

# Example usage
given_date = datetime(2020, 2, 25).date()
result = add_months(given_date, 4)
print(result)

##########################################################
from dateutil.relativedelta import relativedelta
given_date = datetime(2020, 2, 25).date()
months_to_add=4
result_date=given_date+relativedelta(months= + months_to_add)
print(result_date)