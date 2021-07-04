# 1) what is String ?

##A string is a sequence of characters.
##A character is simply a symbol. For example, the English language has 26 characters.


# 2) How to define strings in Python ?

##my_string = 'Hello'   # --- single Quotes
##print(my_string)
##
##my_string = "Hello"   # --- double quotes
##print(my_string)
##
### triple quotes string can extend multiple lines
##my_string = """Hello, welcome to
##           the world of Python"""
##print(my_string)


# 3) How to access string character/ String Slicing ?

##str = 'programiz'
##print(str)
##
###first character
##print(str[0])
##
###last character
##print(str[-1])
##
###slicing 2nd to 5th character
##print(str[1:5])
##
###slicing 6th to 2nd last character
##print(str[5:-1])


# 4) How to change a string or delete a string ?

# --- In Python we can't modify a particular string at index level 
##my_string = 'Prateek'
####my_string[5] = 'a'
####print(my_string)
##
### output : 'str' object does not support item assignment
##
##my_string = 'Python'
##print(my_string)

# ---For a particular string --

##my_string = 'Python'
##del my_string
##print( my_string)


# 5) What is Concatenation of strings in Python ?

##Concatenation is Joining of two or more strings into a single one.

##Name ='Rahul'
##Marks = 95

##Strng = Name + " scored " + str(Marks)+  " in Maths "
##print(Strng)

##Strng = "%s scored %d in Maths" %(Name,Marks)
##print(Strng)
##
##Strng = "{} scored {} in Maths" .format(Name,Marks)
##print(Strng)
##
##Strng = f "{Name} scored {Marks} in Maths"
##print(Strng)


# 6) Iterating Through a string

##We can iterate through a string using a for loop

##var = "Python Presentation "

##for itr in var:
##    print(itr)


##for itr in var:
##          if itr == 'y':
##             print("True")
##             break
##          else:
##              print("false")
          

# ---- Enumerate is use where we want output with index number and letters in variable
##for itr in enumerate (var):
##    print(itr)
 
          
