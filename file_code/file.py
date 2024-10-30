'''
PYTHON LAB: file.py

This program will present all way of using file in python. 
We wiil go from creation, append, update and delete file the folder. '''

import os
#To open a file for reading it is enough to specify the name of the file:
f = open("fun.py")
#open and read the file after the appending:
f1 = open("list.py", "rt")     #"r" is for read and "t" text
f2 = open("hackaton.py", "rb")     #"r" is for read and "b" binary code
f3 = open("/Users/josephmbatchou/Documents/PYTHON_LABS/list.py", "rt")     #if the file is locally set
print(f1.read())
print(f2.read(5))                    #Return the 5 first characters of the file
print(f3.readline())          #Read one line of the file. By calling readline() two times, you can read the two first lines:
#By looping through the lines of the file, you can read the whole file, line by line:
f4 = open("format.py", "r")
for x in f4:
   print(x)

# It is a good practice to always close the file when you are done with it. It is away of saving the files
f5 = open("operator.py", "r")
print(f5.read())
f5.close()
# To write to an existing file, you must add a parameter to the open() function:
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content
f6 = open("first_print.py", "a")
f6.write("Now the file has more content!")
f6.close()
# open and read the file after the appending:
f7 = open("first_print.py", "r")
print(f7.read())
# Create a new file
f = open("myfile.txt", "x")
f = open("myfile2.txt", "w")

# This part must import the OS module, and run its os.remove() function:##
import os
# Delete an existing file
os.remove("myfile.txt")

#Delete a folder
os.rmdir("myfolder")

# check if file exist then delete it 
if os.path.exists("demofile.txt"):
   os.remove("demofile.txt")
else:
   print("The file does not exist")
# Check file is empty or not,Write a program to check if the given file is empty or not
size=os.stat("test file.txt").st_size
if size==0:
   print("file is empty")
else:
  print("file is not empty")