'''
PYTHON LAB: swap.py

Write a program that will ask for two integer numbers and swap the number without using the third variable.
Display on the screen:  the sum of the number1 and number is: sum.'''

#Program as user to enter number
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

print(x,y)
x=x+y
y=x-y
x=x-y
print(x,y)
