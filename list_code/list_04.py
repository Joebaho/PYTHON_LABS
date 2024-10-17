'''
PYTHON LAB: list_04.py

Write a python program to remove all the duplicates from a list

'''
# 1st Solution 
def remove_duplicates(lst):
    """
    Removes duplicate elements from a list and returns a new list with unique elements.
    
    Args:
        lst (list): The input list from which duplicates need to be removed.
        
    Returns:
        list: A new list with unique elements from the input list.
    """
    return list(set(lst))

# Example usage
original_list = [1, 2, 3, 2, 4, 3, 5]
unique_list = remove_duplicates(original_list)
print("Original List:", original_list)
print("Unique List:", unique_list)

# 2nd Solution
l1=[1,2,3,3,3,4,4,5,6,7,8,9,9]
l2=[]
for i in l1:
   if i not in l2:
      l2.append(i)
print(l2)