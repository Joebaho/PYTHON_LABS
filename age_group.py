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
