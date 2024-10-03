'''
PYTHON LAB: get_max_min.py

- Write a Python program that prints the largest and smallest values in a list.
- Print the two values on the same line, separated by a space.
- The largest value should appear first and the smallest value should appear second.
- You may assume that the list only contains numeric values
- If the list is empty, print "None."

Expected output:
[3,4,5,6]       --> 6 3
[-1,-2,-3,-4]   --> -1 -4
[0,0,0,0]       --> 0 0
[]              --> []
'''

my_list_1 = [3,4,5,6]
my_list_2 = [-1,-2,-3,-4]
my_list_3 = [0,0,0,0]
my_list_4 = [] 


print(max(my_list_1), min(my_list_1))
print(max(my_list_2), min(my_list_2))
print(max(my_list_3), min(my_list_3))
print(my_list_4)