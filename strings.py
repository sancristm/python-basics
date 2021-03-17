#string operations in python includes
string0="I am "
string1="mamboleo sancrist "
string2=" an upcomming programmer "
string3="mamboleo"

# string concatenation
print(string0+string1+string2) # returns I am mamboleo sancrist an upcomming programmer



#string repitition
print(string1*3) # returns "mamboleo sancrist mamboleo sancrist mamboleo sancrist'


#string slicing
print(string3[2:6]) #returns "mbol" after slicing operation done
print(string3[5:-1]) #retuns "le" after slicing of index -1 which is "o"

# string indexing i.e refrenceng the value by it's index number
print(string3[4])   #returns "o"

#string methods
print (string1.upper())  # prints the entire string to upper case
#string1.max()
#string3.main()
print(string3.split(' , ')) #splits the sting into list of characters
print(string3.find("mam")) #finds the string characters index


