# print('resolution of simple equation ')
# print("The equation is on form ax+b=0")

# a= input('What is the value of a:  ')
# b= input('What is the value of b:  ')
# x= -int(b) /int(a)
# print('la premiere solution est x:' , x)
print('resolution of the second degree equation')
print('equation is on form ax2+bx+c=0')
a= input('What is the value of a:  ')
b= input('What is the value of b:  ')
c= input('what is the value of c:  ')

E= int(b) ** 2
M= 4 * int(a) * int(c)
D= 2 * int(a)
A= E - M
com = int(0)
import math
square_root= math.sqrt(int(A))

def equation():
    

    if square_root == com : 
     x0= -(int(b)) / D
     print('La solution unique est x0:' , x0)
    elif square_root > com :
     x1= (int(b) - square_root) / D
     x2= (int(b) + square_root) / D
     print('la premiere solution est x1:' , x1)
     print('la deuxieme solution est x2:' , x2)

    # elif square_root < com :
    #  import cmath
    #  x=int(b) / D 
    #  y=square_root / D
    #  import math
    #  square_root_j= math.sqrt(int(-1))
    #  j=square_root_j
    #  z1= complex(x,y);
    #  z2=complex(x,-y);
    #  z1= x +yj
    #  z2= x-yj
    #  print('la premiere solution est z1:' , z1)
    #  print('la deuxieme solution est z2:' , z2)
    else: 
     print(" error ")
# if __name__ == '__ equation __':
#    equation()