# Program for summarization of two number

#enter value of number 
number1= float(input('What is the value of number1:  '))
number2= int(input('What is the value of number2:  '))

#perform the math
addition= float(number1) + float(number2)
summarization= int(number1) + int(number2)

#message 
sum1 = f"The  float sum of {number1} and {number2} is : {addition}  "
sum2 = "The integer sum of {} and {} is : {} " .format(number1, number2, summarization)

#Provide result
print(sum1)
print(sum2) 

