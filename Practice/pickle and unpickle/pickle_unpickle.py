# pickle.py 

# pickle:- To convert python object to byte strem this pickle or writing state :- dums() serializing  

# unpickling :- To convert byte strem to python object  this unpickling or reading state:- load() deserializing


import pickle

data = {'name':'sanket','age':25,'languages':['python','java','c++']}

with open ('pickle and unpickle/data.pkl','wb') as file:
    pickle.dump(data,file)

print("data has been successfully pickled and saved to 'data.pkl'")    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
"""
# Read Mode for unpickling
'r' : Read mode
'w' : write mode
'b' : Binary mode
'rb': Read in binary mode
'wb': write in binary mode
"""

# Unpickling 
with open('pickle and unpickle/data.pkl','rb') as file:
    loaded_data = pickle.load(file)

print("Unpickled Data:",loaded_data)    


# Example 2). pickling multiple objects 

import pickle

data1 = [1,2,3,4,5]
data2 = {'a':10, 'b':20, 'c':30}

with open ('pickle and unpickle/multiple_data.pkl','wb') as file:
    pickle.dump(data1, file)
    pickle.dump(data2, file)

print("Multiple objects have been pickled")    


# unpickling or unserialize's 

with open('pickle and unpickle/multiple_data.pkl','rb') as file:
    loaded_data1 = pickle.load(file)
    loaded_data2 = pickle.load(file)

print("unpickled Data1:",loaded_data1)    
print("unpickled Data1:",loaded_data2)    


# Example-3) . Pickling Data to a Bytes Object

import pickle

data = [10,20,30,40]

pickle_data = pickle.dumps(data)

print("Data serialized to bytes:",pickle_data)


# unpickling :- 

unpickeld_data = pickle.loads(pickle_data)

print("Data deserialized from bytes:",unpickeld_data)






# practice 

# pickle Basic 

# import pickle

# data = {'name':'sanket','age':22,'salary':100000}

# with open('pickle and unpickle/practice.pkl','wb') as file:
#     pickle.dump(data,file)


# print("Data has been pickled and saved to 'data.pkl'")


# # unpickle 

# with open('pickle and unpickle/practice.pkl','rb') as file:
#     loaded_data = pickle.load(file)

# print("unpickled Data:",loaded_data)    

# import pickle

# data = {'name':'sanket','age':25,'salary':100000}

# with open ('pickle and unpickle/test2.pkl','wb') as file:
#     pickle.dump(data,file)
# print('pickl has been success full','test2.pkl') 


# # unfickling 

# with open('pickle and unpickle/test2.pkl','rb') as file:
#     loaded_data = pickle.load(file)
# print("unpicled data:",loaded_data)    









# pickle dump :- python object convert to bytestrems  dump() fun  :- serilazer process also know

# import pickle

# data  ={"name":"sanket","age":22, "laungage":['pythpn','java','php']}

# with open ('pickle and unpickle/test777.pkl','wb') as file:
#     pickle.dump(data,file)
# print("The pickle is succfully create test777.pkl")


# # unpickling :-  unserilazer load () func byte strem convert into python objects

# with open('pickle and unpickle/test777.pkl','rb') as file:
#     loaded_data = pickle.load(file)
# print("unpickeld data:",loaded_data)    




# multiple objects pickle 

# import pickle

# data1 = [1,2,3,4,5]
# data2 = {'a':10,'b':20,'c':30,'d':40}

# with open ('pickle and unpickle/multiple.pkl','wb') as file:
#     pickle.dump(data1,file)
#     pickle.dump(data2,file)
# print("the pickle has successfully multiple objects")    


# # unpickle multiple objects

# with open ('pickle and unpickle/multiple.pkl','rb') as file:
#     loaded_data = pickle.load(file)
#     loaded_data2 = pickle.load(file)

# print("unpickle data",loaded_data)    
# print("unpickle data2",loaded_data2)    



# pickle simple Eg:- to convert python object to bystrems (serialier) 
# import pickle

# data = {"name":"sanket","age":25,"laungvage":["python","java","php"]}

# with open ('pickle and unpickle/test.pkl','wb') as file:
#     pickle.dump(data,file)
# print("pickle has succesfully")

# # unpickle 

# with open ('pickle and unpickle/test.pkl','rb') as file:
#     pickle_data = pickle.load(file)
# print("The unfikeld data",pickle_data)    

# # multiple objects pickle 

# data1 = [1,2,3,4,5]
# data2 = {'a':10,'b':20,'c':30}

# with open('pickle and unpickle/multiple_objects','wb') as file:
#     pickle.dump(data1,file)
#     pickle.dump(data2,file)

# print("succsfully pickle!!")

# # unpickle multiple objects 

# with open("pickle and unpickle/multiple_objects",'rb') as file:
#     multiple_objects1 = pickle.load(file)
#     multiple_objects2 = pickle.load(file)

# print("unpicked object1:",multiple_objects1)
# print("unpicked object2:",multiple_objects2)









