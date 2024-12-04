# 1.static variable in python also call class variable inside a class variable
# For total class only one copy of static variable will be created and shared by all objects of that class.
# We can access static variables either by class name or by object reference
# But recommended class name (Ek copy bana create kar lo static variable and share kar lo all objects ko)

class comapny:
    comany_name = "Wipro" # static variable 

    def __init__(self,employe_name):
        self.employee_name = employe_name

    def display(self):
        print(f"Employee:{self.employee_name},company:{comapny.comany_name}") 

emp1 = comapny("sanket")           
emp2 = comapny("deepak")

# Access static variable
emp1.display()
emp2.display()

# change static the variable 
comapny.comany_name ="infosys"
emp1.display()
emp2.display()

#----------------#----------------------------#---------------------------
# Another Example:- class variables(static variable)  & How to modify 

class Employee:
    company_name = "infoys" # class variable 
    def __init__(self,nm,sal):
        self.name = nm         
        self.salary = sal

e1 = Employee("sanket",5000000)        
e2 = Employee("kaushal",1000000)        

print (Employee.company_name)
print (e2.company_name)

# Modification
# Employee.company_name = "TCS" # ye hum ne direct  class or company name ko liye Not an object
# print (Employee.company_name)

e2.company_name = "TCS" # ye alag se new banayega 
print(e2.__dict__)
print(Employee.company_name)
        

# 2 instance variable inside a constructor function we can decare that is non as instance variable 
# Note :-An instance variable is unique to each object and is defined within the constructor (__init__) using self.

# If the value of a variable is varied from object to object, then such type of variables are called
# instance variables.


class Car:
    def __init__(self, make, model):
        self.make = make # Instance variables
        self.model = model

    def display(self):
        print(f"Car: {self.make} {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display()
car2.display()

car1.model = "Camry"
car1.display()

"""How to access Instance variables:
We can access instance variables with in the class by using self variable and outside of the class by
using object reference."""


# @Note:-
# instance variables :- inside a constorctorce variable this instance  non as (object ke level variable yaa ni object to object value of varid)

# static variable :- inside a class we can declare this is static varable(class Level)

# Local variable :- ye hamare function ke baad decalare karte hai (method Level variable)

# global:-out side of class we can define this variable 


# 3 Local variable (method Level variable) :- isko hum function me define karte hai scope limited hota hai to the function
# A local variable is defined inside a function and is only accessible within that function.
# ye sirf wahi function ke liye accessible hai..

def greet():
    Local_message = "Hello, Local!"
    print(Local_message)

greet()

# Another Example :- hum usko jo func banaya hai usme hi sirf access kar sakte hai out side of the nahi kar sakte
class Test:

    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        # print(a) #NameError: name 'a' is not defined (ye sirf a m1 me hi define hoskta hai)
        print(b)
t=Test()
t.m1()
t.m2

# 4 Global variable :- out side of function we can decalare that's non as global variable


# a = 50  # Global variable (iske niche ka sara programe scope hai iska) 
# def my_fun(c):
#     print(a)
#     b=100 # local variable
#     sum1 = b + c
#     print(sum1)
# my_fun    

# Gloable keyword
# name same rakhna padega kabhi us waqt hum use karenge global keyword ka

# a = 50 

# def show():
#     global a
#     a = a + 10
#     print("I:",a)

# show()    
# print("I:",a)

# i = 0
# def myfunc():
#     global i
#     while i<5:
#         i+=1
#         print(i)

# myfunc()
# print("Gloabal:",i)


#  Global variable
# user_name = "Guest"

# def set_user_name(name):
#     global user_name  #  global keyword 
#     user_name = name  # Modifying global variable

# def greet_user():
#     print(f"Hello, {user_name}!")

# greet_user()
# set_user_name("sanket")
# greet_user()


"""
Note:-
 How to delete instance variable from the object:

1. Within a class we can delete instance variable as follows
del self.variableName
2. From outside of class we can delete instance variables as follows
del objectreference.variableName


If we change the value of static variable by using either self
or object reference variable:


Ager value chamge karna hai to hum either use karenge self* kaa object refrence variable uske baad hogi change
uske name kaa new instance variable add hoga that particular object.
"""
class Test:
    a = 10
    
    def my_func(self):
        self.a = 800

t1 = Test()
t1.my_func()

print(Test.a) # ye class ka variable # 10
print(t1.a) # ye function ka variable hai # 800

#----------------#----------------------------#---------------------------
"""
in this example line 188 this b is an instance variable. 
It is created inside the __init__ method and is unique to each object (t1, t2, etc.).
"""
class Test:
    a=10
    def __init__(self):
        self.b=20

t1=Test()
t2=Test()

Test.a=888

t1.b=999

print(t1.a,t1.b)
print(t2.a,t2.b)

#----------------#----------------------------#---------------------------
# Not delete by using object refrence variable ****
# By using object reference variable/self we can read static variables, but we cannot modify
# or delete.

# Eg:-
# class Test:

#       a=10
# t1=Test() # object reference variable
# del t1.a #===>AttributeError: a

# hum object reference variable se static variable ko read kar sakte hai but we can not modify or delete. If we are trying then we will get error.

# We can modify or delete (static** variables only) by using classname or cls variable.
# (And ager karna hai to direct class name yaa uska variable but we can not delete as object variable)
# del Test.a -->True or class name also we can delete ..