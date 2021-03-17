#list initialization
mylist = ["apple", "banana", "cherry"]
print(mylist) # Returns ['apple', 'banana', 'cherry']

#list allows duplicate data
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # returns ["apple", "banana", "cherry", "apple", "cherry"]

print(len(thislist))    # retuns list lenth i.e  for this  case it retuns 3 for the three items in the list

print(type(mylist)) # retruns the datatype present in the list

 #using the list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#accessing the list by positive indexing
print(thislist[1]) #returns "banana"

#accessing the list by negative indexing
print(thislist[-1])  #returns "cherry"

#range of indexes
print(thislist[1:2]) #returns banana cherry 

#adding items on the list
thislist.append("orange") #adds orange on the list