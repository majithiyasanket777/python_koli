# Multi Threading

# multi Tasking :- koi work ko ek sakth karna it's call multi tasking 

#  There are 2 types of Multi Tasking:- 

# 1. Process based Multi Tasking:- (suitable at operating system level)
"""
kahi work's ko Ek sath karna jaha pe jo task hai uski process jo hai woh independent hai
   ese Tasks ko process based Multi Tasking kehte hai  
# Another #
Ek hi Time par bout sare Task Execute hote hai jisme har ek Task seprate hota hai 
matlb:- EK Task ka dusre Task se koi lena dena Nahi hai thats process based Multi Threding
   
Eg:- hum python code typing karte hai editor se and we can listen mp3 song the wahi same system
At the same time hum download bhi kar sakte hai woh same file ko internet se.
ye jo Task hai woh executing ho rahe hai Ek sath lekin independent hai(each other) sab se .

"""
#---------------#----------------#---------------#------------------#--------
# 2. Thread based Multi Tasking:- (programatic Level for suitable)

"""
isme kya hai kii Ek programe me hi alag alag Task hai woh Task independent hai woh Task Ek Thread keh laayega woh 
Therad kaa Dusre Task(Thered se) koi lena dena nahi hai
That is Thread based Multi Tasking
or 
Process Me :- har ek Task ek indepent programe hota hai 
And 
2.Thread based Multi Tasking:- isme Ek programe me sare Task hote hai Ek dusre se independent hote hai..
uss Task :-Thered kaha jata hai  

The main important application areas of multi threading are:
1. To implement Multimedia graphics
2. To develop animations
3. To develop video games
4. To develop web and application servers
etc...

Every python program by defalult contains one thread which is nothing but main Thread.

"""
import threading
print("Current Executing Thread:",threading.current_thread().getName())

# current_thread() which returns the current executing
# Thread object. ye object ko call karta hai getName() To hume current executing thread ka name milega.
# o/p: Current Executing Thread: MainThread

#----------#----------The ways of Creating Thread in Python:-----------#-----------#--------
# thread in python by using 3 ways

# 1. Creating a Thread without using any class:

from threading import *
def display():
    for i in range(1,11):
        print("Child Thread")
t=Thread(target=display) #creating Thread object
t.start() #starting of Thread
for i in range(1,11):
    print("Main Thread")

"""
Ager multiple threads present honge hamare program,so hum execution order hai woh Accapt
nahi kar sakenge or hum exact output bhi expect nahi kar sakte multiple threaded programs se
bcause woh exact out  put provide hi nahi karta ye depend karta hai machine to machine and 
run to run.

Note:-Thread hai woh pre-define class hai python module me hum apna own  Thread create nahi kar sakte
"""
#---------------#----------------#---------------#------------------#--------

# 2. Creating a Thread by extending Thread class

"""
We have to create child class for Thread class. In that child class we have to override run() method
with our required job. Whenever we call start() method then automatically run() method will be
executed and performs our job.
"""
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread-1")
t=MyThread()
t.start()
for i in range(10):
    print("Main Thread-1")

#---------------#----------------#---------------#------------------#--------

# 3. Creating a Thread without extending Thread class:

from threading import *
class Test:
    def display(self):
          for i in range(10):
            print("Child Thread-2")
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread-2")  

#------------#----------# Setting and Getting Name of a Thread:----------#---------------#--------

"""
pyhton me every thered kaa by default name diya hota hai usko hum customized name bhi
provide kar sakte hai by programmer.
t.getName() --> Returns Name of Thread
t.setName(newName) --> To set our own name
"""

from threading import *
print(current_thread().getName())
current_thread().setName("sanket majithiya")
print(current_thread().getName())
print(current_thread().name) # pehle MainThread tha or abb new name hogaya hai change hoke sanket majithiya

"""
out-put:- 
MainThread
sanket majithiya
sanket majithiya

"""
#------------#----------Thread Identification Number(ident)::----------#---------------#--------

"""
sare thread ka internally unique identification number available hota hai. we can acess 
this id by using implicit variable "ident"
"""

from threading import *
def my_thread():
    print("This is child thred")
my_thread1 = Thread(target=my_thread)

my_thread1.start()
print("The main Thread identification Number:",current_thread().ident)
print("child Thread identification Number:",t.ident)

#------------#---------active_count()------------#----------------#---------------
# This function returns the number of active threads currently running.
# ye function return karega Active threads currently running kitne hai uska number.

from threading import Thread, active_count

def my_thread():
    """A simple thread function"""
    print("Thread is running")

print(f"Active threads before starting: {active_count()}")

t = Thread(target=my_thread)
t.start()

