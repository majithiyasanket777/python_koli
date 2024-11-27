# Tuple All methods... (count,index)
# immutable (changes Not applicable),orderd, duplicatevalues are allowed,indexing allowed ,slicing allowed hectrogeinous are applicable 

# count kitni baar woh item repeat ho rahi hai...
my_tuple = ("sanket","Deepak","priyank","priyank")

count_number = my_tuple.count("priyank")

print(count_number) # out put:- 2

# index konse index me hai....

colour = ("red","green","yellow","Black","Blue")

index_of_colur = colour.index("Black")

print(index_of_colur)  




# my_tuple = (10,20,30,40,50,60)

# my_tuple [0] =  "sanket"

# print(my_tuple)

#-----------#--------------#-------------#-------------#------------
# type , comma thta consider tuple other wise not
my_tuple = (10,)
print(type(my_tuple))
#-----------#--------------#-------------#-------------#------------
# tuple :- immutable, orderd, indexing, ,slicing, duplicate value allow, hectrogienous value are allow, instruction of preserved words are allow
# set :- mutable, unorderd, unindexing, duplicate are not allow, hectrogienous are allow.... 

#-----------#--------------#-------------#-------------#------------
# start with basics
t =  10,20,30,40
print(type(t))

#-----------#--------------#-------------#-------------#------------

my_list = [10,20,30,40] # convert kar diya isne list se tuple me 
s = tuple(my_list)
print(s)
#-----------#--------------#-------------#-------------#------------

t= tuple(range(10,20,2))
print(t)
#-----------#--------------#-------------#-------------#------------

t= [10,20,30,40,50,60]
print(t[0]) # 10
print(t[-1]) # 60
# print(t[100]) # out of the range 
#-----------#--------------#-------------#-------------#------------
my_tuple = (10,20,30,40,50,60)
print(my_tuple[2:5]) # 30,40,50
print(my_tuple[2:500]) # 30,40,50,60
print(my_tuple[::2])  # 10,30,50

#-----------#--------------#-------------#-------------#------------
# *** We can not Accessing tuple Beacuse it's immutable data type
# my_tuple = (10,20,30)
# my_tuple [2]= 700  # TypeError: 'tuple' object does not support item assignment
# print(my_tuple)
#-----------#--------------#-------------#-------------#------------
# my_tuple =[ 10,20,30]
# my_tuple [2]= 700
# print(my_tuple)
#-----------#--------------#-------------#-------------#------------
# 1. Concatenation Operator(+):

t1 = (10,20,30)
t2 = (40,50,60)  
print(t1+t2)    #out put:- (10, 20, 30, 40, 50, 60)
#-----------#--------------#-------------#-------------#------------
# 2. multiplication oprator 

t = (10,20,30)
print(t*3) # out put:- (10, 20, 30, 10, 20, 30, 10, 20, 30)
#-----------#--------------#-------------#-------------#------------
# revser tuple 3 Diffrent waise
my_tuple = (10,20,30,40,777)
reverse_tuple = sorted(my_tuple,reverse=True)
print(reverse_tuple)

#-----------#--------------#-------------#-------------#------------
# my_tuple = (10,20,30,40)
# revser_tuple = tuple(reversed(my_tuple))
# print(revser_tuple)

#-----------#--------------#-------------#-------------#------------
# my_tuple = (10,20,30,40,55,66)
# revser_tuple = (my_tuple[::-1])
# print(revser_tuple)
#-----------#--------------#-------------#-------------#------------
# max &  min
my_tuple = (10,20,30,40)
print(max(my_tuple))
print(min(my_tuple))
#-----------#--------------#-------------#-------------#------------
a = 1
b = 2
c = 3 
d = 4

my_tuple = (a,b,c,d)
print(my_tuple)
#-----------#--------------#-------------#-------------#------------
t = (10,20,30,40)
a,b,c,d =t   # a=10,b=20,c=30,d=40
print("a=",a,"b=",b,"c=",c,"d=",d)
#-----------#--------------#-------------#-------------#------------
# Tuple comphrhansion not suppoted by in python 

# my_tuple = (input("Enter your number:"))
# my_tuple = [int(n)for n in my_tuple]
# my_tuple1 = (n**2 for n in my_tuple)
# # print(type(my_tuple1))
# for x in my_tuple1:
#     print(x)
#-----------#--------------#-------------#-------------#------------

# my_tuple = (input("Enter your string:"))
# my_tuple = 

# my_tuple1 = input("Enter valid number:")
# my_tuple1 =  [int(s) for s in my_tuple1]
# my_tuple = (n**2 for n in my_tuple1)
# for n in my_tuple:
#     print(n)
# print(type(my_tuple))
#-----------#--------------#-------------#-------------#------------

# write programe tuple sum And Average to this programe 

# t = eval(input("Enter your number:"))
# l = len(t)
# sum = 0
# for n in t:
#     sum=sum+n
#     print("the sum of",sum)
#     print("the sum of average",sum/l)
