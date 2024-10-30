import shutil

def write_list_to_file(lst, file_name):
    with open(file_name, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

# Example usage
my_list = [1, 2, 3, 4, 5]
original_file = "output.txt"
copy_file_name = "output_copy.txt"

# Write list to original file
write_list_to_file(my_list, original_file)

# Create copy of the file using shutil
shutil.copy(original_file, copy_file_name)

print(f"Original file '{original_file}' has been created")
print(f"Copy has been created as '{copy_file_name}'")