print(f"Active threads after starting: {active_count()}")
t.join()
print(f"Active threads after finishing: {active_count()}")

#------------#---------enumerate() function------------#----------------#---------------

# This function returns a list of all active threads currently running.

# from threading import Thread, enumerate
# import time

# def thread_function(name):
#     """A simple thread function"""
#     print(f"Thread {name} starting")
#     time.sleep(2)  # Simulate some work
#     print(f"Thread {name} finishing")

# thread1 = Thread(target=thread_function, args=("One",))
# thread2 = Thread(target=thread_function, args=("Two",))

# thread1.start()
# thread2.start()

# active_threads = enumerate()
# print(f"Active threads: {[thread.name for thread in active_threads]}")

# thread1.join()
# thread2.join()

# final_active_threads = enumerate()
# print(f"Active threads after completion: {[thread.name for thread in final_active_threads]}")

#------------#---------isAlive()------------#----------------#---------------

# isAlive() method checks whether a thread is still executing or not.

# from threading import *
# import time
# def display():
#     print(current_thread().getName(),"...started")
#     time.sleep(1)
#     print(current_thread().getName(),"...ended")
# t1=Thread(target=display,name="ChildThread1")
# t2=Thread(target=display,name="ChildThread2")

# t1.start()
# t2.start()

# print(t1.name,"is Alive :",t1.is_alive())
# print(t2.name,"is Alive :",t2.is_alive())
# time.sleep(3)
# print(t1.name,"is Alive :",t1.is_alive())
# print(t2.name,"is Alive :",t2.is_alive())
#------------#---------join() method:------------#----------------#---------------

# If a thread wants to wait until completing some other thread then we should go for
#  join() method.

# from threading import *
# import time 
# def display():
#     for i in range(10):
#         print("seetha Thread")
#         time.sleep(2)

# t = Thread(target=display)
# t.start()
# t.join() # This is Line executed by main Thread
# for i in range(10):
#     print("Ram Thread")        

# Example to call join method() time period
"""
Note: We can call join() method with time period also.
t.join(seconds)
In this case thread will wait only specified amount of time.

"""
# from threading import *
# import time 
# def display():
#     for i in range(10):
#         print("seetha Thread")
#         time.sleep(2)

# t = Thread(target=display)
# t.start()
# t.join(5) # This is Line executed by main Thread
# for i in range(10):
#     print("Ram Thread")    

"""
Working with Mysql database
"""        

#------------#---------# Daemon Threads:()------------#----------------#---------------

# matlab ki ye background me bhi running hi hote hai This threads are call Daemon Threads

# iska main object hai ki ye support provide karta hai Non Daemon Threads ko like(main thread)

"""
Eg:- Garbage Collector

Ager main Thread runs karta hai low memory, immediately PVM runs Garbage  Collector ye 
destroy kardega useless objects ko and provide karega free memory,so woh main Thread 
wapas se continue execution kar sakta koi bhi memory problems bina.
"""
# How to check whether thread is Daemon or not by using t.isDaemon()

from threading import *
print(current_thread().isDaemon())
print(current_thread().daemon)
# ye method se hum Daemon ka nature chabge kar sakte hai, but hume Thread sataring 
# se pehle isko use karna padta hai  warna RuntimeException:cannot set daemon status of active thread

# from threading import *
# print(current_thread().isDaemon())
# current_thread().setDaemon(True)  # RuntimeError: cannot set daemon status of active thread

#------------#-----------Default Nature:()------------#----------------#---------------

"""
- by Default main Thread jo hota hai woh Non Daemon hota hai but jo thread baaki hai woh
parent to child inharit karate hai and parent hai woh Daemon hai to child bhi hoga
ager nahi hai to chil bhi nahi hoga  

"""
# Eg:- 1
# from threading import *
# def job():
#     print("Child Thread")
# t=Thread(target=job)
# print(t.isDaemon())#False
# t.setDaemon(True)
# print(t.isDaemon()) #True

"""
Whenever the last Non-Daemon Thread terminates automatically all Daemon Threads will be
terminated.
"""
# Eg:- 2
# from threading import *
# import time
# def job():
#     for i in range(10):
#         print("Lazy Thread")
#         time.sleep(2)
# t=Thread(target=job)
# #t.setDaemon(True)===>Line-1
# t.start()
# time.sleep(5)
# print("End Of Main Thread")

"""
Note:- 
Eg:- 2  me jo comment ki hai Line 1 so both Main Thread and child Threads are Non Daemon
and both will be executed their completion.

Note:- Ager hum commenting Line 1 hai woh naa karte to Main Thread  hai woh Non-Daemon
and hamara child Thread Daemon kehlata
-Ager main Thread Terminates hoga Automatically so child be terminate hoga automatically 
"""
