'''
PYTHON LAB: string_03.py

Write a program to remove characters from a string starting from zero up to n and return
a new string.
For example:
remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a
string. remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters
from a string. Note: n must be less than the length of the string.

'''
#Solution 1
def remove_chars(word, n):
    x=len(word)
    p=list(word)
    for i in p:
        if n<=x:
         z=word[n:]
    print(z)
remove_chars("pynative",2)