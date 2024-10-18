import cmath

def equation():
    print('equation is on form ax^2+bx+c=0')
    # Enter the value of each input
    a = float(input('What is the value of a: '))
    b = float(input('What is the value of b: '))
    c = float(input('What is the value of c: '))

    # Calculate the discriminant
    discriminant = (b**2) - (4*a*c)
    delta = cmath.sqrt(discriminant)
    # Check if the discriminant is positive, negative, or zero
    if discriminant == 0:
        # One real root (repeated)
        x0 = -b / (2*a)
        print('The unique solution is x0:', x0)
        return x0
    elif discriminant > 0 :
        # Two real roots
        x1 = (-b + delta) / (2*a)
        x2 = (-b - delta) / (2*a)
        print('The first solution is x1:', x1)
        print('The second solution is x2:', x2)
        return x1, x2
    else:
        # Two complex roots
        j= -1
        z1 = (-b + (delta*j)) / (2*a)
        z2 = (-b - (delta*j)) / (2*a)
        print('The first solution is z1:', z1)
        print('The second solution is z2:', z2)
        return z1, z2

if __name__ == '__main__':
    equation()