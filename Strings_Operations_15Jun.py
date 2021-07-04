# --- Strings Operations ------

#1) capitalize()
# --- Converts the first character to upper case

##txt = "hello, and welcome to my world."
##
##x = txt.capitalize()
##
##print (x)

# --- if first character is number 


##txt = "36 is my age."
##
##x = txt.capitalize()
##
##print (x)


### 2) casefold()
### --- Converts string into lower case
##
##txt = "Hello, And Welcome To MY World!"
##
##x = txt.lower()
##
##print(x)

# 3) center()
# -----Returns a centered string --- It will take space --- It is mandatory to give argument 

##txt = "PY"
##
##x = txt.center(20)
##
##
##print(x)


#--- it will take 0 in output exclude space 

##txt = "banana"
##
##x = txt.center(20, "O")
##
##print(x)


# 4)count()
# --Returns the number of times a specified value occurs in a string 

##txt = "I love apples, apple are my favorite fruit"
##
##x = txt.count("apple")
##
##print(x)

# --- Search from position 10 to 24:
##txt = "I love apples, apple are my favorite fruit"
##
##x = txt.count("apple", 10, 24)
##
##print(x)



# 5)endswith()
# --Returns true if the string ends with the specified value

##txt = "Hello, welcome to my world."
##
##x = txt.endswith(".")
##
##print(x)

# ----
var = "Hello, welcome to my world."

x = var.endswith("my world")

print(x)






