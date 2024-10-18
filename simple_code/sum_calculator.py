'''
PYTHON LAB: sum_calculator.py

Write a program that will ask for two numbers (integer or float) and calculate the sum of those two numbers.
Display on the screen:  the sum of the number1 and number is: sum.'''

#enter value of number 
number1= float(input('What is the value of number1:  '))
number2= int(input('What is the value of number2:  '))

#perform the math
addition= float(number1) + float(number2)
summarization= int(number1) + int(number2)

#message 
sum1 = f"The  float sum of {number1} and {number2} is : {addition}  "
sum2 = "The integer sum of {} and {} is : {} " .format(number1, number2, summarization)

#Provide result
print(sum1)
print(sum2) 

