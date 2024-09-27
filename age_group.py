'''
PYTHON LAB: age_group_categorization.py

Prompt the user to enter their age as an integer.
Based on the input, categorize the person into one of the following life stages:
Infant: 0-1 year
Toddler: 2-3 years
Child: 4-12 years
Teenager: 13-19
Adult: 20-64 years
Senior: 65 years and older
Display the appropriate life stage
If the user enters a negative number or a non realistic number (more than 150) display an "invalid age message'''


# Prompt the user to enter their age as an integer
age = int(input("Please enter your age: "))
C1 ="Infant"
C2 = "Toddler"
C3 = "Child"
C4= "Teenager"
C5 = "Adult"
C6 = "Senior"
# Categorize the person based on the input age
if age < 0 or age > 150:
    print("You entered an Invalid age")
elif age <= 1:
    print(f"{age} year old correspont to {C1.upper()} categorisation")
elif age <= 3:
    print(f"{age} years old correspont to {C2.upper()} categorisation")
elif age <= 12:
    print(f"{age} years old correspont to {C3.upper()} categorisation")
elif age <= 19:
    print(f"{age} years old correspont to {C4.upper()} categorisation")
elif age <= 64:
    print(f"{age} years old correspont to {C5.upper()} categorisation")
else:
    print(f"{age} years old correspont to {C6.upper()} categorisation")
