# -- Tuples Data type ----

# --Tuples are used to store multiple items in a single variable.
# --Tuple items are ordered, unchangeable, and allow duplicate values.
# --Tuples are written with round brackets.


# Example

##thistuple = ("apple", "banana", "cherry")
##print(thistuple)
##
### Allow Duplicate
##
##var = ("a","b","c","a","c")
##print(var)


# Contain Any data Type

##tuple1 = ("abc", 34, True, 40, "male")
##print(tuple1)

# Can't be modify

##team = ("Rohit","Ashwin","Dhoni")
##team[1]= "Virat"
##print(team)

# Cannot Append/add data

##tech = ("PHP","CSS","JAVA")
##tech.append("Python")
##print(tech)

# Usage of For loop

##thistuple = ("apple", "banana", "cherry")
##for i in range(len(thistuple)):
##  print(thistuple[i])


### Joining of two tuples
##
##tuple1 = ("a", "b" , "c")
##tuple2 = (1, 2, 3)
##
##tuple3 = tuple1 + tuple2
##print(tuple1 + tuple2)

# count()	Returns the number of times a specified value occurs in a tuple

##numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5,2,5)
##
##x = numbers.count(5)
##
##print(x)

# Index() Search for the first occurrence of the value

##thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
##
##x = thistuple.index(8)
##
##print(x)
