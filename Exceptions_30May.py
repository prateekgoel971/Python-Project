
# -------- Exception ---------------------------------


# Basic Syntax

##try:
##    var = 10/0
##    print(var)
##    print("a"+10)
##
##except:
##    print("My Error")



# Example 1 --- handling of arithetic error

##try:
##    var = 10/0
##    print(var)
##
##except ZeroDivisionError:
##    print("Arithmetic Error ")


# Example 2 --- Handling of actual Exception from class Exception

##try:
##    print("Prateek" + 10)
##
##except Exception as ex:
##    print(ex)
##
##except:
##    print("My Error")
##
##finally:
##    print("My finally Block")
    

# Example 3:  ------- Catch error in single line

##try:
##    var = 10/0
##    print(var)
##
##except (ZeroDivisionError,TypeError) as ex:
##    print(ex)
##
##except:
##    print("My error")



# Example 4:---- Not system defining error  ----using of word raise to accept own error s

#1) -----

##try:
##    var = 10
##    if var >5:
##        raise IndexError("My Own Error")
##    
##except IndexError as ex:
##    print(ex)
##
##
###2) -----
##    
##try:
##    var = 10
##    if var >5:
##        raise IndexError
##    
##except IndexError:
##    print("index Error")
    


# Example 5:  ---- how to Raise Global Error within the class

##class My_Class(Exception):
##    var = "User Defined Exception "
##
##
##try:
##    var =10
##    if var > 5:
##        raise My_Class
##
##except My_Class as ex:
##    print(ex.var)
  
        


# -------- Method Resolution object (MRO) --------- Priority of calling inheritance class


##class A:
##    def __init__(self):
##        
##
##        
##        def fun(self):
##            print("A")
##
##class B(A):
##    def fun(self):
##        print("B")
##
##
##class C(B):
##    def fun(self):
##        print("C")
##
##
##class D(B,A):
##    pass
##
##D(self).fun()
##        
    

    
    
