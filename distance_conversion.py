'''
PYTHON LAB: distance_conversion.py

Write a program that will ask for a user to enter his/her distance run in Kilometer and convert it to mile (mi), feet(ft), Inches(inc) end meter(m).
Display on the screen: The distance you made today is dist in km, and the equivalent mile is weight mi.  Thank you!  only display three digit decimal e.g:10.234'''

# This Program will take a distance in km you did and convert it in miles the feet and inches.
print('Code to convert km to miles, to feet, to meter and then to inches.')
print("Enter information needed")
name= input('What is your name:  ')
dist_km= input('What is the distance you did in km:  ')
#Declaration of variables
a=1.609
b=3280.84
c=39370.1
d= 1000
top_level = "#" * 65
#Conversion
dist_mi= float(dist_km) / a
dist_ft= float(dist_km) * b
dist_in= float(dist_km) * c
dist_me= float(dist_km) * d
#Result
print(top_level + "\n")
print(f'Hello {name.title()},' "\n" )
print(f'The distance you made today is {dist_km} km is equivalent to {dist_mi:0,.2f} miles.')
print(f'Then {dist_km} km is equivalent to {dist_ft:0,.2f} feet.')
print(f'Also, {dist_km} km is equivalent to {dist_me:0,.2f} meter.')
print(f'And finally {dist_km} km is equivalent to {dist_in:0,.2f} inches.' "\n")
print(f'Thank you for being a great runner!' "\n" )
print(top_level + "\n")
