'''
PYTHON LAB: string_04.py

Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.

'''
name="james"

a=name[0]
print(a)

c=name[-1]
print(c)

l=len(name)
x=int(l//2)
b=name[x]
print(b)
#or
print(name[int(len(name)/2)])
"".join([a,b,c])