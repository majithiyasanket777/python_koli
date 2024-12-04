# 1  Instance Methods:

"""
Inside method implementation if we are using instance variables then such type of methods are
called instance methods.
Inside instance method declaration,we have to pass self variable.

(method ke under implementation karte hai instance variables kaa use karke to ese methods ko instance method kaha jata hai.)
"""

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print("hey!!",self.name)
#         print("your Marks are:",self.marks)
#     def grade(self):
#         if self.marks>=70:
#             print("you got first grade") 
#         elif self.marks>=50:
#             print("you got second grade") 
#         elif self.marks>=40:
#             print("you  got Third grade") 
#         else:
#             print("you are Failed")

# n = int(input("Enter number of student:"))
# for i in range(n):
#     name = input("Enter your name:")
#     marks = int(input("Enter your marks:"))

#     s = Student(name,marks)
#     s.display()
#     s.grade()
# print()



# 2 static methods :- methods which performs operations on external data
"""
esa data jo kisi class se belong karta ho or naa kisi object se
"""

# - No need to pass object or class reference
# - created using decorator
# Eg:-

class Math:

    @staticmethod
    def add(x,y):
        print('The sum:',x+y)

    @staticmethod
    def product(x,y):
        print('The product:',x*y)    

    @staticmethod
    def average(x,y):
        print('The average:',(x+y)/2)    

Math.add(10,20)
Math.product(10,20)
Math.average(10,20)


# 3 class method :-
"""
Inside method implementation if we are using only class variables (static variables), then such type
of methods we should declare as class method.

We can declare class method explicitly by using @classmethod decorator.
For class method we should provide cls variable at the time of declaration

"""

class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name,cls.legs))
Animal.walk('Dog')    
Animal.walk('cat')    

# Another program

class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noOfobjects(cls):
        print('The number of objects created for test class:',cls.count)    

t1=Test()        
t2=Test()
Test.noOfobjects()
t3=Test()  
t4=Test()  
t5=Test()
Test.noOfobjects()  



# Garbage Collection:

"""
In old languages like C++, programmer is responsible for both creation and destruction of
objects.Usually programmer taking very much care while creating object, but neglecting
destruction of useless objects. Because of his neglectance, total memory can be filled with useless
objects which creates memory problems and total application will be down with Out of memory
error.

But in Python, We have some assistant which is always running in the background to destroy
useless objects.Because this assistant the chance of failing Python program with memory
problems is very less. This assistant is nothing but Garbage Collector.

useless objects ko destroy kar deta hai
"""

# How to enable and disable Garbage Collector in our program:
#  By default Gargbage collector is enabled, but we can disable based on our requirement

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled()) # After re-enabling garbage collection, this prints True again.




# class :- ese methods jisme hum class variable ko implmetions kare usind 
# This checks if garbage collection is still enabled. Since it was disabled 
# in the previous step, this prints False.

# instance :- method ke under impimentsion karte hai instance variable kaa to ese methods ko instance methods kaha jata hai.. 