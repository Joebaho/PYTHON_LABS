'''
PYTHON LAB: dictionary_09.py

Change value of a key in a nested dictionary
Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample_dict = { 'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3':
{'name': 'Brad', 'salary': 500} }
expected output:
{ 'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad',
'salary': 8500} }

'''
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

# Change Brad's salary to 8500
sample_dict['emp3']['salary'] = 8500

print(sample_dict)