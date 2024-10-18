'''
PYTHON LAB: triangle_print.py

Write a python program that will print an equilateral triangle'''

# First way of doing this 
#################################################################################
# This first code will display a equilateral triangle
print("           #")
print("         #   #")
print("        #     #")
print("       #       #")
print("      #         #")
print("     #           #")
print("    #             #")
print("   #               #")
print("  #                 #")
print(" #####################")

print(" Here is my first Python Homework. It is a triangle")
#################################################################################

#Second way

#Declaration of variables
top_level = "\t" 
empty = " "
lenght = "#"
bottom_level = "#" * 25

# Print the banner
print(top_level + lenght + "\n")
print(empty * 6 +lenght + empty * 4 + lenght +"\n")
print(empty * 5 +lenght + empty * 7 + lenght +"\n")
print(empty * 4 +lenght + empty * 10 + lenght +"\n")
print(empty * 3 +lenght + empty * 14 + lenght +"\n")
print(empty * 2 +lenght + empty * 17 + lenght +"\n")
print(empty + lenght + empty * 21 + lenght + "\n")
print(bottom_level)

#######################################################################################################

# Third way 
n=int(input("enter the number: "))
for i in range(0,n):
    for j in range(0,n-i):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()

####################################################################################################
#  Triangle rectangle
n=int(input("enter the number : "))
for i in range(n+1,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print("\n")

###################################################################################################
# Triangle isocele as arrow
n=int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
for i in range(n-1,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")

####################################################################################################