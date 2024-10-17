'''
PYTHON LAB: list_07.py

Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected result:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

'''
# 1st Aresult 
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = []
for item1 in list1:
    for item2 in list2:
        result.append(item1 + item2)

print(result)

# Second Solution
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        print(i+j)
