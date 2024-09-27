'''
PYTHON LAB:banner.py

Write a program that will write the given banner in a rectangle made with the pounds sign(#)
Display on the screen:  The result '''

#Declaration of variables
top_level = "#" * 65
lenght = "#"
space = "\t" * 8
name = "Joseph"
banner = "WELCOME TO STREET FIGHTER : "
bottom_level = "#" * 65

# Print the banner
print(top_level + "\n")
print(lenght + space + lenght + "\n")
print(lenght + "\t" * 2 + banner + name + "\t" * 2 + lenght +"\n")
print(lenght + space + lenght + "\n")
print(bottom_level)