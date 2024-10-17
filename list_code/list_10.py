'''
PYTHON LAB: list_10.py

Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

'''
# 1st Solution 
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
new_item = 7000
target_list = list1[2][2]  # Access the inner list [5000, 6000]
target_list.append(new_item)  # Add the new item to the inner list
print(list1)  # Output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

#Second Solution
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
