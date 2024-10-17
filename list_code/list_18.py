
'''
PYTHON LAB: list_18.py

create lambda function for the sum of all the elements in the list

'''
#First Solution
from functools import reduce
l1=[5,8,10,20,50,100]
from functools import reduce
result=reduce(lambda x,y:x+y, l1)
print(result)

#Second Solution
from functools import reduce
def sum_list(lst):
    return reduce(lambda x, y: x + y, lst)

# Test the function
list1 = [1, 2, 3, 4, 5]
print(sum_list(list1))  # Output: 15