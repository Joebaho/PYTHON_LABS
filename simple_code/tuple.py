'''
PYTHON LAB: tuple.py

This program will present all way of using tuple in python. '''

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple is ordered, unchangeable and allow duplicate. Tuple use regular brackets. 

# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#first tuple assignig value to a tuple is called packing a tuple
friends_tuple = ('John','Michael','Terry','Eric','Graham')                                                                                                       
print(friends_tuple)

# To extract the value back into variables is called Unpacking
fruits = ("avocado", "banana", "mango")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#or
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Tuple allow slicing as list 
print(friends_tuple[2])                                                              
print(friends_tuple[2:4])
print(friends_tuple[:5])
print(friends_tuple[-1])

# Check if an element exist in the tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
thetuple = ("apple", "banana", "cherry")
for i in range(len(thetuple)):
  print(thetuple[i]) 
# You can also use the while loop
tuple = ("apple", "banana", "cherry")
i = 0
while i < len(tuple):
  print(tuple[i])
  i = i + 1
#to create empty tuple
empty_tuple1 = ()
#empty_tuple2 = tuple()

# You can check the type and len of the tuple
print(type(friends_tuple))
print(len(friends_tuple))

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
my_tuple = ("apple", "banana", "cherry")
y = ("pineaple",)
my_tuple += y
print(my_tuple)

print(thistuple)
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print(y)

# append on tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
x= tuple(y)
print(x)

#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
a = ("apple", "banana", "cherry")
b = list(a)
b.remove("apple")
a = tuple(y)
print(a)
print(b)

# To delete the tuple completely
second_tuple = ("apple", "banana", "cherry")
del second_tuple  

# To join two or more tuples you can use the + operator:
tuple_1 = ("access", "building" , "site")
tuple_2 = (1, 2, 3)

tuple_3 = tuple_1 + tuple_2
print(tuple_3)
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
new_fruits = fruits * 2
print(new_fruits)




