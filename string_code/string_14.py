'''
PYTHON LAB: string_14.py

String characters balance Test
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the
characters in the s1 are present in s2. The character’s position doesn’t matter.

'''

# Frist Solution
def is_balanced(s1, s2):
    # Convert strings to sets to remove duplicates
    s1_set = set(s1)
    s2_set = set(s2)

    # Check if all characters in s1 are present in s2
    return s1_set.issubset(s2_set)

# Example usage
string1 = "abc"
string2 = "abcd"
if is_balanced(string1, string2):
    print(f"The strings '{string1}' and '{string2}' are balanced.")
else:
    print(f"The strings '{string1}' and '{string2}' are not balanced.")

# Second Solution
s1 = "Yn"
s2 = "PYnative"
count=0
for i in s1:
    if i in s2:
       count+=1
if len(s1)==count:
    print("s1 and s2 are balanced")
else:
    print("s1 and s2 are not balanced") 