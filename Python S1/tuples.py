'''
Tuples are defined within ()
Tuples are also ordered sequence but immutable (means you can't change its content).
Tuples are used to write-protect data.
Tuples are faster than lists as its cannot change dynamically.
You can't find elements in a tuple.
You can use 'in' operator to check if an element exist in tuple.
'''
#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)


#Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#You cannot add items to a tuple:
thistuple = ("apple", "banana", "cherry")
#thistuple[3] = "orange" # This will raise an error

#One item tuple, remember the commma:
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

'''
Method = Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''
