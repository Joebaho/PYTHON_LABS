'''
PYTHON LABS: writing_list.py

Write a Python program that writes the elements of a list to the file denoted by the variable file.
Each element should be written on a separate line.
The file should be new or its existing content must be replaced by this new content.
If this is the list: [1, 2, 3, 4, 5]
After running the program, the content of the file should be:
1
2
3
4
5
'''
############################################################################################
def write_list_to_file(list_data, file_name):
    with open(file_name, 'w') as file:
        for item in list_data:
            file.write(str(item) + '\n')

list_data = [1, 2, 3, 4, 5]
file_name = 'output.txt'
write_list_to_file(list_data, file_name)

for item in list_data:
    print(f"{item} \n")

###########################################################################################
my_list = [1, 2, 3, 4, 5]

with open('list_file.txt', 'w') as file:
    for item in my_list:
        file.write(str(item) +'\n')
        print(f"{item} \n")

for item in list_data:
    print(f"{item} \n")

##########################################################################################
        
import shutil
my_list = [1, 2, 3, 4, 5]

with open('list_file.txt', 'w') as file:
    for item in my_list:
        file.write(str(item) +'\n')
with open('list_file.txt', "r") as f1:
        print(f1.read())

    # Copy the contents of source_file to destination_file
shutil.copy('list_file.txt', 'copy_file.txt')
with open('copy_file.txt', "r") as file2:
        print(file2.read())
#########################################################################################

def write_list_to_file(list, file_name):
    with open(file_name, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')

def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            # Copy content from source to destination
            for line in source:
                destination.write(line)

my_list = [1, 2, 3, 4, 5]
original_file = "output.txt"
copy_file = "output_copy.txt"

write_list_to_file(my_list, original_file)

# Create copy of the file
copy_file(original_file, copy_file)

print(f"Original file '{original_file}' has been created")
print(f"Copy has been created as '{copy_file}'")

########################################################################################

import shutil

def write_copy_file(list, file_name):
    with open(file_name, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')

# Example usage
my_list = [1, 2, 3, 4, 5]
original_file = "original_file.txt"
copy_file = "copy_file.txt"

# Write list to original file
write_copy_file(my_list, original_file)

# Create copy of the file using shutil
shutil.copy(original_file, copy_file)






















