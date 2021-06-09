#------Example of count Function ------------

##var="Dhoni is my history"
##output=var.count("i")
##print(output)

#------Example of Find Function ------------ if input not found then it will return -1 and execute rest code
##var="Dhoni is my history"
##output=var.rfind("a")
##print(output)
##print("Hello")
      
#------Example of Index Function ------------ if input not found then it will terminate whole program and not execute rest code

##var="Dhoni is my history"
##output=var.rindex("a")
##print(output)
##print("Hello")

#------- looping (Iteration) ----------------

# Example 1 :
##var="Dhoni is my history"
##for x in var:
##    print(x)

#Example 2:
##var="Dhoni is my history"
##counter=0
##for x in var:
##    print(x)
##    counter = counter + 1
####    counter = L-1
##    print(counter)

# ------------ Example of if & else & elif Statment ----------

# Example 1:

##var ="India is "
##for x in var:
##    if x == 'i':
##       print("Success")
##    elif x == 'a':
##        print("Success")
##    else:
##        print('Failure')

# Example 2 :

##var ="India is "
##for x in var:
##    if x == 'i'or x =='a':
##       print("Success")
##    else:
##        print('Failure')


# ---------- Example of Concate String -----------



##name ="Dhoni"
##score = 59

# Example 1:
##statment = "My captain " + name + " scored " + str(score) + " against Srilanka "

# Example 2:
#%s --- string
#%d ---- integer
##statment = "My captain %s  scored  %d  against Srilanka "%(name,score)

#Example 3:
# use of curly bracket {}
##statment = "My captain {}  scored  {}  against Srilanka ".format(name,score)

#Example 4:
##statment = f"My captain {name}  scored  {score}  against Srilanka"
##print(statment)
