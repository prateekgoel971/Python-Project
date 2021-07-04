# ---- Python Loops -----

# While Loop
# With the while loop we can execute a set of statements as long as a condition is true


##i = 1
##while i < 6:
##  print(i)
##  i += 1


# The break Statement
##With the break statement we can stop the loop even if the while condition is true:

##Example

##i = 0  
##str1 = 'javatpoint'  
##  
##while i < len(str1):   
##    if str1[i] == 't':   
##        i += 1  
##        break  
##    print('Current Letter :', str1[i])   
##    i += 1  



# Continue Statment
# With the continue statement we can stop the current iteration, and continue with the next:

##i = 0  
##str1 = 'javatpoint'  
##  
##while i < len(str1):   
##    if str1[i] == 'a' or str1[i] == 't':   
##        i += 1  
##        continue  
##    print('Current Letter :', str1[i])   
##    i += 1  


# Else Statment
# Print a message once the condition is false:

##i = 1
##while i < 6:
##  print(i)
##  i += 1
##else:
##  print("i is no longer less than 6")




# Python For Loops
# A for loop is used for iterating over a sequence


##fruits = ["apple", "banana", "cherry"]
##for x in fruits:
##  print(x)


# looping through a string

##for x in "banana":
##  print(x)

# Break Statment

##fruits = ["apple", "banana", "cherry"]
##for x in fruits:
##  print(x)
##  if x == "banana":
##    break


# Continue Statment

##fruits = ["kiwi", "banana", "orange"]
##for x in fruits:
##  if x == "banana":
##    continue
##  print(x)


# Range Function

##The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 and ends at a specified number.

# 0,1,2,3,4,5
##for x in range(6):
##  print(x)
##
### 2,3,4,5
##for x in range(2, 6):
##  print(x)


##for x in range(2, 30, 3):
##  print(x)



# Else Statment
# Once the loop is finished


for x in range(6):
  print(x)
else:
  print("Finally finished!")
