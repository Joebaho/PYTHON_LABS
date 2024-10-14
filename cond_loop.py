'''
PYTHON LAB: cond_loop.py

This program will contains some conditional and looping program.'''

## Write a python program to search a given number from a list.##
l1=[4,5,6,2,3,9,1,4,5,6,3]
n=int(input("enter the number: "))
for i in l1:
    if i==n:
        print("Number exist")
        break
else:
    print("number dont exist")

########################################################################################################
    
## Write a program to check if the given number is a palindrome number.
## A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers.
    
n=(input("enter the number: "))     
rev_number=n[::-1]
print(rev_number)
if n==rev_number:
   print("the given number is palindrom")
else:
   print("the given number is not palindrom")

######################################################################################################
#Create a new list from a two list using the following condition. Given a two list of
#numbers, write a program to create a new list such that the new list should contain odd numbers
#from the first list and even numbers from the second list.

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[]
for i in l1:
    if i%2!=0:
      l3.append(i)
for i in l2:
    if i%2==0:
      l3.append(i)
print(l3)

#####################################################################################################
# Print multiplication table form 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print("\n")

####################################################################################################
# Print all the armstrong numbers in the range of 100 to 1000
armstrong_list=[]
for i in range(100,1000):
    a=i%10 # 123-->3
    num=i//10 #123-->12
    b=num%10 #--->2
    c=num//10 #-->1
    if (a**3)+(b**3)+(c**3)==i:
       armstrong_list.append(i)
print(armstrong_list)

#####################################################################################################
# Write a program to print all the unique combinations of four digits from 1 to 5 for ex (1,2,3,4)
for i in range(0,5):
    for j in range(0,5):
        if i != j:
            print(i,j)

####################################################################################################
# Write a program to print whether a given number is prime number or not
x=int(input("enter the number: "))
new=[]
if x==1:
   print("1 is not prime number")
else:
   for i in range(1,x+1):
       if x%i==0:
          new.append(i)
#print(new)
   if len(new) > 2:
       print("it is not a prime number")
   else:
       print("it is prime number ")

######################################################################################################
# User will provide 2 numbers you have to find the HCF of those 2 numbers
x=int(input("enter the number: "))
y=int(input("enter the number: "))
x_div=[]
y_div=[]
for i in range(1,x+1):
    if x%i==0:
       x_div.append(i)
for i in range(1,y+1):
    if y%i==0:
       y_div.append(i)
comman_list=[]
for i in x_div:
    if i in y_div:
       comman_list.append(i)
print("HCF of given two number is ",max(comman_list))

###################################################################################################
# User will provide 2 numbers you have to find the by LCM of those 2 numbers
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
if a>b:
   greater=a
else:
   greater=b
while(True):
   if (greater%a==0) and (greater%b==0):
      LCM=greater
      break
   greater+=1
print(LCM)

#####################################################################################################
# Print Pascal Triangle
n=int(input("enter the number: "))
list1=[]
for i in range(0,n):
    temp=[]
    for j in range(0,i+1):
        if j==0 or j==i:
           temp.append(1)
        else:
           temp.append(list1[i-1][j]+list1[i-1][j-1])
    list1.append(temp)
#print(list1)
for i in range(n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print(list1[i][j],end=" ")
    print()

#####################################################################################################
# Print list in reverse order using a loop
l1=[1,2,3,4,5]
for i in l1[::-1]:
    print(i,end=" ")
#####################################################################################################

            

