# 1 class me multiple function honge yaa Ek hi function ko hum multiple time call karenge Alag Alag value ke through..

# in python method overriding is possibal and supported
# and method overloading are not supported

"""
Note:- Ek class define kiya hai usme 2 methods(function) hai  ya usse jyada same name ki and  uske behaviour (properties) are diffrent
so This is method overloading 

"""
# Note :- Ager hum baar baar same name ke methods(fun) ko decare karte hai and diffrent number of parameters than python always considerd last method
# function overloading :- class name same ,method bhi same  paramiters are different 
# function overRiding :- class name same paramiters are same lekin A ko B me inharit karana...


# op. 1 method overloading

class A:
    def show(self):
        print("Welcome")
        
    def show(self,Firstname=''):
        print("Welcome",Firstname) 
        
    def show(self,Firstname='',Laststname=''):
        print("Welcome",Firstname,Laststname) 
        
obj =A()
obj.show()   
obj.show('Ankush')         
obj.show('Ankush','majithiya')


# How to Achive in python overloading (jugad) if elif else se kar saktehai
# youtube link :- https://www.youtube.com/watch?v=25iwB1d8r3Q&t=364s 
class calci:
    def add(self,num1=None,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            print("Addition is:",num1+num2+num3)
        elif num1!=None and num2!=None:
            print("Addition is:",num1+num2)
        else:
            print("incorrect parameter method") 

c1 = calci()
c1.add(10,20)                   
c1.add(10,20,30)       


#op-2)-----------------Operator Overloading:---------------#

# We can use the same operator for multiple purposes, which is nothing but operator overloading.

# Eg1: + operator can be used for Arithmetic addition and String concatenation
print(10+20)#30
print('durga'+'soft')#durgasoft
      
# Eg2: * operator can be used for multiplication and string repetition purposes.
print(10*20)#200
print('durga'*3)#durgadurgadurga

class Employee:

    def __init__(self,name,salary):

        self.name=name

        self.salary=salary

    def __mul__(self,other):

       return self.salary*other.days

class TimeSheet:

      def __init__(self,name,days):

            self.name=name
            self.days=days
e=Employee('Durga',500)
t=TimeSheet('Durga',25)
print('This Month Salary:',e*t)

#op-3)-----------------Constructor Overloading:---------------#

"""
Constructor overloading is not possible in Python.**
If we define multiple constructors then the last constructor will be considered.
"""

# class Test:
#     def __init__(self):
#         print('No-Arg Constructor')

#     def __init__(self,a):
#         print('One-Arg constructor')

#     def __init__(self,a,b):
#         print('Two-Arg constructor')    
# t1=Test()
# t1=Test(10)
# t1=Test(10,20)

# 2)-----------------*methodOverriding---------------#-        

class A: # parent
    def Disp(self):
        print("This is parant class method..!! ")

    
class B(A):    
    def Disp(self):
        super().Disp() # paranet class ko inharharite
        print("This is child class method")
        
obj =B()
obj.Disp()

#----------------- Constructor overriding Program :---------------#-        
class p:
    def __init__(self):
        print('parent class Constructor')

class B(p):
    def __init__(self):
        print('child class Constructor') 
c = B()

# output:- child class Constructor
#----------------- Parent class constructor by using super() Method overriding: :---------------#-        

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, eno, esa):
        super().__init__(name, age)  # Initialize the super() method on parent class
        self.eno = eno
        self.esa = esa

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.eno)
        print("Employee Salary:", self.esa)

e1 = Employee('Sanket', 22, 77777, 100000)
e1.display()

e2 = Employee('Deepak', 18, 7777, 15000)
e2.display()

#-----------------builte in function functionality change---------------#-        
class cart:
    def __init__(self,basket1,basket2,basket3):
        self.clothes = basket1
        self.electronics = basket2
        self.other = basket3

    def __len__(self): # ye hum ne khud se banaya hai so isme hum ne len  ko return karvaya and uska concatination karvaya...
        print("total number of items in cart:") 
        return len(self.clothes)+len(self.electronics)+len(self.other)

shantanu=cart(['jeans','shirt','t-shirt'],['earphones','mobile'],['chair'])
print(len(shantanu)) #6

#3)-----------------Duck_typeing---------------#-        

# Duck_type :- mujhe object ka  name nahi malum hai to woh automatically le lega us object ki value ko mujhe specified karne ki jarrorat nahi hai.


"""
In Python we cannot specify the type explicitly. Based on provided value at runtime the type will
be considered automatically. Hence Python is considered as Dynamically Typed Programming
Language.

(python me hum type specify nahi kar sakte run time par value ke adhar par usko nakki kiya jata hai isliye woh Dynamically typed programming Launguage hai)
 But we can solve this problem by using hasattr() function.
"""
# hasattr() function.


class Duck:
    def talk(self):
        print('Quack..Quack..')

class Dog:
    def talk(self):
        print('Bow Bow..')
class Cat:
    def talk(self):
        print('meow meow..')
class Goat:
    def talk(self):
        print('myaah myahh..')


def f1(obj):
    obj.talk()

i = [Duck(),Duck(),Cat(),Goat()]
for obj in i:
    f1(obj)


# method overloading :- class same methods are same but parameters are difreent 

# method overriding :-  class name same methods are same parameter bhi same lekin A ko B me inharit karate hai 


