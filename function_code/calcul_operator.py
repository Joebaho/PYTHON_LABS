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




