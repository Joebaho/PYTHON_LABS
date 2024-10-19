'''
PYTHON LAB:body_weight_calculator.py

Write a program that will ask for a user to enter his/her body weight in pounds (lbs) and convert it to kilogram (kg).
Display on the screen: your body weight is weight in lbs, and the equivalent kgs is weight kg.  

Thank you!  only display three digit decimal e.g:10.234'''

# Program to convert weight from pouns to Kilogram
print('Welcome to the weight program convertor.Here you can convert your weight from pounds to kilogram or vice versa. \n')

def weight_calculator(name, unit, weight):
   v= 0.4535
   weight_lbs= float(weight) / v
   weight_kg= float(weight) * v

   return  weight_lbs, weight_kg 
name = input('Enter your name:\t ').capitalize()
unit= input('Enter the unit value lbs or kg ?:\t')
weight= input('Enter your weight:\t' ) 
result = weight_calculator('name', 'unit', float(weight))    
#Conditional Statement
x1="lbs"
x2="kg"
if unit==x1:
   info=f"Hello dear {name}, " "\n""\n"
   weight_kg_result=f"Your body weight is {weight} in lbs, and the equivalent in kgs is {result[1]:0,.3f} kg." "\n""\n" "Thank you!"
   print(info, weight_kg_result)

elif unit==x2:
   info=f"Hello dear {name}, " "\n""\n"
   weight_lbs_result=f"Your body weight is {weight} in kg, and the equivalent in lbs is {result[0]:0,.3f} lbs." "\n""\n" "Thank you!"
   print(info, weight_lbs_result)
else:
    print("Invalid unit entered. Please enter either 'lbs' or 'kg'.")