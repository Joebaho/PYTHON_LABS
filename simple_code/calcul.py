a= input('What is the value of a:  ')
b= input('What is the value of b:  ')
c= input('what is the value of c:  ')
addition= float(a) + float(b)
Subtraction= float(a) - float(b)
Multiplication= int(a) * int(b)
Division_float= int(a) / int(b)
Division_floor= int(a) // int(b)
Modulus= int(a) % int(b)
Exponent= int(a) ** int(b)
import math
square_root= math.sqrt(int(c))

print(addition) 
print(Subtraction) 
print(Multiplication) 
print(Division_float) 
print(Division_floor) 
print(Modulus) 
print(Exponent)
print(square_root)

# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')

# calcul of square of number 
        
squares = []
for x in range(1, 11):
    squares.append(x**2)
print(squares)
