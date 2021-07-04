# ----- Lists ---------

# -- Lists are used to store multiple items in a single variable.
# --List items are ordered, changeable, and allow duplicate values.
# -- List items have a defined order, and that order will not change.
# -- List are defined with usage of square brackets.[]
# - ist items are indexed, the first item has index [0], the second item has index [1]


# Example :

##ls =["apple", "banana", "cherry"]
##print(ls)


# Allow Duplicate

##var = ['Prateek','Vikram','Mounika','Vikram','Prateek']
##print(var)

# List can be of any data type (int,boolean,string)

##my_list = ['Python',2,True,'Presentation',False,3,6]
##print(my_list)


## List can be modify

##lst = ['Java','Python','PHP','.NET']
##lst[3] = "CSS"
##print(lst)

# --- It will modify the value of banana and cherry


# -- 1:3

##thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
##thislist[1:3] = ["blackcurrant", "watermelon","Apple","Bana"]
##print(thislist)


# -- Modify 2 and 3 index value with only single value 
##thislist = ["apple", "banana", "cherry"]
##thislist[1:3] = ["watermelon"]
##print(thislist)

# Range of Index -- include start index value and exclude last index value 

##thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
##print(thislist[2:5])
##
##thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
##print(thislist[-4:-1])



# ---- Various Method of List Data Type -----


# ---- INSERT ----->  method inserts an item at the specified index

##var = ["India","Australia","Africa","Sri Lanka"]
##var.insert(1,"Newzealnd")
##print(var)
##
### --- APPEND ----- > Always add data at the last index
##
subject = ["Maths","English","Hindi"]
SUB1 = ["A","b"]
subject.append(SUB1)
print(subject)
##
### ---- EXTEND ------> To append elements from another list to the current list
##
##thislist = ["apple", "banana", "cherry"]
##tropical = ["mango", "pineapple", "papaya"]
##thislist.extend(tropical)
##print(thislist)
##
### --- we can append tuple,dictonaries also
##
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
##
##
### ----- POP -------> is to delete/remove element from given list with respect to index value.If indx value not given then it will delete from last index value .
##
Letters = ['A','B','C','D']
Letters.pop()
print(Letters)
##
Numbers = [1,2,3,4,5]
Numbers.pop(2)
print(Numbers)
##
### ---- REMOVE ----- > It will remove/delete data from given list
##
Team = ["Dhoni","Virat","Rohit","Ashwin","Virat"]
Team.remove("Virat")
print(Team)
