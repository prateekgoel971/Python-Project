# ----- Statments ----

# -- If else Statments in python

##Python supports the usual logical conditions from mathematics:

##Equals: a == b
##Not Equals: a != b
##Less than: a < b
##Less than or equal to: a <= b
##Greater than: a > b
##Greater than or equal to: a >= b

##a = 33
##b = 200
##if b > a:
##  print("b is greater than a")

##Indentation
##Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.

##a = 33
##b = 200
##if b < a:
##    
##    print("b is greater than a")



# --- If & elif Statmets -- If prvious condition is not true 



##a = 33
##b = 33
##if b > a:
##  print("b is greater than a")
##elif a == b:
##  print("a and b are equal")
##
##
### --- If & elif & else --- If none of preceding condition is true

##a = 200
##b = 33
##if b > a:
##  print("b is greater than a")
##elif a == b:
##  print("a and b are equal")
##else:
##  print("a is greater than b")
##
##
##
### Short Hand If -- if we have only 1 statment to execute
##
##a = 200
##b = 33
##
##if a > b: print("a is greater than b")
####
####
#### Short hand if & else
#### This technique is known as Ternary Operators, or Conditional Expressions.
##
##a = 2
##b = 330
##print("A") if a > b else print("B")
####
####
####
##### 1 statment with three conditions
####
##a = 330
##b = 330
##print("A") if a > b else print("=") if a == b else print("B")
##
##
##
### Operators with Condition Statments
##
### And
##
##a = 200
##b = 33
##c = 500
##if a > b and c > a:
##  print("Both conditions are True")
##
##
### Or
##
##a = 200
##b = 33
##c = 500
##if a > b or a > c:
##  print("At least one of the conditions is True")
##
##
### Nested If -- If statment inside if statment
##
##x = 41
##
##if x > 10:
##  print("Above ten,")
##  if x < 20:
##    print("and also above 20!")
##  else:
##    print("but not above 20.")
##
##
# Pass statment

a = 33
b = 200

if b > a:
  pass






