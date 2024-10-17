'''
PYTHON LAB: list_13.py

Write a program that can perform union and intersection on 2 given list.

'''
# first Solution
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
uni=[]
inter=[]
for i in l1:
   if i in l2:
      inter.append(i)
print(inter)
for i in l1:
    if i not in uni:
       uni.append(i)
for i in l2:
    if i not in uni:
       uni.append(i)
print(uni)

#Second Solution

def list_union(list1, list2):
    """
    Returns the union of two lists.
    """
    return list(set(list1) | set(list2))

def list_intersection(list1, list2):
    """
    Returns the intersection of two lists.
    """
    return list(set(list1) & set(list2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("Union:", list_union(list1, list2))
print("Intersection:", list_intersection(list1, list2))
