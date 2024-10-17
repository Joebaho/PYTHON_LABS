'''
PYTHON LAB: dictionary_08.py

Get the key of a minimum value from the following dictionary
sample_dict = { 'Physics': 82, 'Math': 65, 'history': 75 }
Expected:
math

'''
sample_dict = { 'Physics': 82, 'Math': 65, 'history': 75 }

# Get the key of the minimum value
min_key = min(sample_dict, key=sample_dict.get)

print(min_key)

####################################################################

sample_dict = {
'Physics': 82,
'Math': 65,
'history': 75
}
min(sample_dict,key=sample_dict.get)