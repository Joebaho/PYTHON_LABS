'''
PYTHON LAB: set_02.py

 Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output: {40, 50, 30}

'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find the intersection of the two sets
common_items = set1.intersection(set2)

# Print the result
print(common_items)