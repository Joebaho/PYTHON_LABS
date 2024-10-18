csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
friends_list= (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

# 1st method

# print(csv.split())
# print(csv.split(','))
# print(','.join(csv.split(':')).split(';'))
# print(','.join(','.join(csv.split(';')).split(':')))
# print((','.join(','.join(csv.split(';')).split(':'))).split(','))

#2nd method

print(csv.replace(';',',').replace(':',',').split(','))
