"""
class is blue print of objects  in python every things is object to create requried some Model or blue print
which is nothing but class

properties can be represent --> variables
Acion can be represent ---> methods 

3 variables are allowed:- 

1 Instance variables(object Level variables)
2 static variable(class Level variables)
3 Local variable (Methods Level variables)

various types of allow methods
1 instance methods
2 class methods
3. static methods


what is Attributes :- varable in class that is attributes
EX:- name : str = str()
EX:- universtity : str = str()

what is methods :- in side the class function are non as methods(class ke under jo function aata hai woh this is none as methods)

what is instance:-(constrocter ke under jo variable ata hai woh)
"""
# Attribute :- class ke under ke variable ko 
# methods :- in side the class function 
# instance :- cnstocter under variable 

"""
What is object :- instance of the object python is every thing is object like:- name,car,pen,laptop
syntax:- referncevarable = classname()

"""

# Constructor:- __init__ se define karenge , dunder method bhi kaha jata and magic method bhi kehte 
# Without Constructor :- object cannot be creted 
 
# 1 parameter rise Constructor :-

class Fruite:
    def __init__(self,name,python,java):
         self.name = name
         self.marks = python,java 

obj = Fruite("sanket",90,50)
print(obj.__dict__)

obj2 = Fruite("deepak",60,90)
print(obj2.__dict__)

# 2  Default Constructor:- self Arrgumet lega

class Fruite:
    def __init__(self):
        print("object has been created ")

    def show_type(self,fruite_type):
        print(f"This is a{fruite_type}")

my_fruite = Fruite() 
my_fruite.show_type('Apple')           

# or 

class Employee:
    def __init__(self):
        self.salary = 22000
        self.age = 21 

e1 = Employee()        
e2 = Employee() 
print(e1.__dict__)

# 3. Default 
class Employee:
    pass

e1 = Employee()        
e2 = Employee() 
print(e1.__dict__)


# variables :- 
"""
1  static variable (class variable)
2 instance variable (object level variable)
3. local  vaiable   (method level variable)

methods :- 
1 class (class related method)
2 istance (class realeted method)
3 static methods (General utility method)
"""



# instance method:- If we are using atleast one instance variable(using static) 

"""
Esi method jo class variable ho instance ussi method ko instance method kaha jata hai..

Inside method implementation if we are using instance variables then such type of methods are
called instance methods.
Inside instance method declaration,we have to pass self variable.

"""        

