'''
PYTHON LAB: string_08.py

Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Ault"
s2 = "Kelly"
expected-->AuKellylt

'''
#first Solution
def append_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

# Example usage
s1 = "Ault"
s2 = "Kelly"
result = append_middle(s1, s2)
print(result)  # Output: AuKellylt

# Second Solution
def append_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

# Third Solution
s1="Ault"
s2="Kelly"
l=len(s1)
mid=l//2
f=s1[:mid]
s=s1[mid:]
s3=f+s2+s
print(s3)