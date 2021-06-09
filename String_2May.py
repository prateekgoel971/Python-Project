#------------Example of Sting datatype -----------------

##country = "India"
##print(country)
##print(type(country))



##country = 'India'
##print(country)
##print(type(country))


# --------------Index Represetation --------------------------
# 0,1,2,3,4

##country = 'India'
##print(country[3])

#Output = i


# ----------String example with space and more variations------------

statment = "MI vs CSK"

##print(statment[0])
# Output --- M

##print(statment[0:])
# output --- MI vs CSK  0: Means forward direction till end

#print(statment[0:5])
# output --- MI vs  0: Means forward direction till 5

#print(statment[-1])
#output --- K minus pick value from last

##print(statment[-2:])
# backward Direction
#output --- SK minus pick value from last

#  -------------Len & Dir Fucntion example------------

##country = "India is "
##print(len(country))
##print(dir(country))


### -------Example of r -- RAW DATA-------------

##path=r"c:\new\time.txt"
##print(path)

#print same path as above otherwise if we are not giving r then it will take it as \librarry 

# ----------Example of String and Integer function with Input Data --- Not work in 2.7 version -------------

##country=input("Enter your name : ")
##print(country)
##print(type(country))

##Integer function with Input Data
##score=int(input("Enter your Number : "))
##print(score)
##print(type(score))

#---- String is immutable (Modification is not allowed) Example ------------
##Country = "Australia"
##Country [3] = "d"
##print (Country)

#output -----  'str' object does not support item assignment


##name= input('what is your name ? ')
##colour = input('what is your favourite colour')
##print(name + "Favourite" + colour)
