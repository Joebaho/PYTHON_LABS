'''
PYTHON LAB: dictionary.py

Write a Python program that prints result with all parameters or methods using in a dictionary.

'''

# first print showing just how list works
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# You can access the items of a dictionary by referring to its key name, inside square brackets 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
X = thisdict["model"]
Y = thisdict.get("year")                  
print(thisdict["brand"])                                             
print (X)                                                                               
print (Y) 
#It is possible to use the dict() constructor to make a dictionary  
thedict = dict(name = "John", age = 36, country = "Norway")
print(thedict)
#The keys() method will return a list of all the keys in the dictionary  
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
Z = thisdict.keys()   
print (Z) 
# Change and add new key to the list     
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
A = car.keys()
print(A) #before the change . dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
print(A) #after the change. dict_keys(['brand', 'model', 'year', 'color'])
# Change and add new value to the list 
B = car.values()
print(B) #before the change. dict_values(['Ford', 'Mustang', 1964])
car["year"] = 2020
print(B) #after the change 
# The items() method will return each item in a dictionary , as tuples in a list
C = car.items()
print(C) #before the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#you can use update a dictionary you must use the update() method .  
car.update({"year": 2020})
print(car)                           #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
#Adding an item to the dictionary is done by using ta new index key and value to it 
car["size"] = "full"
print(car) 
#Removing items: There are several methods to remove items from dictionary 

#-The pop() method removes the item with the specified key name
car.pop("size")
print(car)
#-the popitem() method removes the last inserted item (in version before 3.7, a random item is removed instead): 
car.popitem()
print(car) 
#-The del keyword removes the item with the specified key name: 
del car["year"]
print(car)  
#-The clear () method empties the dictionary 
car.clear()
print(car)
#Loop through a dictionary  you can use the for loop . The return value are the keys of the dictionary, but there are methods to return the values as well
#to print all keys names in the dictionary , one by one use 
for x in thisdict:
  print(x) 
# to print all values in the dictionary , one by one
for x in thisdict:
  print(thisdict[x])
#You can also use the values() method to return values of a dictionary  and the keys() method to return all keys and you can use items() to return all items
for x in thisdict.values():
  print(x)                                                                
for x in thisdict.keys():
  print(x)                                                               
for x, y in thisdict.items():
  print(x, y)
#Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()
print(mydict) 
#Another way to make a copy is to use the built-in function dict().
dict = dict(thisdict)
print(dict) 
# Nested Dictionaries is dictionary that can contain multiples dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#Or, if you want to add three dictionaries into a new dictionary  you must create the different dictionaries and the create the bid one by nesting the three previous in one 
 
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily) 

#To access items from a nested dictionary , you use th name of the dictionaries, starting with the outer dictionary 

print(myfamily["child2"]["name"])                                                                              