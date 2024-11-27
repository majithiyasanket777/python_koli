#  + pluse index left to right 
#  - right to left 


# Explicit :- maunally 
# Implicit :- automatically

s = "durga"
print(s[0]) # d

print(s[1]) # u

print(s[1:]) # urga

print(s[1:40]) # urga

print(s[:4]) # durg


print(s[:]) # durga

print(s*3) #  durga durga durga


# print(len(s)) # 5


# range (start_value, stop_value, step_value)

# for i in range(5):
#     print(i)

# for i in range(1,5):
#     print(i)    

# for i in range(1,5,2):
#     print(i)    


for i in range(2,21,5): # 2,7,12,17 
    print(i)    

# with using loops  1 to 100
for i in range(1,101):
    print(i)    



# def number()    


# type casting 

# to convert one type to Another type  
# Eg:- 

# reusult = bool(2.30)
# print(type(reusult))



# result = complex("ten")
# print (type(result))


# print(complex(10.5))

z1 = complex(4,-5)

z2 = complex(4,-1)

print(z1 * z2)



print (bool(0))
print(bool(0+0j))
print(bool(""))
# print(type(z))
# real and imagenary part are zero the result is :- flase 
# empty string the result is :- flase 


# List Accessing 
list1 =  [20,55,20,'Hello']
list1[1] = 'sanket'   

print(list1)


# list Accessing :- 

list2 = ['Apple',20,30,40,50]
list2 [1] = 'sanket'

print(list2)

# nested list  Accessing 

list1 = [['sanket',50],['deepak',60] ,['vivek',90]]
list1 [1] = ["Apple",50]
print(list1)