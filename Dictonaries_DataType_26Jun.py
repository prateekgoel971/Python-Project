# -- change the item value

d1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

d1["year"] = 2018

print(d1)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# --- Add item to dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)

student = {
    "Name":"Prateek",
    "Age":27,
    "Subject":"Python"
    }
student.update({"Class":"12th Standard"})
print(student)

# -- Remove item

##team = {
##    "Name":"Dhoni",
##    "Number":7,
##    "Age":36
##    }
##team.pop("Number")
##print(team)

##class= {
##    "Name":"Rahul",
##    "Age":25,
##    "RollNo":33,
##    "Phone":"2456788"
##    }
##class.popitem()
##print(class)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",s
  "year": 1964
}
del thisdict["model"]
print(thisdict)

student = {
    "Name":"Prateek",
    "Age":27,
    "Subject":"Python"
    }
del student
print(student)

