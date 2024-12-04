# write a program to postive index and negetive index display a charcter by index wise


# s = input("Enter some string:")
# i = 0 
# for x in s:
#     print("The character present in postive index{},and negetive index is{}".format(i,i -len(s),x))
#     i=i+1


# Accessing string using slicing 



# s="Learning Python is very very easy!!!"

# print(s[1:7:1]) # earnin

# print(s[1:7]) # earnin 

# print(s[1:7:2])# eri

# print(s[:7])#Learnin

# print(s[7:])#g Python is very very easy!!!

# print(s[::])# Learning Python is very very easy!!!

# print(s[:])# Learning Python is very very easy!!!


# print(s[::-1])# ysae ysae yrev yrev si nohtyp gninraeL


# s = "Learinng python is very very easy!!!"
# n = len(s)
# i = 0
# print("forword direction")
# while i<n:
#     print()

# # checking member ship oprator in string 


# # s = "durga"

# # print('d' in s)

# s1 = input('Enter first string:')
# s2 = input("Enter second string:")

# if s1 == s2:
#     print("Both string are equal")
# elif s1<s2:
#     print("First string is less than second string")
# else:
#     print("First sting is greater than second string")

#---------------------#-------------------#---------------------

# city = input("Enter your city:")
# scity = city.strip()
# if scity == "Mumbai" or scity== "mumbai":
#     print("Hello Mumbai!!!")

# elif scity == "Banglor":
#     print("Hello Banglor!!!")

# elif scity == "Rajsthan":
#     print("Hello Rajsthan!!!")
# else:
#     print("you enter invalid city!!!")    

# s = "Learning python is very easy!!!"
# print(s.find("python"))

#---------------------#-------------------#---------------------

# s="durgaravipavanshiva"
# print(s.find('a'))
# print(s.find('a',7,15))
#---------------------#-------------------#---------------------

# s = input("Enter main string:")
# subs = input ("Enter sub strng:")

# try:
#     n=s.index(subs)
# except ValueError:
#     print("Substring not found")
# else:
#     print("Substring is  found")      
#---------------------#-------------------#---------------------
# s = input("Enter main string: ")
# subs = input("Enter substring: ")

# if subs in s:
#     print("Substring is found")
# else:
#     print("Substring is not found")
#---------------------#-------------------#---------------------
# s = input("Enter your strin")    
# subs = input("Enter your substrin")    
# try:
#     n=s.index (subs)
# except:    
#     print("substring")
# #---------------------#-------------------#---------------------
s = "abcabcabcabc"
print(s.count('a'))
#---------------------#-------------------#---------------------
s="Learning python is very difficult"
s1=s.replace("difficult","easy")
print(s1)
#---------------------#-------------------#---------------------
s ="ababababababab"
s1=s.replace("a","b")
print(s1)
#---------------------#-------------------#---------------------
s = "sanket software solution"
l = s.split()
print(l)
#---------------------#-------------------#---------------------
s = "sanket software solution"
l = s.split()
for x in l:
    print(x)
#---------------------#-------------------#---------------------
s = "22-23-24"
l = s.split('-')
for x in l:
    print(x)
#---------------------#-------------------#---------------------
# Join
s = "sanket","majithiya","python"
l = '-'.join(s)
print(l)
#---------------------#-------------------#---------------------

s = "sanket majithiya how are you"
l = s.split()
for x in l:
    print(x)
#---------------------#-------------------#---------------------
s = "sanket","majithiya","howare", "you"
l = "-".join(s)
print(l)
#---------------------#-------------------#---------------------

#---------------------#-------------------#---------------------
s = "Learning python very easy"
print(s.capitalize())
print(s.startswith('learning'))
print(s.endswith('easy'))
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.index('a'))
#---------------------#-------------------#---------------------

# s = input("Enter a number:")
# if s.isalnum():
#     print("its is alpha numaric number")
#     if s.isalpha():
#         print("it is alpha number")
#         if s.lower():
#             print("its is lower case numbers:")
#         else:
#             print('upper case alpha bate')
#     else:
#         print("it is digit") 
# elif s.isspace():
#     print("it is space character")
# else:
#     print("Non space special character")              
              
#---------------------#-------------------#---------------------
name = 'sanket'    
age = 20 
salary = 100000

print("my name is {}, and my age is{} ,and current salary is{} ".format(name,age,salary))
print("my name is {0}, and my age is{1} ,and current salary is{2} ".format(name,age,salary))
print("my name is {x}, and my age is{y} ,and current salary is{z} ".format(z=salary,y=age,x=name))


name = "sanket"
number = 10
print("my name is {:>10}".format(name)) # minimu 10 charter other wise remaing speace are there
print("my name is {:<10}".format(name))
print("my name is {:^10}".format(name)) # center using
print("my name is {:=10}".format(number)) # this is only number aliment are applicable

class person:
    age = 48
    name = "durga"

print("{p.name}'s age is {p.age}'s ".format(p=person()))    


import datetime
date=datetime.datetime.now()
print("this is current month data ,{:%d/%m/%y/ %H:%M:%S}".format(date))

#---------------------#-------------------#---------------------
# s = input('Enter string:')
# print(s[::-1])
#---------------------#-------------------#---------------------
# s = input('Enter string:')
# print(''.join(reversed(s)))
#---------------------#-------------------#---------------------
# Program to reverse order of words.
# s = input("Enter some thing:")
# l = s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# output=' '.join(l1)
# print(output)
#---------------------#-------------------#---------------------
# characters as even position and odd poistion

# s=input("Enter some string:")
# print("Characters at Even postion:",s[0::2])
# print("Characters at Odd postion:",s[1::2])

