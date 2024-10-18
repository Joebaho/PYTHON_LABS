print("Welcome to Python") 
print('I will like it sure!')

failed_subjects=10
name="Joseph"
print ('Dear friend our number is ' + str(failed_subjects) + ' cages')
print(name + ' will be the owner of the ' + str(failed_subjects) + ' cages')
failed_subjects="15"
name='Depes'
print('if we are not sure of ' + name + ' to take care of ' + failed_subjects + ' cages')

a="it's"
b='it\'s'
print(a + ' raining out there')
print("I think " + b + " raining out")

print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
c1 = int(float("3.4"))   # c1 will be...
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,c1,d,e,f,g,h,i,j])
print("it\'s raining out there")
print("it's raining now I can't go out")
print('it\'s the person I can\'t talk to')

a=10
b=3
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

Item_Name='wood'
price=100
inventory_stock=325
presence= True
msg=Item_Name, price,inventory_stock, presence
print(msg)
print(Item_Name, price,inventory_stock, presence)

msg='Welcome to Python 101:Strings'
msg1=msg[-9]+' '+msg[:7]+' '+msg[-5]+msg[-4]+msg[-3]+msg[-2]+' '+msg[8:10]+' '+msg[8]+msg[12]+msg[2]+msg[1]+msg[-5]
msg2=msg[10:17]+' '+msg[-4]+msg[-1]+' '+msg[0:3]+msg[2]+' d'+msg[4]+msg[-3]+msg[1]
msg3=msg[-6]+msg[14]+msg[-4]+msg[-1]+' '+msg[5:7]+msg[-1]+msg[-1]+'a'+msg[-2]+msg[1]+' '+msg[-4]+msg[-1]+' '+msg[22:28]
print(msg1.title())
print(msg1[::-1])
print(msg2)
print(msg2.upper())
print(msg3.capitalize())
print(msg1.lower())
print(msg2.find('e'))
print(msg.find('Strings'))
print(msg.replace('Python' , 'Java'))  
print(msg2.replace('Python' , 'Java'))  
print('Python' not in msg)  

name='TERRY'
color = 'RED'
msg =name + ' loves the color ' + color.lower() + '!'
msg1 = '[' + name + '] loves the color ' + color.lower() + '!'
msg2 = f'{name.capitalize()} loves the color {color.lower()}!'
print(msg)
print(msg1)
print(msg2)

failed_subjects=10
name="Joseph"
print ('Dear friend our number is ' + str(failed_subjects) + ' cages')
print(name + ' will be the owner of the ' + str(failed_subjects) + ' cages')
failed_subjects="15"
name='Depes'
print('if we are not sure of ' + name + ' to take care of ' + failed_subjects + ' cages')
msg= f'if we are not sure of  {name.upper()}  to take care of ' + failed_subjects + ' cages'
print(msg)

name1='TERRY'
name2='joe'
color = 'RED'
msg = name1 + ' loves the color ' + color+ '!'
msg1 = f'{name2} loves the color {color}!'
msg2= f'{name1} loves the color {color.lower()}'
msg3= f'{name2.upper()} loves the color {color.upper()}'
print(msg)
print(msg1)
print(msg2)
print(msg3)


