'''
PYTHON LAB: set_07.py

Check if two sets have any elements in common. If yes, display the common
elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
expected:
Two sets have items in common {10}

'''
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

common_elements = set1.intersection(set2)

if common_elements:
    print(f"Two sets have items in common {common_elements}")
else:
    print("Two sets have no items in common")

######################################################################################

set1 = {10 ,20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
   print("above two set dont have any common element")
else:
   print(set1.intersection(set2))  
    
  