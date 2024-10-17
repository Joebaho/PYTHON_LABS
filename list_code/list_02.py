'''
PYTHON LAB: list_02.py

Find the reverse of a number provided by the user(any number of digit)

'''
# First Solution
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reverse of the number is:", rev)

# Second Solution
n=int(input("enter the number: "))
digit_list=list(map(int,str(n)))
digit_list=digit_list[::-1]
num=int("".join(map(str,digit_list)))
print(num)