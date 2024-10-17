'''
PYTHON LAB: set_08.py

 Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected;
{70, 10, 20, 60}

'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Create a new set by taking the union of set1 and set2
# and subtracting the intersection of set1 and set2
set3 = set1.union(set2) - set1.intersection(set2)

print(set3)

#####################################################################

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)