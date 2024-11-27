#---------------------#-------------------#---------------------
x = 888

def add(a,b):
    print("The sum:",a+b)

def product(a,b):
    print("The Product:",a*b)    
#---------------------#-------------------#---------------------
# 2 second example que
# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#---------------------#-------------------#---------------------
# dir() function :- To list out all members of current module..
# x = 10 
# y = 30

# def f1():
#     print("Hello")
#     print(dir()) # To print all member to current module  
#     print(f1.frexp)
#---------------------#-------------------#---------------------
# x = 100
# my_name = "sanket"
# print(type(my_name))
# print(dir(my_name))
# print(my_name.startswith("sa")) # True
#---------------------#-------------------#---------------------

#---------------------#-------------------#---------------------

"""
use dir() :-For every module at the time of execution Python interpreter will add some special
properties  automatically for internal use.
Based on our requirement we can access these properties  also in our programe. 

print(__builtins__)
print(__cached__)
""" 
#---------------------#-------------------#---------------------
# special varable __name__ :- 
# def f1():
#     if __name__ == '__main__':
#         print("code to be executed")
#     else:   
#         print("code to be executed as module from some other program")
# f1()        
#---------------------#-------------------#---------------------
# math module 

# from math import *
import math
print (dir(math))
"""
['__doc__' ,'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
"""

# print(sqrt(4))
# print(ceil(10))
# print(floor(10))
# print(fabs(10))
# print(fabs(-10))
