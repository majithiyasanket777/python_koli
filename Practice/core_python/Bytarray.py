# bytearray its is a mutable we can add and change the values of (1,256)
 
l = [10,20,30,40,50] 
b = bytearray(l)
b[0] = 77
for x in b:
    print(x)


# bytes # immutable 

l =  [10,20,30,40,50]
b = bytes(l)
b[0] = 79
