import sqlite3

# Create table 
##connection = sqlite3.connect("Prateek.db")
##query="""create table student ("Name" text, "Age" number)"""
##query_execution = connection.execute(query)
##connection.commit()
##connection.close()

#Insert Data
##connection = sqlite3.connect("Prateek.db")
##query="""Insert into student ("Name","Age") values ("Prateek",27)"""
##query_execution = connection.execute(query)
##connection.commit()
##connection.close()


#Extract Data (getting Data from DB)
##connection = sqlite3.connect("Prateek.db")
##query="""Select * from student"""
##query_execution = connection.execute(query)
##query_output = query_execution.fetchall()
##print(query_output)
##connection.commit()
##connection.close()


# -----Usage of Function -------

##def my_db(query,db):
##    connection = sqlite3.connect(db)
##    query_execution = connection.execute(query)
##    query_output = query_execution.fetchall()
##    print(query_output)
##    connection.commit()
##    connection.close()
##
##a="Prateek.db"
##b="""Select * from student"""
##my_db(b,a)

# ---- File operation -----

file_obj = open("Prateek.txt","w")
file_obj.write("asdd")
file_obj.close()
