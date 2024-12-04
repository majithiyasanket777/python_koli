"""
# getter syntaxt:-@property laga di to woh getter ban gaya.[in python are methods that are used to access the values of an object's properties.] New Method baan rahe jo behave kar raha hai like a property.
#**Actualy use :- kisi function ki return value ko Ek object ki property ki Tarah istmaal kar sakte hai And usko set bhi kar sakte hai 

setter methods also call Mutator method.
getter methods also call Accessor method.

setter method :- set values of instance variable (esi values hoti hai jiska use karke aap instance variable ka value change kar sakte hai ek new instance variable bana sakte hai.)

getter method :- set values of instance variable (sirf data ko fetch karega No modification and no changes variable)

setter syntax :- @(property_name).setter
@ten_value.setter 

# Getter syntax:-

def getVariable(self):
    return self.varable

"""

class Myclass:
    def __init__(self,value):
        self.value = value

    def show(self):
        print(f"value is {self.value}")

    @property # getter ye decorator hai hamara
    def ten_value(self):
        return 10* self.value

    @ten_value.setter # setter decorator
    def ten_value(self,new_value):
        self.new_value = new_value/10


obj = Myclass(10)   
obj.ten_value = 67   
print(obj.ten_value)  


# Another example :- 

class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.Marks=marks

    def getmarks(self):
        return self.Marks        


n = int(input("Enter number of student:"))
for i in range(n):
    s=Student()
    name=input("Enter Name:")
    s.setName(name)
    marks=int(input('Enter Marks:'))
    s.setMarks(marks)


    print('Hi',s.getName())
    print('Your Marks:are:',s.getmarks())
    print()





    

# gettter :- get value fetch karega values ko woh modifly or change nahi kar sakta values ko Accesore  

# setter :- we can modifly and change the values instance variable values mutatore



# class Employee:
#     def setName(self,nm):
#         self.name = nm

#     def getName(self):
#         print("The name is:",self.name)
             
  

# setter syntax 
def setvariable(self,variable):
    self.variable = variable

# Example
def setName(self,name):
    self.name = name    

# getter method 

def getvariable(self):
    return self.varable

# Example 
def getName(self):
    return self.name


# getter 

def getvariable(self):
    return self.varable


# setter

