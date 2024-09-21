import math

def resolve_equation_second_degree(a, b, c):
    if a == 0:
        x = -c / b
        return f"The solution is x = {x}"
        #return resolve_equation_first_degree(b,c)
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"There are two real solutions : x1 = {x1} et x2 = {x2}"
    elif delta == 0:
        x0 = -b / (2*a)
        return f"There is a double solution : x0 = {x0}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-delta) / (2*a)
        return f"There are two complex solutions : z1 = {real_part} + {imaginary_part}i et z2 = {real_part} - {imaginary_part}i"

# Test du programme
print("The resolution of equation ax² + bx + c = 0")
a = float(input("Enter the value a : "))
b = float(input("Enter the value b : "))
c = float(input("Enter the value c : "))

result = resolve_equation_second_degree(a, b, c)
print(result)