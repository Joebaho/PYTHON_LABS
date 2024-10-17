'''
PYTHON LAB: list_17.py

what is easiest way to shuffle the list

'''
# Firt Solution
from random import shuffle
list1=["Milind","Kanchan","Rohit","Shashi"]
shuffle(list1)
print(list1)

#Second Solution

import random

def shuffle_list(lst):
    """Shuffles the given list randomly."""
    random.shuffle(lst)
    return lst

# Example usage
original_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(original_list)
print(shuffled_list)