# A group of functions,variables and classes saved to file,which is nothing but Module.

# Every python file (.py) acts as a module.

# Note :- whenever we are using a module in our program, for that module compiled file will be generated and stored in the hard disk permanently.
#---------------------#-------------------#---------------------

# print(help("modules")) :- isse all module ki list milegi haamre system kiii :- isse aap pata sakte ho ye  module system me available hai ki nahi 
#---------------------#-------------------#---------------------
# 1st example 
# import sanketModules
# print(sanketModules)
# sanketModules.add(10,20)
# sanketModules.product(10,20)
#---------------------#-------------------#---------------------
""" using from directly (Not using import Directly)
from sanketModules import *
add(10,20)
product(10,20)   
"""
#---------------------#-------------------#---------------------
# 2nd example 
# import sanketModules
# print(sanketModules)
# l = list(map(lambda x:x*2,sanketModules.my_list))

# print(l)
#---------------------#-------------------#---------------------
# member aliasing: (as)

from sanketModules import x as y,add as sum
print(y)
# print(x) # NameError: name 'x' is not defined beacuse humne x ko as y me change kar diya  uper
sum(10,20)

# Note :- Once we defined as alias name,we should use alias name only and we should not use original name
#---------------------#-------------------#---------------------
# import sanketModules
# print(dir(sanketModules))
# print(__file__) # /home/vijay/Templates/Practice/Modules.py
#---------------------#-------------------#---------------------
# Reloading module :- by default call karunga to ek hi baar print hoga lekin ,me do baar module  ko import karu to woh 2 baar run hona chahiye iske liye hum iska use karte hai... 

# import importlib
# import sanketModules

# importlib.reload(sanketModules) # out-put:-  # hello world ,hello world

#---------------------#-------------------#---------------------
# Random
from random import *

# for i in range(10):
#     print(random())
# #---------------------#-------------------#---------------------
# # Date And Time
# from datetime import *

# current_date = datetime.now().date()
# print("current data:",current_date)

# current_time = datetime.now().time()
# print("current data:",current_time) 
# #---------------------#-------------------#---------------------
# # Randint()function: #  Always genrat int numbers (isko dedo range and woh numbers jika aapko int number chahiye )

# for i in range(10):
#     print(randint(1,1000))
# #---------------------#-------------------#---------------------
# # uniform():- return random float values  between 2 given numbers

# from random import *

# for i in range(10):
#     print(uniform(1,10))
#---------------------#-------------------#---------------------
# randrange # random numbers genrate kar ke dega range me hume 

for i in range(10):
    print(randrange(10))

for i in range(10):
    print(randrange(1,10)) # 0 ko nahi lega 1 se start hoga  
#---------------------#-------------------#---------------------
# choice() # ye return karega random numbers ko or objects from given list or tuple

my_list = ["sanket","sunny","vivek","vinny","chinny"]
for i in range(10):
    print(choice(my_list))
#---------------------#-------------------#---------------------

# pakages 

"""
it's a collection of module files
- __init__.py that consider python pakage .This file can be empty
- pakage can contain sub pakage als

The main Advantages of pakage statemnets
- we can resolve naming conflicts
- we can indentify our components uniquely
- improve modularity of the application
"""




#---------------------#-------------------#---------------------
# revsion
# random nmbers

# from random import *
# random  number
# for i in range(12):
#     print(random())

#  only int
# for i in range(14):
#     print(randint(1,100))

# float value
# for i in range(10):
#     print(uniform(1,10))



# from datetime import *


# my_time = datetime.now().time()
# print("current time ",my_time)

# my_time = datetime.now().date()
# print("current date ",my_time)
