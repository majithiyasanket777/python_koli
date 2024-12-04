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
#---------------------#-------------------#-----------------------

my_list = list(range(0,10,2))
print(my_list)
print (type (my_list))

#---------------------#-------------------#-----------------------# 
my_string =  "majithiya sanket prashantbhai"
words =  my_string.split()
joing_string = " ".join([words[0],words[1],words[2]])
print(joing_string)
#---------------------#-------------------#-----------------------# 
my_list = list(range(1,11))
print(my_list)
#---------------------#-------------------#-----------------------# 
my_list = [1,2,3,4,5,6,7,8]
my_fruites = [9,10,11,12,13,14,15]
my_list.extend(my_fruites)
print(my_list)
#---------------------#-------------------#-----------------------# 
my_list = "majithiya sanket prashantbhai"
words = my_list.split()
my_words = " ".join([words[1],words[0],words[2]])
print(my_words)
#---------------------#-------------------#-----------------------# 

# display elemnt in index wise 

my_l = ["A","B","C","D","E","F","G"]

for i in range(len(my_l)):
    print(f"Elemet at index {i}:{my_l[i]}")

# print(f"Element at Index :{l[0]}")
# print(f"Element at Index :{l[1]}")
# print(f"Element at Index :{l[2]}")


# this wey i will beacame change the index  


# even number
# my_set = str(input("Enter your number:"))
# my_set1 = {int(x) for x in my_set if int(x)%2==0} 
# print(my_set1)


# my_set = input("Enter your Even number:")
# my_set1 = {x for x in my_set if int(x)%2==0}
# print(my_set1)

# my_dict = eval(input("Enter your string (e.g., {'a': 10, 'b': 20})"))
# my_dict1 = sum(my_dict.values)
# print("Sum= ",s)
# print(my_dict1)


# from keys default value should be 20,20,20
books = {"python","java","Php"}
price  = 20
my_dict = dict.fromkeys(books,price)
print(my_dict)


# get 

my_dict1 = my_dict.get(500,"sammer")
print(my_dict1)


# my_dict = {100:"sanket",200:"vivek"}
# my_dict1 = my_dict.get(200,"sammer")
# my_dict1 = my_dict.get(400,"sammer")





























