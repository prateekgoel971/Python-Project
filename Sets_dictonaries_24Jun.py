# --- Sets Method -----

# Pop 
# Remove a random item from the set:

##fruits = {"apple", "banana", "cherry"}
##
##fruits.pop()
##
##print(fruits)
##
### It will return the remove item
##
##fruits = {"apple", "banana", "cherry"}
##
##x = fruits.pop()
##
##print(x)
##
### Remove
### It remove specific item from sets
##
##x ={'table','chair','fan'}
##x.remove('fan')
##print(x)


# Copy

#Copy the fruits set:

##fruits = {"apple", "banana", "cherry"}
##
##x = fruits.copy()
##
##print(x)


# symmetric_difference
# Return a set that contains all items from both sets, except items that are present in both sets:

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.symmetric_difference(y)
##
##print(z)
##
##
##
### symmetric_difference_update
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.symmetric_difference_update(y)
##
##print(x)






# ------------ Dictionaries Data Type ------------


## Dictionaries are used to store data values in key:value pairs.

## A dictionary is a collection which is ordered*, changeable and does not allow duplicates.


##thisdict = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##print(thisdict)
####
####
##thisdict = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##print(thisdict["brand"])


# Duplicates are not allowed

##thisdict = {
##  "name": "Prateek",
##  "Age": "Mustang",
##  "year": 1964,
##  "year": 2020
##}
##print(thisdict)


# Dictinary data type

##thisdict = {
##  "brand": "Ford",
##  "electric": False,
##  "year": 1964,
##  "colors": ["red", "white", "blue"]
##}
##print(thisdict)

# Access Item in Dicinaory 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

x = thisdict.keys()

print(x)
