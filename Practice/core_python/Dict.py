# dict all methods (get,key,values,from-keys,pop,popitem,setdefault) key value pair key is mutable and value is unmutable


# from keys 
my_dict = {"key":"Fruite","values":"Apple"}

default_dict = my_dict.fromkeys(my_dict,"unknow")

print(default_dict)

# get 
my_dict = {"Apple":"Fruite","values":"banna"}
print(my_dict.get("Apple"))
print(my_dict.get("kiwi",18))


# popitem remove last eliment end of the list 

my_dict = {"key":"apple","values":"banna"}

remove_dict = my_dict.popitem()


print(remove_dict)


# Dictionary Loops
# x = {"type":"Fruite","name":"Apple"}
# for y in x.values():
#     print(y)

# Dictionary :- mutable, unorderd, un indexing, duplicate values are Not allowed

# i can same name key so new updated values bee add
dict = {"sanket":30,"Vivek":60}
dict ["sanket"] = 777
print(dict)

#  Dict Accessing indexing  se add karna hai 

my_dict = {"Aman":30,"Vivek":60,"priyank":90}
my_dict ["SANKET"] =100
print(my_dict)


# list :- mutable , orderd ,indexing,slicing are allow, duplicate values are allow,hectrogienous objects are allow []

# tuple :- immutable, orderd , indexing ,slicing, duplicate values are allow, hectrogienous are allow ()

# set :- mutabl, unorderd,unindexing, duplicate value are not allow, hectrogienous are allow {}

# Dict :- mutable, unorderd,unindexing, dupplicate keys are not allow but values can be allow 

# instraction orderd is not preserved means jiss karam me dale uss karm me nahi milegi hume values kese bhi aa sakti hai...

# what types of python data types are allowed as key (Ans):- immutable all data types use as key like :-Tuple,string 


s = "sanket\nmajithiya"
print(s)


s = "sanket\majithiya"
print(s)

# s = "This is\"symbol"
# print(s)

#-----------#--------------#-------------#-------------#------------
# start programe :

# my_dict = {100:"sanket",200:"durga",300:"vivek"}
# print (my_dict)
# my_dict [400] ="Deepak" # New dict add 
# print(my_dict)
# my_dict [100]="sammer" # updated dictinary well be added 
# print(my_dict)

#-----------#--------------#-------------#-------------#------------
# delete this key
# my_dict = {100:"sanket",200:"durga",300:"vivek"}
# del my_dict [100]
# print(my_dict)
#-----------#--------------#-------------#-------------#------------
# clear :- se all dictionary will be clear 
my_dict = {100:"sanket",200:"vivek"}
my_dict.clear()
print(my_dict) 
#-----------#--------------#-------------#-------------#------------
# Get # perticular me key se value Dekh sakta hu konsi hai  (usko key doo jiski values jaan ni hai woh apko value dega )

my_dict = {100:"sanket",200:"vivek"}
my_dict1 = my_dict.get(200,"sammer")
my_dict1 = my_dict.get(400,"sammer")
print(my_dict1) # out :- Vivek key se value Access kar sakta hu
#-----------#--------------#-------------#-------------#------------
# pop() only key  will be Removing 
my_dict = {100:"sanket",200:"vivek",300:"sammer"}
my_dict.pop(100)
print(my_dict) # out:- {200: 'vivek', 300: 'sammer'}
#-----------#--------------#-------------#-------------#------------
# popitem() # No Argumets are required
my_dict = {100:"sanket",200:"vivek",300:"sammer"}
my_dict.popitem()
print(my_dict) 
#-----------#--------------#-------------#-------------#------------
# keys:- sari key mujhe mlegi 

my_dict = {400:"sanket",200:"majithiya",300:"deepak"}
keys=my_dict.keys()
print(keys)
#-----------#--------------#-------------#-------------#------------
# values :- it returns all values 
# my_dict = {400:"sanket",200:"majithiya",300:"deepak"}
# all_values = my_dict.values()
# print(all_values)
# #-----------#--------------#-------------#-------------#------------
# ietms  # its Returns key vales pair all the 
my_dict = {400:"sanket",200:"majithiya",300:"deepak"}
my_dict.copy()
print(my_dict)
all_items = my_dict.items()
print(all_items)
#-----------#--------------#-------------#-------------#------------
# set -Default
my_dict1 = {
            # "Colour":"Red",
            "Company":"BMW",
            "Model":"x5"
    }
