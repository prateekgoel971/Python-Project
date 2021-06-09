# Enumerate ---------------
##var='india is '
##for x,y in enumerate (var):
##    print(x)
##    print(y)
##
##for x in enumerate (var):
##    print(x)
    
##for x,y in enumerate (var):
##    if x%2 ==0 :
##        print(x,y)

# Example of Range --------        
##for x in range(10):
##    print(x)
##for x in range(1,10):
##    print(x)
##for x in range(0,10,2):
##    print(x)

## ------- List Data Type ------We can Modify data in list 
##var=[]
##print(type(var))

##var=["Dhoni","Rohit","Raina",7,8]
##print(var[1])
##var[1]="Kohli"
##print(var)

# ----- Deep Copy Vs Shallow Copy ----------

#Deep Copy -- Changes in both variable 
##var=["a","b","c"]
##var1=var
##print(var)
##print(var1)
##var1[2]="z"
##print(var)

# Shallow copy --Changes data only in given variable 
##var=["a","b","c"]
##var1=var[:]
##print(var)
##print(var1)
##var1[2]="z"
##print(var)
##print(var1)

# ----- Functions with List data Type ----------------

##var =["Dhoni","Kohli","Ashwin"]
##
##var.insert(1,"Raina")
##print(var)


##var.append("Welcome")
##print(var)

##var.extend(["Welcome","India"])
##print(var)

##var.pop(0) --- #Delete from index level
##var.pop() ---- # Delete from last index
##print(var)

##var.remove("Kohli") ---# Remove given argument from list 
##print(var)

##var.clear()
##print(var)

##del var[0] ---- #Delete from index level
##print(var)

##del var  ----- # Delete all var and give error also 
##print(var)

##output=[]
##for x in range(9):
##    if x%2 == 0:
##       output.append(x)
##print(output)

##output =[x for x in range(9) if x%2 ==0]
##print(output)
##
##x=[i**+1 for i in range(3)]
##print(x)

# ----- Functions with Tuples data Type ----------------

##var=("Dhoni","Raina","Dhoni")
##print(dir(var))
##print(var.count("Dhoni"))
##var[0]="kohli" ---- # can't modify in tuple data type 
##print(var)


# ----- Functions with Dictionary data Type ----------------

##my_dict= {"Name":"Prateek","Lang":"Python"}
##print(dir(my_dict))
##print(my_dict)

# To add data in given string

##my_dict['coutry'] = "India"
##print(my_dict)

# -- 2 same keys with different value -- wil give output as latest one -Will not provide  duplicate

##my_dict= {"Name":"Prateek","Lang":"Python","Country":"india","Lang":"Australia"}
##print(my_dict)

# - Keys value can be in any format in Dictinary data type

##my_dict= {"Name":"Prateek","Lang":"Python","Country":"india","Lang":"Australia",1:"Kohli",2.0:"Ashwin",True:"Rahul"}

# -- Keys cannot be of duplicate values -- it will give latest value --- in below example it will give -- Raina as output

##my_dict = {True:"Dhoni",1:"Kohli",1.0:"Raina"}
##print(my_dict[True])

##my_dic= {"name":["Dhoni","Kohli"],"age":{"number":[55,56,57]}}
##print(my_dic["name"][1])
##print(my_dic["age"]["number"][1])


#----- Functions in Dictinary ----
##my_dic= {"name":["Dhoni","Kohli"],"age":{"number":[55,56,57]}}

##output=[]
##for x in range(5):
##    output[x]= x*x
##    print(output)
##output ={x:x*x for x in range(5) }
##print(output)
