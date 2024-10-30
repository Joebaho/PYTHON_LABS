'''
PYTHON LAB: copy_story.py

Write a function called copy, which takes in a file name and anew file name and copies the contents of first file into the second file. 
(Note: we've provided you with the first chapter of Alice's adventures in Wonderland to give you some
sample text to work with. This is also the text usedin the tests.)

copy('story.txt', 'story_copy.txt') # None
# expect the contents of 'story.txt' and 'story_copy.txt' to be the same
'''
def copy(file_name, new_file_name):
    try:
        with open(file_name, 'r') as file, open(new_file_name, 'w') as new_file:
            content = file.read()
            new_file.write(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
copy('sample.txt', 'sample_copy.txt')

############################################################################################
import os
def copy(file_name, new_file_name):
    with open(file_name, 'r') as file, open(new_file_name, 'w') as new_file:
            content = file.read()
            new_file.write(content)
# Example usage
copy('sample.txt', 'sample_copy.txt')
# check if file exist and check the size too 
# size=os.stat("sample.txt").st_size
# if os.path.exists("sample.txt") and size != 0:
#    if os.path.exists("sample_copy.txt") and size != 0:
#       print("Both files exist and are not empty")
#    else:
#       print("Both files do not exist")
# else:
#    print("error message")
# # Delete an existing file
# os.remove("sample.txt")
# os.remove("sample_copy.txt")

####################################################################################################
import shutil

def copy(src_file, copy_file):
    # Open source file in append mode and write additional content
    with open(src_file, "a") as f1:
        f1.write("Alice: Would you tell me, please, which way I ought to go from here?")
        f1.write("The Cheshire Cat: That depends a good deal on where you want to get to.")
        f1.write("Alice: I don't much care where!")
        f1.write("The Cheshire Cat:Then it doesn't matter which way you go.")
        f1.write("Alice: I shall take you up on the highest branch of the tallest tree.")
        f1.write("The Cheshire Cat:Oh, you're sure to do that, if only you walk long enough.")


    # Open source file in read mode and display its content
    with open(src_file, "r") as f1:
        print(f1.read())

    # Copy the contents of source_file to destination_file
    shutil.copy(src_file, copy_file)

# Example usage
copy("sample1.txt", "sample2.txt")
