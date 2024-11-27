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

what is methods :-in side the class function are non as methods(class ke under jo function aata hai woh this is none as methods)

what is instance:-(constrocter ke under jo variable ata hai woh)
"""
# Attribute :- class ke under ke variable ko 
# methods :- in side the class function 
# instance :- cnstocter under variable 

"""
What is object :- instance of the object python is every thing is object like:- name,car,pen,laptop
syntax:- referncevarable = classname()

"""



# variables :- 
"""
1  
2 instance 
3. local 

methods :- 
1 class 
2 istance 
3 static methods 
"""
# class variables  & How to modify 

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



