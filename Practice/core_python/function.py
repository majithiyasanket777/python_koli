# User Define function()
# syntax :-
# def function_name(parameters):

# Built in functions():- print,id,type,input etc 

# def wish(name):
#     print("hello good morning",name,"Thank you for messageing me")
# wish("sanket")    
# wish("Deepak")   

# squer of function

# def squerenumber(number):
#     print("The squere of number",number,"is",number*number)
# squerenumber(4)    
# squerenumber(5)    

#-----------#--------------#-------------#-------------#------------
# Reurn value
def add(x,y):
    return x+y
result=add(10,20)
print("The sum is:",result)
print("The sum of is",add(100,200))

#-----------#--------------#-------------#-------------#------------
# Return kuch bhi nahi karayenge to  Answer None aayega....
# If we are not writing return statement then default return value is None
def f1():
    print("Hello")
f1()
print(f1())    
#-----------#--------------#-------------#-------------#-------------
# using function Even or odd

def my_func(num):
    if num %2==0:
        print(num,"is Even number")
    else:
        print(num,"is odd numbers")    
my_func(10)
my_func(15)
#-----------#--------------#-------------#-------------#-------------
"""  4 types of  Arrgumets are allowed in python
1.Positional arguments
2. keyword arguments
3. default arguments
4. Variable length arguments
"""
# 1..Positional arguments # The number of Argumets must be matched, order is important (isme 2 posstion dii hai to function me bhi do hi deni)

def sub(a,b):
    print(a-b)

sub(100,200)
sub(200,100)

# 2.  keyword arguments:- The number of Argumets must be matched, order is not important (order aage piche hoto chalega, but same of name hona chahiye)

def wish(name,msg):
    print("hello",msg,name)

# wish(name="sanket",msg="Good morning")    
# wish(msg="Good morning",name="sanket")    
"""
Note:-
wish("sanket","good morning") # valid
wish("sanket", msg="good morning") # valid
# wish(name="sanket","good morning") # invalid Becasue 
"""
# 3.) Default arguments :-some time we can provide default values for out positional Argumets
def wish(name="guest"):
    print("Hello",name,"Good morning")

wish("sanket")
wish()    

def speack(name="Animal"):
    print("Hello",name,"Good morning")
speack("vivek")    
speack()  

# 4.) variable length arguments:- implemented by tuple concept (*n any number of arrguments are pass)*Astrac symbol
def sum(*n): # def sum(n,*n): # ek value haamri n me gai hai woh 10 kaam dega haar baar hume...
    total = 0
    for x in n:
        total=total+x
    print('The sum:',total)     
sum()
sum(10)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)
sum(10,20,30,40,50)

def sum(name,*marks):
    total = 0
    for x in marks:
        total = total+x
    print("hello:",name,'your total marks are',total) 
sum('sanket',10,80,30)       
sum('deepak',50,20,30)   
#-------------------#-------------#-------------#-------------
# veriable length keyword Arrgument
                       
def sum(num1,**num): # ek value haamri num1 me gai hai so aab sum uske Alwa ki values ka hoga
    sum = 0
    for key in num:
        sum=sum+num[key]
        print(sum)

sum(num1=10,num2=20)
sum(num1=10,num2=20,num3=30)
sum(num1=10,num2=20,num3=30,num4=40)


#-------------------#-------------#-------------#-------------
# def f1(n,*s):
#     print(n)
#     for s1 in s:
#         print(s1)
# f1(10)    
# f1(10,20,30)    
#-----------#--------------#-------------#-------------#-------------
   
def wish(name,msg="how are you!!"):
    print("Hello",name,msg)

wish(name="sanket",msg="good morning")    
# wish(msg="thanks for messaging..!!!",name="sanket",)    
#-----------#--------------#-------------#-------------#-------------
# variable lenght arguments 

def sub(*n):
    total=0
    for x in n:
        total=total+x
    print("the sum :",total)
   
sub(10)
sub(10,20)
sub(10,20,30)    
sub(10,20,30,40)    
sub(10,20,30,40,50)    

#-----------#--------------#-------------#-------------#-------------
#global  pure program me globay  access karega work karega 

a = 10
def f1():
    print(a)

def f2():
    print(a) 
        
print()

# local  perticular function ke under hi kaam karega local variable

def f1():
    a = 10
    print(a)

def f2():
    print(a)

f1()    
f2()     
#-----------#--------------#-------------#-------------#-------------
# Recursive Functions:-  1  reduce lenght of code and improve redablity,complex problem can be solve 

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("factorial of 4",factorial(4))    
print("factorial of 4",factorial(5))    

# def demo():          # function ke under function pass kiya ye 1000 times chalega fir error maximum recursion depth  this error will be show 
#     print("hello")
#     demo()

