'''
PYTHON LAB: list_13.py

Remove all occurrences of a specific item from a list.
Given a Python list, write a program to remove all occurrences of item 20.
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
[5, 15, 25, 50]

'''
#First Solution
list1 = [5, 20, 15, 20, 25, 50, 20]
list1 = [x for x in list1 if x != 20]
print(list1)

# Second Solution
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
     list1.remove(20)
print(list1)