# List methods  Append,Extends,count,update,clear,copy,delete  
# list is :-  orderd , hatrogenious (diffrent type of object allow like :- int,float,dict) duplicate values are allow, [],list is growable in nature,mutable
# beacuse  1 this is mutable so usme collection of elemnt add kar sakte hai 

# why list is order :- beacuse indexing slicing are applicable And second Answer or :- list me hum multiple datatypes ki values daal sakte hai like int,float,dict 
# insertion order is preserved :- hume jis form me data dala tha ussi form me hume
# if you represent group values as single entity so we are using list:-
#---------------------#-------------------#---------------------
s = {10}
print(type(s))   # set 

s1 = {} 
print(type(s1))  # Empty dict

s3 = () 
s4 = set(s3)
print (type(s4))  # Empty set 

s2 = () 
print(type(s2)) # Empty tuple
#---------------------#-------------------#---------------------
# Append 
# my_list  = ["sanket","Vijay","Rohit"]
# my_list.append("sahil")
# print(my_list)

#---------------------#-------------------#---------------------
# Extend 
# my_fruite = ["Apple","banna","Kiwi"]
# more_fruite = ["orange","mango","pinaple"]

# my_fruite.extend(more_fruite)
# print(my_fruite)
#---------------------#-------------------#---------------------
# Count 

# my_list = ["Apple","Banna","kiwi","Apple","Kiwi"]
# count_list = my_list.count("Apple")
# print(count_list)
#---------------------#-------------------#---------------------
# List Accessing 
# my_list = ["apple","Mango","Banna","Kiwi"]
# print(my_list[0])
#---------------------#-------------------#---------------------
# List Compharsion method
# n = [n for n in range(1,101)]
# print(n)

# l = []
# l.append(10)
# l.append(20)
# print(l)
#---------------------#-------------------#---------------------
# Nested list :- list ke under list 

# sanket = [['sanket',50],['kiran',60],['vivek',90]]
# print(sanket)

# list is mutable instartion of order is presverd,duplicate values are allow, groable, [], hectrogeniuos 

# Group of elients add in single entity 

# Nested Accesiing list :- 

# list1 = [['sanket',50],['vivek',60],['aman',70]]
# list1  [0] = ['Nayan',60]
# print(list1)
#---------------------#-------------------#---------------------

# Accessing the list 

# list1 = ['sanket',30,50,90]
# list1 [0] = 1
# print(list1)

# Linked List in Python 🐍 with Easiest Explanation & Execution

# my_list = list(range(0,10,2))
# print(my_list)
# print(type(my_list))

#---------------------#-------------------#---------------------

# To only display only even numbers 
s = [x for x in range(1,11) if x %2==0]
print(s)

n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])  # 3,5,7
print(n[4::2])  # 5,7,9
print(n[3:7])   # 4,5,6,7
print(n[8:2:-2]) # 9,7,5
print(n[4:100]) # 5,6,7,8,9,10

#---------------------#-------------------#---------------------
# Accessing list
n = [10,20,30,40]
n[1]=[777]
print(n)
#---------------------#-------------------#---------------------

# Element at index 

my_list = ["A","B","C","D","E","F"]

for i in range(len(my_list)):
    print(f"Elements at index{i}:{my_list[i]}")
#---------------------#-------------------#---------------------
n = [1,1,2,2,2,2,3,3,3]
print(n.count(1))
print(n.count(2))
print(n.count(3))
#---------------------#-------------------#---------------------
# index 

n = [10,20,30,40,50,60,70,80]
print(n.index(10))
print(n.index(20))
print(n.index(30))
print(n.index(40))
print(n.index(50))
print(n.index(60))
print(n.index(70))
print(n.index(80))
#---------------------#-------------------#---------------------
# insert 
n = [10,20,30,40,50]
n.insert(5,60)
n.insert(-6,60)
print(n)
#---------------------#-------------------#---------------------
# Extend 

my_list = ["Apple","Banna","Kiwi"]
my_list.extend("Banna")
print(my_list) #  ['Apple', 'Banna', 'Kiwi', 'B', 'a', 'n', 'n', 'a']
#---------------------#-------------------#---------------------
# remove 
my_list = [10,20,30,40,50]
my_list.remove(30)  # isme partiular woh eliment
print(my_list)
#---------------------#-------------------#---------------------                                               
# pop

