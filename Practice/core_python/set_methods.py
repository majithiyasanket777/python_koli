# set (add, frozen set)

# unorderd,unindex, duplicate value not Allowed, mutable ,hectrogenious are allowed,growable

# Empty set 

s = set()
print(type(s))


# frozen set :-/ We can not Add or Remove Eliments because This  is a immutable in nature...

s1 = {10,20,30,40,50}
f = frozenset(s1)
print(type(f))

# Empty Dectionary 

s = {}
print(type(s))


# Binary to decimal,oct,hex,bin

# binary :- 0 & 1  :- 0b & 0B
# decimal :- 0 to 9 digits not start on 0
# octal   :- 0 to 7 
# hexa :- 0 to 9 and a - f total 16 digits 

print(oct(13))
print(hex(13))

print(bin(13))

# convert to int
print(int(0o15))

print(int(0xd))

print(int(0b1101))

result = int(False)
print(result)
print(type(result))

#-----------#--------------#-------------#-------------#------------
# s = {10,20,30,40}
# l = type(s)
# print(l)
#-----------#--------------#-------------#-------------#------------
s = [10,20,30,40]
l = set(s)
print(type(l))
print(l)
#-----------#--------------#-------------#-------------#------------
s = set(range(10))
print(s)  # out put:- {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 
#-----------#--------------#-------------#-------------#------------
s = {}
print(type(s))  # <class 'dict'> Beacause Empty set are always consider <dict>
#-----------#--------------#-------------#-------------#------------
# add
my_set = {10,20,30,40}
my_set.add(50)
print(my_set)
#-----------#--------------#-------------#-------------#------------
# updte
my={10,20,30,40}
my_set = {50,60,70,80}
my.update(my_set)
print(my)
#-----------#--------------#-------------#-------------#------------
# copy  # New object will be created copy(new clone genrated)
s = {10,20,30,40}
s1 = s.copy()
print(s1)
#-----------#--------------#-------------#-------------#------------
# pop
my_set = {101,202,303,404}
my_set1 = my_set.pop()
print(my_set)
print(my_set1)
#-----------#--------------#-------------#-------------#------------
# remove
my_set = {10,20,30,40}
my_set.remove(30) 
print(my_set) # out put:- {40, 10, 20}
#-----------#--------------#-------------#-------------#------------
# clear
my_set = {10,20,30}
my_set.clear()
print(my_set)  # out put:- set()
#-----------#--------------#-------------#-------------#------------
# union # return all elment present both sets

x = {10,20,30,40}
y = {50,60,70,80}
print(x.union(y))
print(x|y)
#-----------#--------------#-------------#-------------#------------
# intersection()  # Return both elimets in set 
x = {10,20,30,40} 
y = {30,40,50,60}

print(x.intersection(y)) # {30,40}
print(x&y) # {10,20}

#-----------#--------------#-------------#-------------#------------
# Diffrence() x me hai but y me nahi to woh return karega elimets ko
x = {10,20,30,40}  
y = {30,40,50,60}

print(x.difference(y)) # {10,20}
print(y.difference(x)) # {50,60} 
#-----------#--------------#-------------#-------------#------------
# symmetric_difference(): either(x) or either(y) but not in both() simple dono me same hoga to woh return nahi karega
x = {10,20,30,40}
y = {50,20,40,60,70,80}
print(x.symmetric_difference(y)) # 10,30,50,60,70,80
print(x^y)
#-----------#--------------#-------------#-------------#------------
# set comprehension():-

# squere in set 

#-----------#--------------#-------------#-------------#------------
#  even number
# my_set = str(input("Enter your number:"))
# my_set1 = {int(x) for x in my_set if int(x)%2==0} 
# print(my_set1)

#-----------#--------------#-------------#-------------#------------
# even numbers on set Simple wey
 
# my_set = int(input("Enter your number:"))
# my_set1 = {int(x) for x in my_set if x.isdigit() and int(x)%2==0}
# print(my_set1)

#-----------#--------------#-------------#-------------#------------
# my_set = int(input("Enter your number:")) # 12345
# my_set1 = {int(x)**2 for x in my_set}
# print(my_set1) # :- out put :- {1, 4, 9, 16, 25}
#-----------#--------------#-------------#-------------#------------
# Dynamic **
# even numbers in set 
# my_set = int(input("Enter your number:"))
# my_set1 = { x for x in  range(1,my_set,+ 1) if x% 2 == 0}
# print(my_set1) 
#-----------#--------------#-------------#-------------#------------
# Squer of set dynamic

# my_squer = int(input("Enter your number:"))
# my_sqe_numbers = {x**2 for x in range(1,my_squer,+1)}
# print(my_sqe_numbers)

#-----------#--------------#-------------#-------------#------------
# # vowels
# w = input("Enter your vowles:")
# s=set(w)
# v={'a','e','i','o','u'}
# d = s.intersection(v)
# print("The diffrent vowels in ",w,"are",d)
#-----------#--------------#-------------#-------------#------------
# frozen set Example:- 
# my_set = {10,20,30,40}
# my_set.add(my_set)
# my_frozen = frozenset(my_set)
# my_frozen.add(50) # error aayega kyuki ye unmutable hai out :- AttributeError: 'frozenset' object has no attribute 'add'
# print(type(my_frozen))
#-----------#--------------#-------------#-------------#------------

""" 
Diffrence Tuple And Frozen set :- Both are immutable but
Tuple :- order applicable, Duplicate are allowed, index slice applicable 

Frozen set :- order Not applicable,Duplicate are Not allowed, index slice Not applicable 

"""

 































"""
# binary :-   0 & 1 
decimal :-    1 to 9 Not start with 0
octa :-       0 to 7 
hexa :-       0 to 9 and a-f total 16 digits


complex data type :- 

real and  imgaenary 
Imagenary part only decimal allowd  and hexa,octa,bin not allowd
eg:- 1.2222 


"""