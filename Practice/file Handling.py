"""
as part of programing we have store our data permently for future purpose.
for this requirement we should go for files.
Types of files :-

1. Text files:- To store character data Eg:- abc.txt
2. Binary files :- like images,video files,audio files etc
"""

""" Page 186
To allow mode in python
f = open(filename, mode)

r - read that file 

w - write operation Ager specified file is not already availble 
then this mode create file new file

a - append ke liye use karte hai if already contains some data than ye override karegi and 
Ager nahi hai already so new file create karegi

r+ - read and write data into the file 

w+ - To write and read data.override karega exiting data ko

a+ - To append and read data from the file

x - Ager file already exit karti hogi then we will get error file already ExistsError.


Note:- Ager hume file ko close Nahi karni hai to hum file ko with se bhi likh sakte hai 
 
Note*:- with open likhenge to hume file ko close() kara ne kii jarrorat nahi hai
"""

# f = open("sanket.py","w")
# x = f.write("hello sanket this is your files")
# f.close()


with open("sanket.py","w") as f:
    f.write("hello sanket Good morning")


#-----------#--------------#-------------#-------------#--------------
f = open("sanket.py","w")
print("file name",f.name) 
print("file Mode",f.mode)
# print("file Readable",f.readable())
print("file writable",f.writable())
# print("file is close",f.close)
# f.close()
# print("file is close",f.close)
#-----------#--------------#-------------#-------------#--------------
# (Write)data overriede every time :- will file will be run
# f = open("sanket.py","w")
# f.write("sanket\n")
# f.write("majithiya1\n")
# f.write("prashantBhai\n")
# print("data writeen to success fully")
# f.close()

# Note :- while writing data by using write() methods, compulsory we have to provide line 
# seperator(\n),otherwise total data should be written to a single line.

#-----------#--------------#-------------#-------------#--------------
# Reading data to text file:-
"""
read()-> To read total data from the file
read(n) -> To read 'n' characters from the file
readline()-> To read only one line
readlines()-> To read all lines into a list
"""

# f = open("function.py","r")
# data = f.read() # read all data
# data = f.read(10) # To read first 10 charater :- spece be count karega
# print(data)
# f.close()

#-----------#--------------#-------------#-------------#--------------
with open("function.py","r") as f:
    if f.readable:
        for line in f:
            print(line,end='')  
#-----------#--------------#-------------#-------------#--------------

# tell() :- to find of curent postion of a file pointer from the beginning of the file.
# - start position with 0 

f = open("sanket.py","r")
print(f.tell()) #bye default 0 hoga kyki start with 0
print("reading the entire file again",f.read())
f.read(3)
f.close()

# seek() :- hum postion change kar sakte hai using seek() method 

data = 'sanket majithiya'
f = open("sanket.py",'w')
f.write(data)
with open('sanket.py','r+') as f:
    text=f.read()
    print(text)
    print("The current cusor postion",f.tell())
    f.seek(17)
    print("The current cusor postion",f.tell())
    f.write("MS!!")
    f.seek(0)
    text=f.read()
    print("Data After modification")
    print(text)
#-----------#--------------#-------------#-------------#--------------
""" 
How to check particular programe exist or Not
we can use os library to get information about files in our computer
"""
# How to check file exits or Not?? if avialable then print its content

# import os,sys
# fname = input("Enter your file Name:")
# if os.path.isfile(fname):
#     print("File exists:",fname)
#     f=open(fname,"r")
# else:
#     print("file does not exist:",fname)
#     sys.exit(0)
# print("The content of file is:")
# data=f.read()
# print(data)        
#-----------#--------------#-------------#-------------#--------------
"""
Program to print the number of lines,words and characters present in the
given file?
# """
# import os,sys
# fname = input("Enter your file Name:")
# if os.path.isfile(fname):
#     print("The file is exists",fname)
#     f=open(fname,"r")
# else:
#     print("file does not exists:",fname)
#     sys.exit(0)
# Icount=wcount=ccount=0
# for line in f:
#     Icount=Icount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# print("The number of Lines:",Icount)
# print("The number of Words:",wcount)
# print("The number of Characters:",ccount)    
#-----------#--------------#-------------#-------------#--------------
# Handling Binary Data:like images,video files,audio files etc.

