'''
PYTHON LAB: list_16.py

logic for quickly swap the first and last number of the list

'''
# First Solution

l1=[1,2,3,4,5]
temp=l1[-1]
l1[-1]=l1[0]
l1[0]=temp
print(l1)

#Second Soluiton
def swap_first_last(lst):
    if len(lst) < 2:
        return lst
    else:
        first = lst[0]
        last = lst[-1]
        lst[0] = last
        lst[-1] = first
        return lst

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
swapped_list = swap_first_last(my_list)
print("List after swapping first and last elements:", swapped_list)
