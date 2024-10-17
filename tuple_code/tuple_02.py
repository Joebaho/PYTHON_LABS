'''
PYTHON LAB: tuple_02.py.py

Access value 20 from the tuple
The given tuple is a nested tuple. write a Python program to print the value 20.
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

'''
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# Access the value 20 from the nested tuple
value = tuple1[1][1]
print(value)  # Output: 20