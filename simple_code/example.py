print("hello wolrd")
print("message in the sentence")
a=10
b=30
print("The sum:",(a+b))

msg1='welcome to Python 101'
msg2='Hope you will enjoy'
print(msg1, msg2)
print(msg1.upper(),msg2.lower())
print(msg1.capitalize(),msg2.capitalize())

msg='welcome to Python 101:Strings'
msg1=msg[18]+' '+msg[-5]+msg[25:28]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title())
print(msg1[::-1].title())
print(msg1.casefold())
print(msg.count('o'))

msg="""Dear Terry
You must be very tired as I can see
please let me know when I can stop by """
print(msg)
print(msg.find('y'))
print(msg.replace('Terry','Joseph'))

print("Hello, World!")
name = input("What's your name? ")
print("Hello {}!\nWelcome to Dataquest!".format(name))


