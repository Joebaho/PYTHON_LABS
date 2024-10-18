'''
PYTHON LAB: equation_1_degree.py

Write a program that will solve the equation of first degree ax + b = 0
Display on the screen:  the different result existing or not'''

#Solution
def resolve_equation_first_degree(a, b):
    if a == 0:
        if b == 0:
            return "Infinity of solutions"
        else:
            return "The is no solution"
    else:
        x = -b / a
        return f"The is only one solution x = {x}"

# Test du programme
print("The resolution of equation ax + b = 0")
a = float(input("Enter the value a : "))
b = float(input("Enter the value b : "))

result = resolve_equation_first_degree(a, b)
print(result)