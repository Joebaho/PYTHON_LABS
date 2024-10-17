'''
PYTHON LAB: list_09.py

Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
expected:
["Mike", "Emma", "Kelly", "Brad"]

'''
# First Solution 
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = [x for x in list1 if x != ""]
print(list2)

#Second Solution

list1 = ["Mike","", "Emma", "Kelly","", "Brad"]
result=list(filter(lambda x: x!="",list1))
print(result)