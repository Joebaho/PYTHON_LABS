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