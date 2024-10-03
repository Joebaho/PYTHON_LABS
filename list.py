'''
PYTHON LAB: list.py

Write a Python program that prints result with all parameters or methods using in a list.

'''
friends  = ['John' , 'Michael' , 'Terry' , 'Eric' ,  'Graham' ,  'Joe'] 
# first print and check of value or position
print(friends)                       # list all                                                                                                          
print(friends[1])                    # list value at position 1                                                                                                     
print(friends[0],friends[3])         # List value of John space Eric                                                                                  
print(friends[-1])                   #list the last Joe                                                                                   
print(friends[1:4])                  #List from Michael to Eric                                                                                   
print(len(friends))                  # give how many value is contains in the list                                                                                  
print(friends.index('Eric'))         #give the position of Eric                                                                                
print(friends.count('Joe'))          # count how many time we do have Joe in the list 

#We can also sort lis either in order or disorder. Here are hw to do it
print(friends)
friends.sort()                  # Place the list in alphabetical order A-Z
print(friends)
friends.sort(reverse=True)      # place the list in disorder Z-A 
print(friends)
friends.reverse()               # return the list as it was initialy 
print(friends)  
# we can find max or min of a list with 
cars =[911,130,328,535,740,308] 
print(min(cars))                  # give the minnimum on the list 
print(max(cars))                  # give the maximum on the list
print(sum(cars))                  # sumarize all the value of the list 
# We can also while working with list add , remove, change or delete value in the list. Here are some hint to do that. 
friends.append('Max') 
print(friends)                    #['John' , 'Michael' , 'Terry' , 'Eric' ,  'Graham' ,  'Joe' , 'Max']    (Add Max at the end of the list)
  
friends.insert(2,'Max')       
print(friends)                    #['John' , 'Michael' ,  'Max', 'Terry' , 'Eric' ,  'Graham' ,  'Joe' ]  (Insert Max at the second position)
  
friends[2]='Max'   
print(friends)                   #['John' , 'Michael' ,  'Max',   'Eric' ,  'Graham' ,  'Joe' ]    ( Remove Terry and replace by Max )  

friends.extend(cars)
print(friends)                   #['John' , 'Michael' , 'Terry' , 'Eric' ,  'Graham' ,  'Joe' . 911,130,328,535,740,308] join both lists to form one

friends.remove('Graham')       
print(friends)                   #['John' , 'Michael' , 'Terry' , 'Eric' ,   'Joe']  
                
friends.pop()       
print(friends)                   #['John' , 'Michael' , 'Terry' , 'Eric' ,  'Graham' ]  remove last item and keep in memory

del friends[3]      
print(friends)                   #   [ 'John' , 'Michael' , 'Terry' ,  'Graham' ,  'Joe']  Deleted 3 position Eric 

#del friends     
#print(friends)                   #Error: unknow error  List completely delete

#Create a new list or copy use command
friends  = ['John' , 'Michael' , 'Terry' , 'Eric' ,  'Graham' ,  'Joe'] 
del friends[2]
new_friends= list(friends)     
print(friends)                     #['John' , 'Michael' , 'Eric' ,  'Graham' ,  'Joe']                                                    
print(new_friends)                 #['John' , 'Michael' , 'Eric' ,  'Graham' ,  'Joe'] 
#When you have to create an empty list you can do this 
empty_list1 = []
empty_list2 = list( )
empty_list3 = list(( " " , " " , " " )) 
print(empty_list1)
print(empty_list2)
print(empty_list3)
empty_list3.append('Max')
print(empty_list3)
#You can loop through the list items by using a for loop .To print all items in the lit , one by one 
thislist = ["apple", "banana", "cherry"]                                                        
for x in thislist:                                            
    print(x)
#You can also loop through the list items by referring to their index number. Use the range() and len() functions to create a suitable iterable. 
thislist = ["apple", "banana", "cherry"]                                                        
for i in range(len(thislist)):                                                                                         
    print(thislist[i])  
   