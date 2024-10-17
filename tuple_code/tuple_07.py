'''
PYTHON LAB: tuple_07.py.py

Modify the tuple
Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
Expected
tuple1: (11, [222, 33], 44, 55)

'''
tuple1 = (11, [22, 33], 44, 55)
# Convert the tuple to a list to allow modification
list1 = list(tuple1)
# Modify the first item (22) of the list to 222
list1[1][0] = 222
# Convert the modified list back to a tuple
tuple1 = tuple(list1)
print("tuple1:", tuple1)