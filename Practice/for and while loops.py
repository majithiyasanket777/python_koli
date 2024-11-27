# for Loop syntax
# for x in seqence:
#    body

# -----------------#--------------#-------------#------------
s = "sanket"

for x in s:
    print(x)
# -----------------#--------------#-------------#------------
# To print characters present in string index wise:
# s = (input('Enter your string:'))
# i =  0

# for x in s:
#     print("The charcters present at",i,"index is present:",x)
#     i=i+1
# -----------------#--------------#-------------#------------

# for odd numbers 

# for x in range(21):
#     if (x%2!=0):
#         print(x)



# s = input("Enter your number")
# for x in s:
#     print("This is odd numbers",s%2==0)


# -----------------#--------------#-------------#------------

# syntax itable and expressions
# This is even numbers
my_list = [x for x in range(21) if x%2==0]
print(my_list)

# -----------------#--------------#-------------#------------

# This is odd numbers 
my_list = [x for x in range(21) if x%2!=0]
print(my_list)


# -----------------#--------------#-------------#------------
# even numbers

my_list = [ x for x in range(21) if x%2==0]
print(x)

# -----------------#--------------#-------------#------------

# while loops examples 

x = 1
while x <10:
    print(x)
    x=x+1

i = 1
while i<=10:
    print("hello,Welcome to while loop")
    print(i)
    i=i+1

# -----------------#--------------#-------------#------------
x=1
while x<=20:
    if x %3==0:
        print(x)
    x=x+1
# -----------------#--------------#-------------#------------

# n = int(input("Enter the number:"))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i

# -----------------#--------------#-------------#------------

# name = ''
# while name != 'sunny':
#     name = input("Enter your favouirte actress:")
# print('thnaks for conformation')    

# -----------------#--------------#-------------#------------

# infinite loop
# i = 1 
# while i+1:
#     print('hello sanket How are you',i)
#     i=i+1 
# -----------------#--------------#-------------#------------

# nested loop loop inside in loop

# for i in range(3): # outer for loop
#     for j in range(2): # iner for loop
#         print("hello")

# -----------------#--------------#-------------#------------
# Breack statement 

# i = 1 
# while i 


for i in range(10):
    if i==7:
        print("The code while be stope")
        break
    print(i)

# -----------------#--------------#-------------#------------

cart =  [10,20,30,500,600,700]
for item in cart:
    if item>600:
        print("Your product item is Above 600 please enter item below <600 ")
        break
    print("processing item",item)
# -----------------#--------------#-------------#------------

# continue statement

for i in range(10):
    if i==4 or i==7: # 4 or 7 ko skip kardiya
        continue
        # print("The itraction whill be next")
    print(i) 
# -----------------#--------------#-------------#------------

cart = [10,20,30,500,700,800]
for item in cart:
    if item>=500:
        print("we can not procced the item:",item)
        continue
# -----------------#--------------#-------------#------------

cart = [10,20,30,40,50]
for item in cart:
    if item>=500:
        print("We can  not proccesd the item:",item)
        break
    print(item)                                             
else:
    print("Congrats all the item processed successfully.....")


# pass 

for i in range(100):
    if i%9==0:
        print(i)
    else:pass 



sanket=[20,30,40,50,6,0]
del sanket
print(sanket)       
