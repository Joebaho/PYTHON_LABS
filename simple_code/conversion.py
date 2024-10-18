print('Code to convert km to miles')
print("Enter information needed")
name= input('What is your name:  ')
a=1.609
b=5280
c=12
dist_km= input('What is the distance you did:  ' )
dist_mi= float(dist_km) / a
dist_ft= float(dist_mi) * b
dist_in= float(dist_km) * c
print(f'Hi {name.title()}! The distance you made is {dist_km} km is equivalent to {dist_mi} miles.')
print(f'Then {dist_km} km is equivalent to {(dist_ft)} feet.')
print(f'And finally {dist_km} km is equivalent to {(dist_in)} inches.')