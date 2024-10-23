'''
PYTHON LAB: operator.py

Use function built in to write a program that will ask a user to provide three numbers. We will realise all arthmetic operation 
Calculate addition, substraction, Multiplication, division moduls, exponent and square-foot.

Display on the screen:  the result of each operation
'''
import math

def python_operator(a, b, c):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division_float = a / b
    division_floor = a // b
    modulus = a % b
    exponent = a ** b
    square_root = math.sqrt(c)
    all = a + b + c + a - b + (a * b) + (a / b + a // b) + a % b + a ** b + math.sqrt(c)
    
    return addition, subtraction, multiplication, division_float, division_floor, modulus, exponent, square_root, all

# Get user input and convert to floats (or ints)
a = float(input('What is the value of a:  '))
b = float(input('What is the value of b:  '))
c = float(input('What is the value of c:  '))

# Call the function with the provided values
result = python_operator(a, b, c)
print(result)

# Display the results
print(f"Addition: {result[0]}")
print(f"Subtraction: {result[1]}")
print(f"Multiplication: {result[2]}")
print(f"Division (Float): {result[3]}")
print(f"Division (Floor): {result[4]}")
print(f"Modulus: {result[5]}")
print(f"Exponent: {result[6]}")
print(f"Square root of {c}: {result[7]}")
print(f"All operations: {result[8]}")

##############################################################################################

import math
# Function for addition
def add(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for division float
def divide_float(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return f"ERROR!!! \n\t{num1} can not be divided by {num2}. \n\tTherefore, will result in ZeroDivisionError: float division by zero"
# Function for division floor
def divide_floor(num2, num3):
    return num2 // num3

# Function for modulus
def modulus(num1, num2):
    return num1 % num2

# Function for exponent
def exponent(num1, num2):
    return num1 ** num2

# Function for square root
def square_root(num3):
    return math.sqrt(num3)

def combination(num1, num2, num3):
    return num1 + num2 + num3 + num1 - num2 + (num1 * num2) + (num1 / num2 + num1 // num2) + num1 % num2 + num1 ** num2 + math.sqrt(num3)

# Function to select the operation
def calculate():
    # Getting input from user
    num1 = float(input("\nPlease enter the first number: "))
    num2 = float(input("\nPlease enter the second number: "))
    num3 = float(input("\nPlease enter the third number: "))

    # Display arithmetic operation options
    print("\nArithmetic operation options:\n\t")
    print("\t1. Addition")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division_float")
    print("\t5. Division_floor")
    print("\t6. Modulus")
    print("\t7. Exponent")
    print("\t8. Square Root")
    print("\t9. Combination")

    # Input: Getting the operation selection
    selection = input("\nPlease enter the number (1,2,3,4,5,6,7,8) of your selection here:  ")

    # Perform calculation based on user's arithmetic operation selection
    if selection == '1':
        result = add(num1, num2)
        operation = f"The addition of {num1} and {num2}"
    elif selection == '2':
        result = subtract(num1, num2)
        operation = f"The subtraction of {num1} and {num2}"
    elif selection == '3':
        result = multiply(num1, num2)
        operation = f"The multiplication of {num1} and {num2}"
    elif selection == '4':
        result = divide_float(num1, num2)
        operation = f"The division_float of {num1} and {num2}"
    elif selection == '5':
         result = divide_floor(num2, num3)
         operation = f"The division_floor of {num2} and {num3}"
    elif selection == '6':
        result = modulus(num1, num2)
        operation = f"The modulus between {num1} and {num2}"
    elif selection == '7':
        result = exponent(num1, num2)
        operation = f"The exponent on {num1} to {num2}"
    elif selection == '8':
        result = square_root(num3)
        operation = f"The Square Root of {num3}"
    elif selection == '9':
        result = combination(num1, num2, num3)
        operation = f"The combination of all operators with {num1}, {num2} and {num3}"
    else:
        return "Invalid input"

    return f"\n{operation.upper()} is: {result:0,.2f}" #2 decimal places in case division returns large decimal

print(f"{calculate()} \n\n\tThank you using our application! Feel free to come back again! See you next time !")




