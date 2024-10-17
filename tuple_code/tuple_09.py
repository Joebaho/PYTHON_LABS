'''
PYTHON LAB: tuple_09.py

Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)

'''
tuple1 = (50, 10, 60, 70, 50)

# Initialize a counter variable
count = 0

# Iterate through the tuple
for item in tuple1:
    # Check if the item is 50
    if item == 50:
        # Increment the counter if it is
        count += 1

# Print the final count
print(f"The number of occurrences of 50 in the tuple is: {count}")

###########################################################################
t = (45, 45, 45, 45)
#to check whether all the item are same
all_same=all(i==t[0] for i in t)
if all_same:
   print("yes all the item are same in the given tuple")
else:
   print("No all the item are not same in the given table")