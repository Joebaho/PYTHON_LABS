'''
PYTHON LAB: Check for even or odd number

Write a program that will ask a user for a number then check whether that number is EVEN or ODD.
And at the same time it will tell if the number is positive or negative.
Display on the screen:
Please enter a number between 1-100
Your number user_number is even/odd.'''
#################################################################################################
# def is_odd_or_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Get input from the user
# try:
#     user_input = int(input("Enter a number: "))
#     result = is_odd_or_even(user_input)
#     print(f"The number {user_input} is {result}.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

################################################################################################
# def is_odd_or_even(number):
#     if number % 2 == 0 and number > 0:
#         return "Even and positive"
#     elif number % 2 == 0 and number < 0:
#         return "Even and negative"
#     elif number % 2 == 0 and number == 0:
#         return "Nul"
#     elif number % 2 != 0 and number > 0:
#         return "odd and positive"
#     elif number % 2 != 0 and number < 0:
#         return "odd and negative"
#     else:
#         return "Invalid input. Please enter a valid number"

# # Get input from the user
# try:
#     user_input = int(input("Enter a number: "))
#     result = is_odd_or_even(user_input)
#     print(f"The number {user_input} is {result}.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

##############################################################################################

# Ask the user for a number
num = float(input("Please enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    pos_neg = "positive"
elif num < 0:
    pos_neg = "negative"
else:
    pos_neg = "zero"

# # Check if the number is even or odd (only applies if the number is an integer)
if num < 1 or num > 100:
    print(f"Please try again -- you entered {num}")  
if num.is_integer():
    if int(num) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
else:
    even_odd = "not an integer, so can't determine even/odd"

# Output the result
print(f"The number {num} is {pos_neg} and {even_odd}.")
    
#################################################################################################