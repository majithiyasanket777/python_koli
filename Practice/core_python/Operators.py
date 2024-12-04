# Arrthmetic Opearator
a = 10
b = 2

print('a+b =',a +  b) 
print('a-b =',a -  b)
print('a*b =', a * b)
print('a/b =',a /  b)
print('a//b =',a // b)
print('a%b =', a % b)
print('a**b =',a ** b)

print( a % b )

# Relational Oparators 

a = 10
b = 20

print(a<b)
print(a<=b)
print(a>b)
print(a>=b)

"""
aasic values 

a = 97
b = 98 
c = 99  

A = 65
B = 66 
C = 67

"""
# str also we using this 

a = 'a'  
b = 'c'

print(a<b) # True
print(a<=b) # True
print(a>b) # False
print(a>=b) # False

#------------#----------#---------#------------
# a = "sanket"
# b = "ravi"

# print(a<b) # False
# print(a<=b) # False
# print(a>b) # True
# print(a>=b) # True 



# a = "Deepak"
# b = "ravi"

# print(a<b) # True
# print(a<=b) # True
# print(a>b) # Flase
# print(a>=b) # Flase 


# print(ord('D')) # 68

# print(ord('r')) # 114


# print(True>False)

# print(True>True)  #  False 
# print(True>False) # True
# print(True<False) #  False
# print(True<True)  # False

# Relationl opparators / comparison Operators

# x = int(input("Enter the First number: ")) 
# y = int(input("Enter the second number: ")) 

# if x < y:
#     print("First Number is less than second number")
# else:
#     print(" First Number  is Not less than second Number")


# print(10<20)
# print(10<20<30)
# print(10<20<30<40)
# print(10<20<30<40>50)    


# print(('10' < '20')>'30')
# print(True >'30')

'Equality operators:-'

# 10 == 20 
# 10 != 20
 
print('sanket' == 'durga') # F
print('sanket' != 'durga') # T
print('durga'  == 10)  #  F
print('durg' != 'ravi') #  T
print(False == False) #  T
print(True != False) #  T

a=10
b=2 
print('a+b=',a+b)  # 12 
print('a-b=',a-b)  # 8
print('a*b=',a*b)  # 20 
print('a/b=',a/b)  # 5.0
print('a//b=',a//b) # 5
print('a%b=',a%b) # 0 
print('a**b=',a**b) # 100     (Times hai ye B ka 10*2 2 TIMES power)

print(10==10==10==10==10==10)
print(10==20==30==40==50==60)

"""  
Identitye Operator :-

is Operator 
is Not operator
"""
a = [10,20,30,40]
b = [10,20,30,40]

# print(a == b)
print(a is b) # False
print(a == b ) # True
print(a != b) # False
print(a is not b) # True
print(id(a),id(b))
 
 

# == :- operator is always meant for content comparsion  
# is :-  operator is always meant for reference comparsion

# x and y :- if x is False than return x and True so return y 


# x or y :-  if x is true return x and False so return y



# name = (input("Enter your name:"))

# password = (input("Enter your password:"))

# if name == 'durga' and password == 'sanket':
#     print('valid user')

# else:
#     print("Invalid user")    


# Ternory Oprator:-  if condtion True than first value be considerd else second value will be considerd 

# a = int(input("Enter your First Number: "))

# b = int(input("Enter your second number: "))

# c = int(input("Enetr the therd number: ")) 

# if a < b:
#     min = a
# else:
#     min = b 
# print("minimum value:",min)    

# if a < b and a < c:
#     min = a 
# elif b < c:
#     min = b
# else:
#     min = c 
# print("minimum value:", min)

 
# Q. for minimum 3 numbers  


# Identity operators :- 

# Membership opperators 
# in , Not in 
# x = "hello learning python very easy!!!"

# print('h' in x ) # True
# print('d' in x) # False
# print('d' not in x) # True
# print('python' in x) # True

import math 

degree = 10

print(math.sqrt)
print(math.pi)
print(math.radians(degree))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))


# from math import pi

# r = 16 
 
# print("Area of circle is:", pi*r**2)



# x = int(input("Enter the first number:"))
# y = int(input("Enter the second number:"))

# print("The sum:",x+y)



# a,b = [int(x)for x in input("Enter 2 numbers:").split()]

# print("The sum is:",a*b) 

# onther wey

# a = (int(input("Enter  the first number:")))

# b = (int(input("Enter  the secondest number:")))

# print("The sum of number",a*b) 


# a = float(input("Enter the first  float number:"))
# b = float(input("Enter the second float number:"))
# c = float(input("Enter the thired float number:"))

# print("The sum is:", a+b+c)


# I = eval(input("Enter list"))
# print(type(I))
# print(I)


print("5"+"3")  
print(5+3)
print(5+9)
print(5+10)