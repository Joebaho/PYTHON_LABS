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

# my_list_1 = [3,4,5,6]
# my_list_2 = [-1,-2,-3,-4]
# my_list_3 = [0,0,0,0]
# my_list_4 = [] 


# print(max(my_list_1), min(my_list_1))
# print(max(my_list_2), min(my_list_2))
# print(max(my_list_3), min(my_list_3))
# print(my_list_4)

##########################################################################
# def print_largest_smallest(lst):
#     if len(lst) == 0:
#         print("None")
#     else:
#         largest = max(lst)
#         smallest = min(lst)
#         print(f"{largest} {smallest}")

# # Example test cases
# print_largest_smallest([3, 4, 5, 6])       # Output: 6 3
# print_largest_smallest([-1, -2, -3, -4])   # Output: -1 -4
# print_largest_smallest([0, 0, 0, 0])       # Output: 0 0
# print_largest_smallest([])                 # Output: None

#########################################################################
my_list = [3,4,5,6]

# using the if statement with the max and min built-in functions for my_list 1 and 2
if my_list:
    print (max(my_list), min(my_list))
    
else:
    print (my_list, "None")
    
# List 2    
my_list = [-1,-2,-3,-4]
if my_list:
    print (max(my_list), min(my_list))
    
else:
    print (my_list, "None")

# List 3
# On this example, i'm trying the index method to fetch the max and min num (I know they're all zero's but wanted to see the outcome)

my_list = [0,0,0,0]
if my_list:
    print (my_list[0], my_list[3])
    
else:
    print (my_list, "None")    
    
# List 4    
my_list = []

if my_list:
    print (max(my_list), min(my_list))
    
else:
    print ([])

#################################################################################################
number_list = [
    [3, 4, 5, 6],       # Expected Output: 6 3
    [-1, -2, -3, -4],   # Expected Output: -1 -4
    [0, 0, 0, 0],       # Expected Output: 0 0
    []                  # Expected Output: None
]

# Look through each number list
for my_list in number_list:
    if len(my_list) == 0:
        print("None")
    else:
        print(max(my_list), min(my_list))


####################################################################################################

lists = [[3,4,5,6], [-1,-2,-3,-4], [0,0,0,0], []]  # List of lists

for sublist in lists:
    if len(sublist) == 0:
        print("None")
    else:
        largest = max(sublist)
        smallest = min(sublist)
        print(f"{largest} {smallest}")