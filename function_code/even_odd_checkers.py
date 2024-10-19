'''
PYTHON LAB: even_odd_checkers.py

Check for even or odd number

Write a program that will ask a user for a number then check whether that number is EVEN or ODD.
And at the same time it will tell if the number is positive or negative.
Display on the screen:
Please enter a number between 1-100
Your number user_number is even/odd.'''

################################################################################################
def is_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from the user
try:
    user_input = int(input("Enter a number: "))
    result = is_odd_or_even(user_input)
    print(f"The number {user_input} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

###############################################################################################
def is_odd_or_even(number):
    if number % 2 == 0 and number > 0:
        return "Even and positive"
    elif number % 2 == 0 and number < 0:
        return "Even and negative"
    elif number % 2 == 0 and number == 0:
        return "Nul"
    elif number % 2 != 0 and number > 0:
        return "odd and positive"
    elif number % 2 != 0 and number < 0:
        return "odd and negative"
    else:
        return "Invalid input. Please enter a valid number"

# Get input from the user
try:
    user_input = int(input("Enter a number: "))
    result = is_odd_or_even(user_input)
    print(f"The number {user_input} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")