my_dict1.setdefault  ("Colour","Black")
my_dict1.setdefault( "Company","Rang Rover")
my_dict1.setdefault("Model","j&r")
print(my_dict1)
#-----------#--------------#-------------#-------------#------------
# sum of the numbers 
my_dict = {"A":10,"B":20,"C":30}
s = sum(my_dict.values()) # out put :- 60
print(s)
#-----------#--------------#-------------#-------------#-------------
# vowels 
# my_volwels = input("Enter your  vowels worlds:") 
# s = set(my_volwels)
# v = "a","e","i","o","u"
# d = s.intersection(v)
# print("your vowels number is",my_volwels,"are",d)
#-----------#--------------#-------------#-------------#--------------
# from-keys
my_dict = {100,200,300}
default_value = "Fruit"
my_dict = dict.fromkeys(keys,default_value)
print(my_dict) 
#-----------#--------------#-------------#-------------#--------------
# updated value be add old value replace with new value 
my_dict = {100:"sanket",200:"deepak"}
my_dict[100]="priyank"
print(my_dict)
#-----------#--------------#-------------#-------------#--------------
# get
# my_dict = {100:"sanket",200:"deepak",300:"priyank"}
# my_dict.get(400,"sanket")
# print(my_dict)
#-----------#--------------#-------------#-------------#--------------
# from keys 
keys = {100,200,300,400}
default_values = "Fruite"
my_dict = dict.fromkeys(keys,default_value) 
print(my_dict)  # out put :- {200: 'Fruit', 100: 'Fruit', 400: 'Fruit', 300: 'Fruit'} 

# Another example from keys 

book = {"python","java","PhP"}
default_value = 20
my_dict = dict.fromkeys(book,default_value)
print(my_dict) # out put {'PhP': 20, 'python': 20, 'java': 20}

#-----------#--------------#-------------#-------------#--------------
# Nested dictionary Accessing 

courses = {
    'python':{'duration':1000,'fees':500},
    'php':{'duration':1000,'fees':501},
    'java':{'duration':1000,'fees':502},
}    

# courses['python']['fees'] = 1000  # updated value
# print(courses)

# print(courses['php'])   # get multiple

# print(courses['python']['duration']) # single value get 

# for k,v in courses.items():   # itrate a all values
#     print(k,v) 



























my_dict = input(""" Enter your dictionary: eg:-{101: 'Alice Smith', 102: 'Bob Johnson', 201: 'Carol Taylor'}""")
input = {
  "company": {
    "name": "Tech Innovators",
    "location": "San Francisco",
    "departments": [
      {
        "name": "Engineering",
        "employees": [
          {
            "id": 101,
            "name": "Alice Smith",
            "role": "Software Engineer",
            "skills": ["Python", "Django", "React"],
            "contact": {
              "email": "alice.smith@example.com",
              "phone": "123-456-7890"
            }
          },
          {
            "id": 102,
            "name": "Bob Johnson",
            "role": "DevOps Engineer",
            "skills": ["AWS", "Docker", "Kubernetes"],
            "contact": {
              "email": "bob.johnson@example.com",
              "phone": "987-654-3210"
            }
          }
        ]
      },
      {
        "name": "Marketing",
        "employees": [
          {
            "id": 201,
            "name": "Carol Taylor",
            "role": "Marketing Manager",
            "skills": ["SEO", "Content Strategy", "Analytics"],
            "contact": {
              "email": "carol.taylor@example.com",
              "phone": "555-666-7777"
            }
          },
          {
            "id": 202,
            "name": "Carol Taylor",
            "role": "Marketing Manager",
            "skills": ["SEO", "Content Strategy", "Analytics"],
            "contact": {
              "email": "carol.taylor@example.com",
              "phone": "555-666-7777"
            }
          },
          {
            "id": 201,
            "name": "Carol Taylor",
            "role": "Marketing Manager",
            "skills": ["SEO", "Content Strategy", "Analytics"],
            "contact": {
              "email": "carol.taylor@example.com",
              "phone": "555-666-7777"
            }
          }
        ]
      }
    ],
    "established": 2010,
    "isPublic": False
  }
}