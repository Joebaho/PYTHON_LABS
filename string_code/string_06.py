'''
PYTHON LAB: string_06.py

Count the frequency of a particular character in a provided string. Eg 'hello how are you'
is the string, the frequency of h in this string is 2.

'''
# First Solution 
a=input("enter the text: ")
b=input("enter the character: ")
count=0
for i in a:
    if i in b:
       count=count+1
print("frequency of searched character is ",count,"times")

# Second Solution 
def count_char_frequency(input_string, char):
    """
    Counts the frequency of a particular character in a given string.
    
    Args:
        input_string (str): The input string to search.
        char (str): The character to count the frequency of.
        
    Returns:
        int: The frequency of the character in the input string.
    """
    count = 0
    for c in input_string:
        if c == char:
            count += 1
    return count

# Example usage
input_string = "hello how are you"
char_to_find = "h"
frequency = count_char_frequency(input_string, char_to_find)
print(f"The frequency of '{char_to_find}' in '{input_string}' is {frequency}")