my_list = [10,20,30,40,50]
my_list.pop(3)                # isme index daal na padta hai konsa index remove karna hai warna last Eliment remove karega..
print(my_list)

# append End of the eliment add hoga 
# extend Last me 
#---------------------#-------------------#---------------------                                               

n = [10,20,30,40]
n.reverse()
print(n)

#---------------------#-------------------#---------------------                                               
# Another wey

n = [10,20,30,40,50]
reverse_list = n[::-1]
print(reverse_list)
#---------------------#-------------------#---------------------                                               

# Sorting to the list Note :- sorting me only str yaa numbers hi lega mix nahi lega Typeerror solve:-(key=str)

my_list = [90,"A",80,"B",40,"C"]
my_list.sort(key=str)
print(my_list)

#---------------------#-------------------#---------------------  
# sorting in reverse in natue               
my_list = [40, 30, 20, 10]
my_list.sort(reverse=False)
print(my_list)
#---------------------#-------------------#---------------------  

x = [10,20,30,40,50]
y = x
y  [0]=[777]
print(x)
print(y)
print(id(x)) 
print(id(y)) 
#---------------------#-------------------#---------------------  
my_list = [10,20,30,40,50]
my_list [3]=[777]
print(my_list)
#---------------------#-------------------#---------------------  
# concatination list
a = [10,20,30]
b = [40,50,60]
my_list = a+b
print(my_list)
#---------------------#-------------------#---------------------  
# Repetition Operator(*) 

my_list = [10,20,30]
y = my_list*3
print(y) # [10, 20, 30, 10, 20, 30, 10, 20, 30]
#---------------------#-------------------#---------------------  

# Comparing List objects

x = ["Dog","Elephant","Miow"] 
y = ["Dog","Elephant","Miow"] 
z = ["DOG","ELEPHANT","MIOW"]

print(x==y) # True
print(y==z) # False 
print(y!=z) # True 
#---------------------#-------------------#---------------------
# Nested list using by list in matrix

my_list = [[10,20,30],[40,50,60],[70,80,90]]
for i in my_list:
    print("Row wise:",i)
for i in range(len(my_list)):
    for j in range(len(my_list[i])): 
        print(f"matrix-wise: {my_list[i][j]}")
#---------------------#-------------------#---------------------  
# List comprehensions [expression for item in list if condition]

# Even number use list comprehensions
n = [x for x in range(11) if x%2==0] 
print(n)
# Odd number use list comprehensions
n = [x for x in range(11)if x%2!=0]
print(n)

#---------------------#-------------------#---------------------  

# Dynamic **
# even numbers in List comprehensions
my_list = int(input("Enter your number:"))
my_list1 = [x for x in range(1,my_list,+1) if x %2==0 ]
print(my_list1)
#---------------------#-------------------#---------------------  
# Dynamic **
# List compharsion with squere numbers

my_list = int(input("Enter your number:"))
my_list_squere = [x**2 for x in range(1,my_list,+1) ]
print(my_list_squere)


#---------------------#-------------------#---------------------  
# multiplication number use list comprehensions

n = [x*2 for x in range(1,10)]
print(n)
#---------------------#-------------------#---------------------  
# multiplication number of power use list comprehensions

n = [x**2 for x in range(1,11)]
print(n)
#---------------------#-------------------#---------------------  

words = ["sanket","Nag","Venkatesh","sammer"]
l = [w[0] for w in words]
print(l)
#---------------------#-------------------#---------------------  
words = "the quick brown fox jumps over the lazy dog".split()
print(words)
l = [[w.upper(), len(w)] for w in words]
print(l)
#---------------------#-------------------#---------------------  
# vowels = 'a','e','i','o','u'
# words = input("Enter your vowels:")
# found = []
# for letter in words:
#     if letter in vowels:
#         if letter  not in found:
#             found.append (letter)
# print(found)
# print("The number is diffrent found,{words},"is",{found}")
# print("The number of different vowels present in",words,"is",len(found))
    
# my_list = ['',2,3,4]

# my_list = [n*n for n in my_list]
# print(my_list)    

my_string = "majithiya  sanket  prashant"
words = my_string.split()
revsetse_words = " ".join([words[1],words[0] ,words[2]])
print(revsetse_words)

#---------------------#-------------------#---------------------  


#---------------------#-------------------#---------------------  

