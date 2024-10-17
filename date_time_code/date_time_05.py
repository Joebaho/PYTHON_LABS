'''
PYTHON LAB: date_time_04.py

Find the day of the week of a given date
Given:
given_date = datetime(2020, 7, 26)
Expected output:
Sunday

'''
from datetime import datetime

def get_day_of_week(date):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days_of_week[date.weekday()]

# Example usage
given_date = datetime(2020, 7, 26)
day_of_week = get_day_of_week(given_date)
print(day_of_week)

################################################################################

given_date = datetime(2020, 7, 26)
given_date.strftime("%A")