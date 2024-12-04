# If :-  if 1 condition is true than code to be excuted

name = input("Enter your name: ")

if name == "sanket" or name == "SANKET":
    print("Hello sanket good morning") 
    print("How are you!!!")    

# -----------------#--------------#-------------#------------
# if-elif

name = input("Enter your name: ")

if name == "sanket" or name == "SANKET" :
    print("hello sanket good morning") 
else:
    print("This is  not your name")
print("how are you") 
# -----------------#--------------#-------------#------------
# if-elif-else
name = input("Enter your name:")

if name == "sanket":
    print("hello sanket good morning")
elif name == "SANKET":
    print("hello SANKET good morning")
else:
    print("This is  not your name")
print("how are you") 
#-----------------#--------------#-------------#------------

# 3) if-elif-else

brand = input("Enter your Favourite brand: ")

if brand == "FO" or brand == "fo":
    print("This is childran brand")
elif brand == "FA":
    print("This brand is man brand") 
elif brand == "FT":
    print("This is super Duper Hit brand") 
else:
    print("This is not your brand")    
name=input("Enter Name:")

#-----------------#--------------#-------------#------------
# if name=="sanket":

#     print("Hello Durga Good Morning")

# else:
#    print("Hello Guest Good Moring")
# print("How are you!!!")

#-----------------#--------------#-------------#------------

name = input("Enter your name:")

if name =="SANKET" or name == "sanket":
    print("Hello sanket good moring")
else:
    print("This is not your name")

print("How are you")  
#-----------------#--------------#-------------#------------

# find Bigesst 2 number of commond  promate


n1 = int(input("Enter First number"))
n2 = int(input("Enter second number"))


if n1>n2:
    print("the bigesst number is:",n1)
else:
    print("the bigesst number is:",n2)

#-----------------#--------------#-------------#------------
# Write a program to find biggest of given 3 numbers from the commad prompt?


a = int(input("Enter first  number:"))
b = int(input("Enter second number:"))
c = int(input("Enter Third  number:"))

if a>b and a>c:
    print("the biggest number is",a)
elif b>c:
    print("the biggest number",b)
else:       
    print("the biggest number",c)   


#-----------------#--------------#-------------#------------
# Write a program to find smallest of given 2 numbers from the commad prompt?


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if a<b:
    print("the smalles number",a)
else:    
    print("the smalles number",b)

#-----------------#--------------#-------------#------------
# Write a program to find smallest of given 3 numbers from the commad prompt?


a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter thired number"))

if a<b and a<c:
    print("Enter the smallest number",a)
elif b<c:
    print("Enter the smallest number",b)
else:
    print("Enter the smallest number",c)
#-----------------#--------------#-------------#------------

# Write a program to check whether the given number is even or odd?
            

a = int(input("Enter first number:"))  

if a % 2 == 0:
    print("this is your even numbers")
else:
    print("the number is odd ")    
#-----------------#--------------#-------------#------------
# Write a program to check whether the given number is in between 1 and 100?

n = int(input("Enter your number:"))

if n>=1 and n<=100:
    print("the number",n, "is between")
else:    
    print("the number",n, "Not  between")
#-----------------#--------------#-------------#------------
#  Q. Write a program to take a single digit number from the key board and print is value in English word?

a = int(input("Enter your number: "))

if a == 0:
   print("ZERO")

elif a == 1:
   print("ONE")

elif a == 2:
   print("TWo")

elif a == 3:
   print("THEREE")

elif a == 4:
   print("FOURE")

elif a == 5:
   print("FIVE")

elif a == 6:
   print("SIX")

elif a == 7:
   print("SEVEN")

elif a == 8:
   print("Eight")

elif a == 9:
   print("NINE")

elif a == 10:
   print("TEN")

else:
    print("The number from 0 to 10")