# demo()    
#-----------#--------------#-------------#-------------#-------------
# function Aliasing:  એલાઇઝિંગ  # existing func we can give another name. ise ager hum ne one name delete kiya to bhi stil we can access that function by using alias name 
# Note :- in python function are also object (python me memoary loaction hexa decimal values ka use karke kii jaati hai..)

def wish(name):
    print("good morning:",name)

greeting=wish
print(id(wish))
print(id(greeting))

greeting('sanket')
wish('sanket')

# delted function stile we can access
def wish(name):
    print("Good morning",name)

greeting = wish # jo greeting hai usko bola jaayega aliases name (you can create any number of aliases)

greeting('sanket')
wish('sanket')

del wish
# wish('sanket') # Name error wish is not defined

greeting('pavan')


def display(name):
    print(name)

# print(type(display)) # function denge to type function milega   
# print(type(10)) # <int> 
#-----------#--------------#-------------#-------------#-------------
# Nested function  :- function inside function define

def outer():
    print("outer function started")

    def inner():
        print("inner function is execustion")
    print("outer function calling inner function") 
    inner()
outer()
#-----------#--------------#-------------#-------------#-------------
# Function Decorators:

def my_decor(func):
    def wrapper(name):
      if name == "sanket":
          print("Hello sanket bad morning")
      else:    
          func(name)
    return wrapper

@my_decor
def wish(name):
    print("hello",name,"good morning")

wish("sanket")
wish("durga")
wish("sunny")
#-----------#--------------#-------------#-------------#-------------
def my_decor(func):
    def wrapper(name):
      if name == "sanket":
          print("hello sanket bad morning")
      else:    
          func(name)
    return wrapper

# @my_decor
def wish(name):
    print("hello",name,"good morning")

decorefunction = my_decor(wish)
wish("sanket")
wish("durga")
# wish("sunny")


# my_decor("sanket")
# my_decor("sunny")

decorefunction("sanket")
decorefunction("sunny")
#-----------#--------------#-------------#-------------#-------------
# ** with out using Decorator

def my_decor(func):
    def wrapper(name):
      if name == "sanket":
          print("hello sanket bad morning")
      else:    
          func(name)
    return wrapper

def wish(name):
    print("hello",name,"good morning")

decorefunction = my_decor(wish) # variable Aliacsing jiske under main my_decor and usme (wish) pass karvaya....
wish("sanket")
wish("durga")

decorefunction("sanket")
decorefunction("sunny")
#-----------#--------------#-------------#-------------#-------------
# Generators
def my_gen():
    yield'A'
    yield'B'
    yield'C'

g = my_gen()
print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
for x in g:
    print(x)
#-----------#--------------#-------------#-------------#-------------
def countdown(num):
    print("start countdown")
    while(num>0):
        yield num
        num=num-1

values = countdown(5)
for x in values:
    print(x)
#-----------#--------------#-------------#-------------#-------------
def firstn(num):
        n=1
        while n<=num:
          yield n
          n=n+1

values = firstn(5)
for x in values:
    print(x)
#-----------#--------------#-------------#-------------#-------------
# Generator wrt performance

import random
import time 

name = ["sanket","sunny","Deepak","priyank"]
subjects = ["python","java","php","Blockchin"]

def people_genrator(num_people):
    for i in range(num_people):
        person={
            "id":i,
            "name":random.choice(name),
           " subjects":random.choice(subjects)
        }
        yield person

t1 = time.perf_counter()
people = people_genrator(10000000)
t2 = time.perf_counter()   

print('Took {:.2f} seconds'.format(t2-t1))        
#-----------#--------------#-------------#-------------#-------------
g=(x*x for x in range(10000000000000000))
print(next(g))













#-----------#--------------#-------------#-------------#-------------






















# revsion
#lamda (arrgumets:expresions)

# my_lambda1 = (lambda n:n*n)
# print = ("the squere of lambda",my_lambda1(10))

# my_lambda_even = lambda n:n%2==0

# print("the even number of lambda",my_lambda_even(102))

# my_lambda = lambda a,b,c:a+b+c
# print("the sum of number is ",my_lambda(10,20,30))


# my_list = [1,2,3,4,5,6,7,8,9,10]

# z = list(map(lambda n:n*n,my_list))

# print(z)
#-----------#--------------#-------------#-------------#-------------

#reduce 

# from functools import reduce

# my_func1 = [1,2,3,4,5,6,7,8,9,10,12,114]

# z = reduce(lambda x,y:x+y,my_func1)

# print(z)
#-----------#--------------#-------------#-------------#-------------






























































# output = {}
# for department in input["company"]["departments"]:
#     for employee in department["employees"]:
#         output[employee["id"]] = employee["name"] 
# print(output) 



# opt= {101:"Alice Smith",}



# {101: 'Alice Smith', 102: 'Bob Johnson', 201: 'Carol Taylor',301: 'Sanket majithiya'}
