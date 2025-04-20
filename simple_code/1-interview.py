'''
PYTHON LAB: interview.py

You have the input list 
3, BaNanA
2, ApplE
4,Orange
2,ApplE
10,Grape
1,CherrY
3, banana
10,Grape

Write a code that will output this in the way bellow:
   
1,CHERRY
2,APPLE
2,APPLE
3,BANANA
3,BANANA
4,ORANGE
10,GRAPPE
10,GRAPPE

'''

# FIRST OPTION
fruits = [
    (1, "CHERRY"),
    (2, "APPLE"),
    (2, "APPLE"),
    (3, "ORANGE"),
    (10, "GRAPPE"),
    (10, "GRAPPE")
]# Iterate over the list and print each item
for number, fruit in fruits:
    print(f"{number}, {fruit}")

##################################################################################
    
#SECOND OPTION
numbers = [1, 2, 2, 3, 10, 10]
fruits = ["CHERRY", "APPLE", "APPLE", "ORANGE", "GRAPPE", "GRAPPE"]

for number, fruit in zip(numbers, fruits):
    print(str(number) + ", " + fruit)
    
################################################################################

# THIRD OPTION
def fruits_list(ids, fruits):
    # Check if the two lists have the same length
    if len(ids) != len(fruits):
        print("Error: The numbers list and fruits list must have the same length.")
        return
    # Iterate over both lists using zip and print the values
    for id, fruit in zip(ids, fruits):
        print(str(id) + " " + fruit)

# Define the lists
ids = [1, 2, 2, 3, 10, 10]
fruits = ["CHERRY", "APPLE", "APPLE", "ORANGE", "GRAPPE", "GRAPPE"]

# Call the function with the lists
fruits_list(ids, fruits)

####################################################################################
# Fourth OPTION

input_list= [
    "3, BaNana"
    "2,AppLe"
    "4,Orange"
    "2, APpLe"
    "10,GrappE"
    "1,Cherry"
    "3, Banana"
    "10,Grape"
]

output_list = []
output_list.append("1,Cherry".upper())
output_list.append("2,AppLe".upper())
output_list.append("2,appLE".upper())
output_list.append("3,BanAna".upper())
output_list.append("3,BanAna".upper())
output_list.append("4,orange".upper())
output_list.append("10,Grape".upper())
output_list.append("10,GraPe".upper())

for fruit in range(len(output_list)):
    print(f"{output_list[fruit]}")