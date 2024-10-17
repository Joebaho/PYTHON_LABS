'''
PYTHON LAB: tuple_06.py.py

Copy specific elements from one tuple to a new tuple
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)
Expected
tuple2: (44, 55)

'''
tuple1 = (11, 22, 33, 44, 55, 66)

# Create a new tuple with the elements 44 and 55
tuple2 = (tuple1[3], tuple1[4])

# Print the new tuple
print("tuple2:", tuple2)   


#####################################################
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[3:5]
print(tuple2)