# Intersection Method

# Return a set that contains the items that exist in both set x, and set y:

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.intersection(y)
##
##print(z)
##
##
##x = {"a", "b", "c"}
##y = {"c", "d", "e"}
##z = {"f", "g", "c"}
##
##result = x.intersection(y, z)
##
##print(result)


# Instesection_Differences

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.intersection_update(y)
##
##print(x)

# Difference Update

# Remove the items that exist in both sets:

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.difference_update(y)
##
##print(x)
##
##
### Difference -- it return a new set 
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = y.difference(x)
##
##print(z)


# isdisjoint

# Return True if no items in set x is present in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook","apple"}

z = x.isdisjoint(y)

print(z)



# issubset

# Return True if all items in set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "b", "a"}

z = x.issubset(y)

print(z)

# issuperset

# Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "y"}

z = x.issuperset(y) 

print(z)
