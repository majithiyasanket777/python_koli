# try -execpt handling block
print("stm-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("stm-3")        
#-----------#--------------#-------------#-------------#--------------
try:
    print(10/0)
except ZeroDivisionError as f:
    print("execption rasied and its description is:",f)

#-----------#--------------#-------------#-------------#--------------
# Eg:- 1
# num1 = int(input("Enter your first number:"))
# num2 = int(input("Enter your second number:"))
# try:
#     division_num = num1/num2
#     print(division_num)    
# except (ZeroDivisionError):
#     print("divide by zero not possible not allow")

#-----------#--------------#-------------#-------------#--------------
# 2 type
# num1 = int(input("Enter your first number:"))
# num2 = int(input("Enter your second number:"))
# try:
#     division_num = num1/num2
#     print(div)    
# except (ZeroDivisionError,NameError) as obj: # is trah bhi likh sakte ho(error nahi dega name)
#     print(obj)
#-----------#--------------#-------------#-------------#--------------
# num1 = int(input("Enter your  first number:"))
# num2 = int(input("Enter your second number:"))

# try:    
#     num_divsion = num1/num2
#     print(num_divsion)
# except ZeroDivisionError:
#     print("divide by zero not possible, not allow")    

# try:
#    print(10/0)
# except (ZeroDivisionError,NameError) as msg:
#     print("exeption rasise and descrpition",msg)

#-----------#--------------#-------------#-------------#--------------
# value errror example also add 

# try: 
#     num1 = int(input('Enter your  first number:'))
#     num2 = int(input("Enter your second number:"))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("not divide by zero,not allow")
# except ValueError:
#     print("pleas enter int value")

#-----------#--------------#-------------#-------------#--------------
# Single except block that can handle multiple exceptions:
# try: 
#     num1 = int(input('Enter your  first number:'))
#     num2 = int(input("Enter your second number:"))
#     print(num1/num2)
# except (ZeroDivisionError,ValueError) as msg:
#     print("not divide by zero,not allow",msg)
#-----------#--------------#-------------#-------------#--------------
# finally :- always executed 
"""
try:
    Risky Code
except:
    Handling Code
finally:
    Cleanup code
"""

"""
try:
    Risky code or operation
except:
    error message will be executed inside try
else:
    Ager try block me  execpertion nahi hoga to else execute hoga or
    success_logic() bhi likh sakte hai
finally:
    Always executed            
"""
#-----------#--------------#-------------#-------------#--------------
# Nested try-except-finally blocks:
try:
    print("outer try block")
    try:
        print("inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("inner execept block") 
    finally:
        print("inner finally block")
except:
    print("outer finally")
finally:
    print("outer finally block")                   

"""
out put:- Ager inner block handle nahi kar paayega tabh hi outer except block me jaayega tab hi woh responsibal hoga handle karne 
warna inner se except se handle hogaya to woh Nahi jaayega outer block me.

outer try block
inner try block
inner execept block
inner finally block
outer finally block
"""
# revision

# num1 = int(input("Enter your first number:"))
# num2 = int(input("Enter your second number:"))

# try:
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Not allowed zerodivison error")
# else:
#     print("succefully run")
# finally:
#     print("Thanks for using App")            

# loging  # isme apko leveles set karne padte hai level 30 so uske baad ke aayenge

import logging 
logging.basicConfig(filename='app.log',
                    level=30,
                    filemode='w',
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s - Process: %(process)s - Line: %(lineno)d",
                    datefmt='%d-%b-%Y %H:%M:%S') #changing the level
logging.debug("this is a debug message my sql 3 sath connect kiya hai username sanket_majithiya password 777") #10
logging.info("my loging module will exected and my cart and check out will also executed") #20
logging.warning("you Not usinging  only capital words and special symbol as passwords")#30
logging.error("the error is variable not found")#40
logging.critical("your data base not connect so your app not work propley")#50
logging.exception("zerodivsion error you can not divide by zero and value are only use int as objects")#60

"""
warning
Error
critical

process id :- requried for debuging
line number :- lin number__ log huva hai...
"""


# import loging 
"""
loging.basicconfig (filename='log.txt, level = 30)
isse hum haamri aplicton me error yaa kuch aaye execption unexpected so debbuding me strore kiya hai hamar informatio
uski help se hum handle kar sake
"""

# Python Program to write exception information to the log file

# import logging
# logging.basicConfig(filename='app.txt',level=20)
# logging.info("A New request came:")
# try:
#     x = int(input("Enter your  First number:"))
#     y = int(input("Enter your  second number:"))
#     print(x/y)
# except ZeroDivisionError:
#     print("can not divide by zero:")
#     logging.exception(msg="can no possible this unavailbe!!!")
# except ValueError as msg:
#     print("Enter only int values") 
#     logging.exception(msg)
#     logging.info("Request processing completed")       
# else:
#     logging.info("The opration was successful")


"""
New Topic :- 
# 1. Debugging Python Program by using assert keyword:
"""
# Eg:- 
def squarelt(x):
    return x**x

assert squarelt(2)    
assert squarelt(3)    
assert squarelt(4)   

print(squarelt(2))
print(squarelt(3))
print(squarelt(4))

