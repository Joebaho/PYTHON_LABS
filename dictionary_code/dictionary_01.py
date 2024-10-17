'''
PYTHON LAB: dictionary_01.py

Convert two lists into a dictionary
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1
is the key and item from list2 is the value
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

'''
#1 Soluotion

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict=zip(keys,values)
result=dict(my_dict)
print(result)

#2 Solution
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary)