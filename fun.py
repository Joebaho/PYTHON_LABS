'''
PYTHON LAB:fun.py

Write a program that will use all types of variables( string, float , interger and bolean)
Display on the screen: a message using those variables.'''

#Define a string variable
city= "Hollister"

#define a price as a float variable
price= 10.50

#Define an Interger variable as score
high_score= 99

#Define a bolean variale 
is_having_fun= True
is_not_having_fun = False

# Method 3: Using the bool() function
is_having_fun= bool("True")  # True
is_not_having_fun = bool("") 

print("I live in", city ,".") 
print(price, "is the price of a double buger now.")  
print("I got" , high_score , "points in Python program.")
print(is_having_fun, ", I enjoyed my last trip in Dallas.")
print("Do the party was great?", is_not_having_fun)    