#---------------------#-------------------#---------------------
numbers = [5,3,5,4,6,2,1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
#---------------------#-------------------#---------------------
# Another wey :-
numbers = [5,3,5,4,6,2,1]
numbers.sort()
print(numbers)
#---------------------#-------------------#---------------------
# s = input("Enter some string:")
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous = x
#     else:
#         output=output+previous*(int(x)-1)
# print(output)            
#---------------------#-------------------#---------------------
# Duplicate character Remove

s = ['A','A','B','B', 'C','C','D','D']
duplicate_remove = sorted(set(s))
print(duplicate_remove)

#---------------------#-------------------#---------------------
print("The intEger number is: {:5d}".format(123))
print("The intEger number is: {:05d}".format(123))
print("The intEger number is: {:06d}".format(123))
#---------------------#-------------------#---------------------
print("The float number is: {:08.3f}".format(1234.5))
print("The float number is: {:08.8f}".format(786786123.45))

#---------------------#-------------------#---------------------

# name = "sanket majithiya prashantbhai" 
# my_string = name.split(" ")
# recorder_name = [(my_string[1]), (my_string[0]), (my_string[2])]
# print(recorder_name)
 #---------------------#-------------------#---------------------

name = "majithiya sanket prashantbhai"
spilt_name = name.split(" ")
recorderd_name = [(spilt_name[0]),(spilt_name[1]),(spilt_name[2])]
print(recorderd_name)
#---------------------#-------------------#---------------------


# name = "sanket  majithiya  prashantbhai"
# # Split the name and filter out any empty strings caused by extra spaces
# split_name = [part for part in name.split(" ") if part]

# # Rearrange the parts as desired
# reordered_name = " ".join([split_name[1], split_name[0], split_name[2]])

# print(reordered_name)

#---------------------#-------------------#---------------------
#      0           1      2   
# prashantbhai sanket majithiya
name = "sanket  majithiya  prashantbhai"
# Split and remove any empty strings due to extra spaces
split_name = name.split()

# Rearrange the parts in the desired order
reordered_name = f"{split_name[2]} {split_name[0]} {split_name[1]}"

print(reordered_name)
#---------------------#-------------------#---------------------
msg = "i want to become python programmer"
words = msg.split()
print(len(words))
print(words)
#---------------------#-------------------#---------------------

counteries_name = "india,pakistan,australia,srilanka,amrica,england"
countrys = counteries_name.split(",",3) # words ko separat kart hai 
for country in countrys:
    print(country)

#-----------#--------------#-------------#-------------#------------
# spilt return  list karega... words ki len count karni ho tab use karenge hum iska 
t = ("sanket-majithiya-who")
my_string = t.split('-')
for x in my_string:
    print(x)  
#-----------#--------------#-------------#-------------#------------ 
# join  2 types out put  # 1st out :- sunny-bunny-tonny
t = ("sunny","bunny","tonny")
my_string = '-'.join(t)
#-----------#--------------#-------------#-------------#------------ 
# 2nd type of out put :- s-u-n-n-y-,-b-u-n-n-y-,-t-o-n-n-y
print(my_string)
t = ("sunny,bunny,tonny") # string me all words ko diya hai double quotes
my_string = '-'.join(t)
print(my_string)
#-----------#--------------#-------------#-------------#------------ 
# s = input("Ente r your charcters:")
# print(" your  Even characters:",s[::2])
# print(" your  odd characters:",s[1::2])
#-----------#--------------#-------------#-------------#------------ 

# ubicode ---> 63 A
# character --> a-->93
#-----------#--------------#-------------#-------------#------------ 
# s = input("Enter some string:")
# output =''
# for char in s:
#     if char.isalpha():
#         output=output+char
#         previous= char
#     else:
#         output=output+previous*(int(char)-1) 
# print(output)           
#---------------------#-------------------#---------------------
# s = input("Enter some string:")
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous = x
#     else:
#         output=output+previous*(int(x)-1)
# print(output) 
# ---------------------#-------------------#---------------------
# s = input("Enter the String:")
# l = []
# for x in s:
#     if x not in l:
#         l.append(x)
# output="".join(l)
# print(output)         
#---------------------#-------------------#---------------------
# s = input("Enter your numbers:")
# s1 = "".join(set(s))
# print(s1)
#---------------------#-------------------#---------------------
# my_string = (input("Enter your string:"))
# l = []
# for x in my_string:
#     if x not in l:
#         l.append(x)
# output="".join(l)
# print(output)        
#---------------------#-------------------#---------------------
# s = input("Enter your string:")
# l = []
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# for ch in sorted(l):
#        print("{} occurs {} time".format(ch,s.count(ch)))      
#---------------------#-------------------#---------------------
# Replacing the string 

s = "Learning the python is very Deficault"
s1 = s.replace("Deficault","Very Easy")
print(s1)
#---------------------#-------------------#---------------------
"""Note :-  
print("Binary Form:{0:b}".format(153))
print("Octal Form:{0:o}".format(153))
print("Hexa decimal Form:{0:x}".format(154))
print("Hexa decimal Form:{0:X}".format(154))
Output:
Binary Form:10011001
Octal Form:231
Hexa decimal Form:9a
Hexa decimal Form:9A
Note: We can represent only int values in binary, octal and hexadecimal and it is not possible for
float values.

Note:- Case 2 Number formating in string :-
Formatting Numbers
d--->Decimal IntEger
f----->Fixed point number(float).The default precision is 6
b-->Binary format
o--->Octal Format
x-->Hexa Decimal Format(Lower case)
X-->Hexa Decimal Format(Upper case)

While displaying positive numbers,if we want to include + then we have to write
{:+d} and {:+f}

Note :- string accessing me woh key nahi hai or Access karte hai to out put None aayega
d = {}
print(d.get('A'))  # Returns None
print(d.get('B'))  # Returns None
"""





