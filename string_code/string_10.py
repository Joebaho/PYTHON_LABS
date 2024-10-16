'''
PYTHON LAB: string_08.py

Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and
last characters.
s1 = "America"
s2 = "Japan"
Expected output-->AJrpan

'''
#first Solution 
def get_new_string(s1, s2):
    # Get the first character of each string
    first_char_s1 = s1[0]
    first_char_s2 = s2[0]

    # Get the middle character of each string
    middle_char_s1 = s1[len(s1) // 2]
    middle_char_s2 = s2[len(s2) // 2]

    # Get the last character of each string
    last_char_s1 = s1[-1]
    last_char_s2 = s2[-1]

    # Combine the characters into a new string
    new_string = first_char_s1 + middle_char_s1 + last_char_s1 + first_char_s2 + middle_char_s2 + last_char_s2

    return new_string

# Example usage
s1 = "America"
s2 = "Japan"
result = get_new_string(s1, s2)
print(result)  # Output: AJrpan

# Second Solution
def unite(s1,s2):
    l1=len(s1)//2
    a=s1[0]
    b=s1[l1]
    c=s1[-1]
    l2=len(s2)//2
    x=s2[0]
    y=s2[l2]
    z=s2[-1]
    result="".join([a,x,b,y,c,z])
    return result