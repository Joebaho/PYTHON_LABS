'''
PYTHON LAB:function.py

This part of the program will show how to write function whicj is  a block of code which only runs when it is called .
You can pass data, known as parameters, into a function. A function can return data as a result.
Here are all ways on playing with function in python.'''

# Print a simple function that will display a sentence.
def my_function():
  print("Hello from a function")
my_function() 

# Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emile", "Layton")

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[1])
my_function("Emil", "Tobias", "Linus")

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("The kid first name is " +kid["fname"])
my_function(fname = "Tobias", lname = "Refsnes")   

# Default value The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")                              
my_function() 

# Passing a list as argument
def my_function(fruits):
  for x in fruits:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return value
def my_function(x):
  return 5 * x
print(my_function(3)) 