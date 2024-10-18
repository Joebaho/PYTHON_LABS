'''
PYTHON LAB:function_labs.py

This part of the program will show how to write function whicj is  a block of code which only runs when it is called .
You can pass data, known as parameters, into a function. A function can return data as a result.
Here are all ways on playing with function in python.'''

###############################################################################################################

# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
def exponent(base,exp):
    result=pow(base,exp)
    print(result)
exponent(10,2)

################################################################################################################

#  Write a program to create a function that takes two arguments, name and age, and print their value.
def biodata(name,age):
   print("Name of the person is {} and age is {}".format(name,age))
biodata("Milind",26)

################################################################################################################

# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
l1=[1,2,3,4,5,1]
num1=l1[0]
num2=l1[-2]
def xyz(list):
   if num1==num2:
      return True
   else:
      return False
xyz(l1)

###################################################################################################################

# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
num1=int(input("enter the number: " ))
num2=int(input("enter the number: " ))
def mul_sum_int(num1,num2):
#calculate product of two number
   mul=num1*num2
   total=num1+num2
#checking if product is less than 1000
   if mul<=1000:
      return mul
   else:
      return total
print(mul_sum_int(num1,num2))

###########################################################################################################################
# collecting arbitrary number of arguments to make a pizza
def make_pizza(size,*toppings):
    print(f"making {size} pizza")
    print("toppings: ")
    for i in toppings:
        print(i)
make_pizza("small","butter")
make_pizza("medium","amli","paeri","dijvoe")

###############################################################################################################################
# collecting arbitrary number of keyword arguments
def build_profile(fname, lname, **userinfo):
    # build dictionary
    profile = {"First Name": fname, "Last Name": lname}
    for key, value in userinfo.items():
        profile[key] = value  # Corrected this line
    return profile

# Correct function calls
print(build_profile("milind", "mali"))
print(build_profile("milind", "mali", age=26, Loc="Pune"))

###################################################################################################################################
# Write a program to create function calculation() such that it can accept two variables and calculate
#addition and subtraction. Also, it must return both addition and subtraction in a single return call.
def add_sub():
   n1 = int(input("Enter the first number: "))
   n2 = int(input("enter thesecond number: "))
   x1=n1+n2
   x2=n1-n2
   return x1,x2
result = add_sub()
print(f"Addition: {result[0]}, Subtraction: {result[1]}")

#######################################################################################################################
# Generate a Python list of all the even numbers between 2 to 30
for i in range(2,31):
    if i%2==0:
       print(i,end=" ")

#######################################################################################################################
# first 25 prime number
def is_prime(x):
    new=[]
    if x<=1:
       return False
    else:
        for i in range(1,x+1):
            if x%i==0:
               new.append(i)
#print(new)
    if len(new)<=2:
        return True
    else:
        return False
#now will write the main code
count=0
num=2
while count<25:
    if is_prime(num)==True:
        print(num,end=" ")
        count+=1
    num+=1

######################################################################################################
# Print the first 20 numbers of a Fibonacci series
n=int(input("enter the number: "))
def fibonacci(n):
    a=0
    b=1
    count=0
    if n<=0:
       print("You can enter only Positive integer values")
    elif n==1:
       print(a)
    else:
       while count<n:
            print(a,end=' ')
            c=a+b
            a=b
            b=c
            count+=1
fibonacci(n)

########################################################################################################
# Write the logic for strong number strong number in python
n=int(input("enter the number: "))
total=0
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
for i in str(n):
    x=fact(int(i))
    total+=x
if n==total:
   print("It is strong number")
else:
   print("it is not a strong number")
#####################################################################################################################


