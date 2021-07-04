# ------ SETS Data Type -------

# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.
# Set items are unchangeable, and do not allow duplicate values.
# Sets are written with curly brackets.

# Example: 

##thisset = {"apple", "banana", "cherry"}
##print(thisset)
##
### Duplicates are not allowed
##
##fruits = {"apple", "banana", "cherry", "apple"}
##
##print(fruits)


# Length of Sets

##thisset = {"apple", "banana", "cherry","KIWI"}
##
##print(len(thisset))
##
##
### Sets can be of any data type
##
##set1 = {"apple", "banana", "cherry"}
##set2 = {1, 5, 7, 9, 3}
##set3 = {1,0,True, False, False}
##
##
##print(set3)


# Access Item

##You cannot access sets by using index 


##str = {'Java','Python','C++'}
##
##for x in str:
##    print(x)



# Methods in Set Data Type

# Add
# you cannot change/modfiy in  sets but you can add new item in sets


##Name = {'Prateek','vikram','Mounika'}
##Name.add('Mohan')
##print(Name)

# Add 2 Sets / update Methods 
# if you want to add another set into current set

####thisset = {"apple", "banana", "cherry"}
####tropical = {1,2,True}
####
####thisset.update(tropical)
####
####print(thisset)


# Remove/Discard Method
# to remove item from given sets

##thisset = {"apple", "banana", "cherry"}
##
##thisset.remove("banana")
##
##print(thisset)


thisset = {"abc", "xyz", "mno"}

thisset.discard("KIWI")

print(thisset)
##
##
###Clear
##
##thisset = {"apple", "banana", "cherry"}
##
##thisset.clear()
##
##print(thisset)
