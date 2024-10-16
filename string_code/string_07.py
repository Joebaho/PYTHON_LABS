'''
PYTHON LAB: string_07.py

Find the index position of a particular character in another string.

'''
#First solution
a=input("enter the text: ")
b=input("enter the character: ")
print(a.index(b))

# Second Solution
def find_index(string, char):
    """
    Find the index position of a particular character in another string.
    
    Args:
        string (str): The string to search.
        char (str): The character to find the index of.
        
    Returns:
        int: The index position of the character in the string, or -1 if not found.
    """
    for i, c in enumerate(string):
        if c == char:
            return i
    return -1

# Example usage
string = "Hello, World!"
char = "o"
index = find_index(string, char)
print(f"The index position of '{char}' in '{string}' is {index}")