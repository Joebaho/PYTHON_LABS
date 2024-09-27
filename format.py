'''
PYTHON LAB:  Format Method
This Code we will be using variables and string format to form and use the two format metod to print message'''

#LAB1 : Declaration of Variables
first_name = "Joseph"
age = 40
favorite_color = "red"
sentence = "Hello, my name is {}. I am {} years old, and faorite color is {}. " .format(first_name, age, favorite_color)

# Print the sentence
print(sentence)


#LAB2: Declaration of variables
city = "Hollister"
temperature = 62
weather = "temperature"
sentence = f"The current temperature in {city} is {temperature:.0f}°C"

# Print the banner
print(sentence)
print(f"The current {weather} in {city}is {temperature:.01}°C")
