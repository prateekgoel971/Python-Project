# ------User Defined Functions--------

#1) functions without Arguments
##def My_function():
##    print("Welcome to HDFC Bank")
##
##My_function()    
##
##

#2) functions with One Argument
##def My_function(Name):
##    print("Hello",Name, "Welcome to HDFC Bank")
##
##My_function("Dhoni")    

#3) functions with More than 1 Arguments
##def my_function(name,country):
##    print("Hello", name, "from" ,country, "welcome")
##
##my_function("dhoni","Ranchi")
##my_function("kohli","Delhi")


#4) Function with Default Arguments

##def my_function(name,Country="India"):
##    print("Hello",name,"from",Country,"Welcome")
##
##my_function("dhoni")
##my_function("virat","Aust")
                

##def my_function(name="Dhoni",Country="India"):
##    print("Hello",name,"from",Country,"Welcome")
##
##
##my_function()
##my_function("Virat","Aus")


#-- put default parameter as last argument--

##def my_function(name="Dhoni",Country):
##    print("Hello",name,"from",Country,"Welcome")
##
##
##my_function("India")
##my_function("Virat","Aus")

# Output : Give error as last argument


#---- Keyword Argument ---- We swipe argument position 

##def my_function(Country,name):
##    print("Hello",name,"from",Country,"Welcome")
##
##
##my_function(name="Dhoni",Country="India")


# ----- Star Argument ----- number of argument max in form of tupple

##def my_func(*name):
##    print(name)
##
##my_func("Dhoni","Ashwin","Raina")
##my_func("Virat")
    
# ----- Double Star Argument ----- multile number of argument  in form of Dictinory

##def my_func(**name):
##    print(name)
##
##my_func(name="Dhoni",age=36)
##my_func(name="Virat",Team="RCB")

#------- Return statment --------

#1)Example

##def my_score(eng,math):
##    total=eng+math
##    return
##
##print(my_score(75,77))
##
### output = None because we are not returning any value



#2) example

##def my_score(eng,math):
##    total=eng+math
##    return total
##
##print(my_score(75,77))
##
### output = 152 because we returning total of sum



# --- Returning more than 1 output

##def my_score(math,eng,name):
##    total=math+eng
##    return total,name
##
##output= my_score(70,80,"Prateek")
##print(output)    #--- return both total & name
##print(output[0]) #--- return only total
##print(output[1]) #--- return only name


## Scoping ------- Priority of variable ----

var = 1000
def func():
    var=100
def func():
##    var = 10
    print(var)


func()


## --- Modification of global Variable -----

##var = 1000
##def my_func():
##    global var # -- declare global -- to modify of outside var -- make a use of global variable --- without using it will give error 
##    var+=10
##    print(var)
##
##my_func()    

#----- to print output till 100
##var = 0
##def fun():
##    global var
##    print("hello",var)
##    var+=1
##    if var ==100:
##        return
##    fun()
##
##fun()          

