'''
PYTHON LAB: month_day_number.py.py

Write a program that will ask a user for a month of a year an that will check the number of days 
of the month and finally displey that.
'''
def num_days(month):  #month_31, month_30 month_28

    if month == 'jan':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    elif month == 'mar':
        print('number of days in',month,'is',31)
    elif month == 'apr':
        print('number of days in',month,'is',30)
    elif month == 'may':
        print('number of days in',month,'is',31)
    elif month == 'jun':
        print('number of days in',month,'is',30)
    elif month == 'jul':
        print('number of days in',month,'is',31)
    elif month == 'aug':
        print('number of days in',month,'is',31)
    elif month == 'sep':
        print('number of days in',month,'is',30)
    elif month == 'oct':
        print('number of days in',month,'is',31)
    elif month == 'nov':
        print('number of days in',month,'is',30)
    elif month == 'dec':
        print('number of days in',month,'is',31)

num_days('oct')

#1st Solution
def num_days(month):

    if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        print('The number of days in month of',month,'is',31)
    elif month == 'feb':
        print('The number of days in month of',month,'is',28)
    elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        print('The number of days in month of',month,'is',30)
month = input('What is the month (3-letter abbreviation, e.g., jan, feb): ').lower()
num_days(month)

#2nd solution 
def num_days(month): 
    
    if month == 'feb': 
        print('The number of days in month of',month,'is',28)
    elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        print('The number of days in month of',month,'is',30)
    else:
        print('The number of days in month of',month,'is',31)
month = input('Enter the month: ')
num_days(month)

#3rd Solution
month = input('What is the month (3-letter abbreviation, e.g., jan, feb): ').lower()

def num_days(month):
    if month in ['apr', 'jun', 'sep', 'nov']:
        days = 30
    elif month in ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']:
        days = 31
    elif month == 'feb':
        days = 28 or days == 29  # Handle leap year (29 days in February)   
    else:
        return "Invalid month"  # Handle invalid month input

    return days
result = num_days(month)
print(f'The number of days in month of {month} is {result}')

#4th Solution
def num_days(month):
    days = 31
    if month in {'apr','jun','sep','nov'}: # you can use list , tuple or set it will works
    #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)
num_days('jan')