# friends  = ['John' , 'Michael' , 'Terry' , 'Eric' ,  'Graham' ,  'Joe'] 
# cars =[911,130,328,535,740,308]
# friends.remove('Eric')
# new_friends=friends.copy()
# print(new_friends) 
         
# name= input('name: ')
# period= input('period: ')
# score= input('score: ')
# msg=f'The team {name} in the period {period} scored {score} goal during the end of match'
# print('The team ' + name + ' in the period ' + period + ' scored ' + score +' goal ')
# print(msg)

#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# #Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily["child2"]["name"])

#function 
# def my_function(fname, lname):
#   print(fname + " " + lname)
#   print(f'Your full name is {fname} {lname}')

# my_function("Emil", "Refsnes") 
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")   
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)
# squares = []

# for x in range(1, 11):
#     squares.append(x**2)
# print(squares)

names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invited to the party on saturday.'
names.extend(names1)
#names = names + names1
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    msg1 = f'{name.title()}! {msg}'
    print(msg1)


