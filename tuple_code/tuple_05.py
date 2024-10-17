'''
PYTHON LAB: tuple_05.py.py

Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)

'''
tuple1 = (11, 22)
tuple2 = (99, 88)

print("Original tuples:")
print(tuple1)
print(tuple2)

# Swap the tuples
tuple1, tuple2 = tuple2, tuple1

print("\nTuples after swapping:")
print(tuple1)
print(tuple2)