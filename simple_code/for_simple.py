# You are having a party and want to invite your friends. 
#you want the print out invitation for each friend usung for loops.
# the names are in two lists, "names" and "names1"
#You also need to add two extra names to the list using an input box, when you run the code 
#printout one invitation toreach friend per line
#names should be properly capitalize 
#Hint : yu may need two for loops to solve this exercise

names=['joe baho', 'Peter bae', 'Martin drill', 'Claude Tounw']
names1=['Depes mba', 'Moses azuk', 'Jose Ruelas', 'Elie tama']
msg = 'You are invited to the party on saturday.'
#names.extend(names1)
#names += names1
names += names1
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    #msg1 = f'{name.title()}! {msg}'
    msg1 = name.title() + '! ' + msg
    print(msg1)

    
        
