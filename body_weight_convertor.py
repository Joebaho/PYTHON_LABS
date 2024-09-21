# Program to convert weight from pouns to Kilogram

print('Welcome to the weight program convertor.Here you can convert your weight from pounds to kilogram or vice versa')
print("Enter information needed")
# input value
name= input('What is your name:  ')
age= input('What is your age:  ')
unit= input('What is your unit value lbs or kg ?: ')
weight= input('What is your weight: ' )
#calcul
x1="lbs"
x2="kg"
v= 0.4535
weight_lbs= float(weight) / v
weight_kg= float(weight) * v
#Conditional Statement
if unit==x1:
   info=f"Hello dear {name}, customer of {age} years old." "\n"
   weight_kg_result=f"Your body weight is {weight} in lbs, and the equivalent in kgs is {weight_kg:0,.3f} kg." "\n" "Thank you!"
   print(info, weight_kg_result)

elif unit==x2:
   info=f"Hello dear {name}, customer of {age} years old." "\n"
   weight_lbs_result=f"Your body weight is {weight} in kg, and the equivalent in lbs is {weight_lbs:0,.3f} lbs." "\n" "Thank you!"
   print(info, weight_lbs_result)
else:
    print("Invalid unit entered. Please enter either 'lbs' or 'kg'.")


