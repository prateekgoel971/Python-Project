# ------ Classes ------------

#Basic example

#Example 1 :

##class My_Class:
##    var ="Dhoni"
##    def Login(ip,pwd):
##        print(ip,pwd)
##    def Hostname(ip):
##        print(ip)
##
##
##print(My_Class.var)
##My_Class.Login("3.3.4.55",1234)
##My_Class.Hostname("3.3.4.55")


# Example 2: Constructor 

##class My_Class:
##    def __init__(self,ip,pwd):
##        self.a = ip
##        self.b = pwd
##
##    def login(self):
##        print(self.a,self.b)
##    def hostname(self):
##        print(self.a)
##
##
##my = My_Class("3.3.4.55",1234)
##my.login()
##my.hostname()



# Example 3 : Overriding

##class My_Class:
##    def __init__(self,ip,pwd):
##        self.a = ip
##        self.b = pwd
##
##    def login(self):
##        print("One",self.a,self.b)
##    def login(self):
##        print("Two",self.a)   #-------- output
##
##
##my = My_Class("3.3.4.55",1234)
##my.login()



# Example 4: Inheritance

##class My_Class:
##    def __init__(self,ip,pwd):
##        self.a = ip
##        self.b = pwd
##
##    def login(self):
##        print("One",self.a,self.b)
##
##class Second_Class(My_Class):
##    def hostname(self):
##        print(self.a)
##
##
##my= Second_Class("3.3.4.55",1234)
##my.hostname()
##my.login()


