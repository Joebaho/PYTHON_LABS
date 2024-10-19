'''
PYTHON LAB:distance_convertor.py

Write a program that will ask for a user to enter his/her distance run in (km) and convert it to miles (mi).
Display on the screen: your distance is weight in km, and the equivalent miles is.  
Thank you!  only display three digit decimal e.g:10.234'''
def distance_convertor():
    name= input('Enter your name:  ')
    a=0.62137
    b=3280.84
    c=39370.1
    dist_km= float(input('Enter the distance you ran in km:  '))
    dist_mi= float(dist_km) * a
    dist_ft= float(dist_mi) * b
    dist_in= float(dist_km) * c
    print(f'\nHello {name.title()},\n\nYou ran {dist_km} km is equivalent to {dist_mi:.3f} miles.')
    print(f'Your {dist_km} km is equivalent to {dist_ft:.3f} feet.')
    print(f'And the {dist_km} km is equivalent to {dist_in:.3f} inches.')
    print('\nThank you!')

distance_convertor()

