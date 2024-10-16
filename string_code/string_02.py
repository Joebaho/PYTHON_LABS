'''
PYTHON LAB: string_02.py

Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index
number.
For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

'''
# Enter the text 
string=input("enter the text: ")
# Convert the string to a list
x=list(string)
print(string)
# loop through the list and print the characters at even indices
print("characters at even indices: ")
for i in x[0::2]:
    print(i,end=" ")