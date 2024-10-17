'''
PYTHON LAB: list_08.py

Iterate both lists simultaneously
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in
original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected-->
10 400
20 300
30 200
40 100

'''
#One Solution 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i, j in zip(list1, list2[::-1]):
    print(i, j)

