'''
PYTHON LAB: operator.py

Write a program that will ask a user to provide three numbers. We will realise all arthmetic operation 
Calculate addition, substraction, Multiplication, division moduls, exponent and square-foot.

Display on the screen:  the result of each operation
'''
import math
#enter value of number 
a= input('What is the value of a:  ')
b= input('What is the value of b:  ')
c= input('what is the value of c:  ')
#erform the math
addition= float(a) + float(b)
Subtraction= float(a) - float(b)
Multiplication= int(a) * int(b)
Division_float= int(a) / int(b)
Division_floor= int(a) // int(b)
Modulus= int(a) % int(b)
Exponent= int(a) ** int(b)
square_root= math.sqrt(int(c))
#Provide result
print(addition) 
print(Subtraction) 
print(Multiplication) 
print(Division_float) 
print(Division_floor) 
print(Modulus) 
print(Exponent)
print(square_root)