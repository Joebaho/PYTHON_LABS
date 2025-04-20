'''
PYTHON LAB: list_01.py

Write a python program to find the max and min item from a list without using the max function

'''
#First Solution 
l1=[4,6,2,8,1]
l1.sort(reverse=False)
l1.sort(reverse=True)
print(l1)
print(l1[0])
print(l1[4])

#second Solution
def find_max_min(lst):
    if not lst:
        return None, None  # Handle empty list case

    max_value = lst[0]
    min_value = lst[0]

    for num in lst:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

# Example usage
numbers = [10, 3, 5, 7, 99, 2, -8, 45]
maximum, minimum = find_max_min(numbers)
print(f"Maximum: {maximum}, Minimum: {minimum}")