# f1=open("your.jpg","rb")
# f2=open("newpic.jpg","wb")
# bytes=f1.read()
# f2.write(bytes)
# print("New Image is available with the name: newpic.jpg")
#-----------#--------------#-------------#-------------#--------------

# csv :- comma seprated value usko likha jata hai .csv Eg:-python.csv

import csv

data = [
    ["PassengerId", "Name", "Age", "Survived"],
    [1, "John Doe", 22, 2],
    [2, "Jane Smith", 28, 0],
    [3, "Robert Brown", 35, 1],
    [4, "Emily White", 19, 0]
]

# data ko write kara ne change kare tab
with open('titanic.csv','w',newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Sample data written to titanic.csv")

# isse data read hoga

with open("titanic.csv", "r") as f:
    titanic_data = csv.DictReader(f, delimiter=",")
    for row in titanic_data:
        print(row)
#-----------#--------------#-------------#-------------#--------------
# zip and unzip files
"""
Advntages :-- improve memory utilization
2. Ager hum file ko transfer kar rahe hai to time reduce kar sakte hai
3.we can improve performance.
syntax:- f = ZipFile("files.zip","W","ZIP_DEFLATED")
f.write(filename) # add file by using write() method.
"""
# zip file isse banegi
from zipfile import *
f=ZipFile("sanket2.zip",'w',ZIP_DEFLATED)
# f.write("sanket2.txt") # Ager write karna hai to 
f.write("file2.txt")
f.write("file3.txt")
f.close()
print("file.zip file xreated successfully")


# unzip karna hoto woh file ko
# from zipfile import *
# f=ZipFile("sanket2345515.zip",'r',ZIP_STORED)
# names=f.namelist()
# for name in names:
#     print( "File Name: ",name)
#     print("The Content of this file is:")
#     f1=open(name,'r')
#     print(f1.read())
#     print()


# chechk karna hoto zip hai ki nahi woh file 
import zipfile

def is_zip_file(file_path):
    return zipfile.is_zipfile(file_path)

file_path = "sanket2345515.zip"

if is_zip_file(file_path):
    print(f"{file_path} is a valid ZIP file.")
else:
    print(f"{file_path} is not a ZIP file.")

#-----------#--------------#-------------#-------------#--------------
# 1. current working Directory check:-
# import os
# cwd=os.getcwd()
# print("The current working Directory:",cwd)
#-----------#--------------#-------------#-------------#--------------
# 2. TO create sub directory in current working directory

# import os
# os.mkdir() # ()-->("your sub directory name")
# print("mysub Directory created in cwd:")

#-----------#--------------#-------------#-------------#--------------
# 3. rename directory

# import os
# os.rename("sanket777.py","errors.py")
# print("myvijay directory rename to newdir")
#-----------#--------------#-------------#-------------#--------------
# 4. remove directory

# import os
# os.removedirs("/home/vijay/Templates/Practice/errors.py")
# print("my sub directory delted")
#-----------#--------------#-------------#-------------#--------------
# 5. list of all sub  directory 
# import os
# print(os.listdir(".")) 
#-----------#--------------#-------------#-------------#--------------
import os

for dirpath,dirnames,filenames in os.walk('.'):

    print("Current Directory Path:",dirpath)

    print("Directories:",dirnames)

    print("Files:",filenames)

    print()
#-----------#--------------#-------------#-------------#--------------








print("hello world")







# revision 

# with open("sanket.py","w") as f:
#     f.write("hello sanket you are python devloper")

