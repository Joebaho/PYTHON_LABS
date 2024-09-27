'''
PYTHON LAB:hackaton.py

Write a program that will user the string method to display the both given message in differents way.
Display on the screen: mDisplay the message with the required method '''

#given messages
msg1 = "welcome to aws python 101 class: strings"
msg2 = "The instructor here is Claudio"

# 1. Capitalize all first character of each word of msg1
capitalized_msg1 = msg1.title()
print(capitalized_msg1)

# 2. Reverse msg2
reversed_msg2 = msg2[::-1]
print(reversed_msg2)

# 3. Write msg1 in lower case
lowercase_msg1 = msg1.lower()
print(lowercase_msg1)

# 4. Write msg2 in upper case
uppercase_msg2 = msg2.upper()
print(uppercase_msg2)

# 5. Find how many "e" characters were used in msg2
e_count = msg2.count("e")
print(e_count)

# 6. Replace "python" by "java" in msg1
rep_msg1 = msg1.replace("python", "java")
print(rep_msg1)

# 7. Write a new message "python is great" using msg1 characters
new_msg1 =msg1[15:21]+' '+msg1[-4]+msg1[-1]+' '+msg1[-2]+msg1[-5]+msg1[1]+msg1[11]+msg1[-6]
print(new_msg1)

# 8. Write new message "Java is well done" using msg1 characters
new_msg2=rep_msg1[15:19]+' '+rep_msg1[-4]+rep_msg1[-1]+' '+rep_msg1[0:3]+rep_msg1[2]+' '+ 'd'+rep_msg1[4]+rep_msg1[-3]+rep_msg1[1]
#rep_msg1 = "welcome to aws java 101 class: strings"
print(new_msg2)


