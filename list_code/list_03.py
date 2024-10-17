'''
PYTHON LAB: list_03.py

Take a number from the user and find the number of digits in it.

'''
# First solution 
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)

# Second Slution
n=int(input("enter the number: "))
digit_list=list(map(int,str(n)))
print(digit_list)
print(len(digit_list))