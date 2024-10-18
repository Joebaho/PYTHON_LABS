'''
PYTHON LAB: digit_reverse.py

Write a program that will ask for four digit integer numbers, then reverse them and check,
whether the reverse is equal to the given one.
Display on the screen:  the reverse number is : rev and number is: (True or False).'''

#Program as user to enter number
# x=int(input("Enter the four digit number: "))

# a = x%10    #We get last digit
# num_1 = x//10 #interger-division here we will get first two digit
# b = num_1%10 #heree we will get last digit of two digit number
# num_2 = num_1//10 #here will get first two digit
# c = num_2%10 # here we will get second  number
# d = num_2//10 #here we get 1st digit
# #formula for reverse
# rev = a*1000+b*100+c*10+d
# #result
# print(rev)
# #now let check if rev==x
# if x==rev:
#     print("True")
# else:
#     print("False")  

#####################################################################################################  
def reverse_number(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    return num == reverse_number(num)

# Ask for input
while True:
    try:
        number = int(input("Enter a four-digit integer: "))
        if 1000 <= number <= 9999:
            break
        else:
            print("Please enter a four-digit number.")
    except ValueError:
        print("Invalid input. Please enter a four-digit integer.")

# Reverse the number
reversed_num = reverse_number(number)

# Check if it's a palindrome
palindrome_check = is_palindrome(number)

# Display results
print(f"The reverse number is: {reversed_num}")
print(f"Number is palindrome: {palindrome_check}")