# Anonymous Functions: lambda function some time we decare function with out name (some time we can pass function as arrgumet another fuction such cases best choice )

# syntax  :- Aargumets_list: expression

square = lambda n:n*n

print("The squer of 4 is:",square(4))
print("The squer of 5 is:",square(5))

my_sum = lambda a,b:a+b

print("The sum of number is:",my_sum(10,20))

#-----------#--------------#-------------#-------------#-------------
# filter () syntax :- (function, iterable) 

l = [1,2,3,4,5,6,7,8,9,10]

z = list(filter(lambda x: x %2==0,l))

print(z)          
#-----------#--------------#-------------#-------------#-------------
# map() (function: itrable )

my_list = [1,2,3,4,5,6,7,8,9,10]

z = list(map(lambda x:x*2,my_list))

print(z)

# map function ka use aap aapseme 2 list kaa squere,sum(+) sab kar sakte ho lekin 
# Note :- ***lenghth same honi chahiye
l = [1,2,3,4,5]

l2 = [6,7,8,9,10]

l3 = list(map(lambda x,y:x*y ,l,l2))
print(l3)
#-----------#--------------#-------------#-------------#-------------
# reduce ()  # Reduce sequence of eliments into a single eliment buy using function :-reduce karo sequence of elimets ko into single eliment se..
from functools import reduce

l = [1,2,3,4,5,6,7,8,9,10]

z = reduce(lambda x,y:x+y,l)
# z = reduce(lambda x,y:x*y,l) 
# z = reduce(lambda x,y:x+y,range(1,101)) # output :- 5050

print(z)