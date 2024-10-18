'''
PYTHON LAB: swap.py

Write a program that will ask for three digit integer numbers and calculate the sum of those digits.
Display on the screen:  the sum of the number1 and number is: sum.'''

#Program as user to enter number
x=int(input("Enter the three digit number: "))

a = x%10    #We get last digit
num = x//10 #interger-division here we will get first two digit
b = num%10 #heree we will get last digit of two digit number
c = num//10 # here we will get first digit of two digit number
result = a+b+c

print(result)