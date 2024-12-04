#------------#-----------Synchronization------------#----------------#---------------

# Ager multiple threads are executing simultaneously to data inconsistency kaa chance ho sakta hai
# problem hogi
"""
Synchronization means at a time only one Thread (Ek time pe ek hi thread ko lega)
- synchronization threads execute hoga one by one so that we can usse overcome hogi 
  problems data inconsistency kii
The main application areas of synchronization are
1. Online Reservation system
2. Funds Transfer from joint accounts
etc
"""

# from threading import *
# import time
# def wish(name):
#    for i in range(10):
#       print("Good Evening:",end='')
#       time.sleep(2)
#       print(name)
# t1=Thread(target=wish,args=("Dhoni",))
# t2=Thread(target=wish,args=("Yuvraj",))
# t1.start()
# t2.start()

# hume irregular output milta hai to both threads are executing simultaneously wish()
# function hume ye problem ko overcome karne ke liye Synchronization use karte hai..

#------------#----------Synchronization By using Lock concept----------#---------------#--------

"""
Locks are the most fundamental synchronization mechanism provided by threading module.
l = Lock() Ese object create kar sakte hai hum uska

- Ye Lock object only one object ko hold karke rakhta hai at time Ager Dusre Thread ko 
required hai Woh same Lock ki to usko wait karna padega Lock ke releases hone ka
(similar to common wash rooms,public telephone booth etc)

- Lock karna hai acquire method() ka use karenge
l.acquire()

- unlock karna hai release() method 
l.release()


Note:-1. ager release() method ko call karenge to owner hona chahiye woh lock kaa khud
2.woh Lock hona chahiye already varna error show karega
RuntimeError: release unlocked lock
"""
# from threading import *
# l = Lock()
# # l.acquire() # Line -->1
# l.release

# Ager line number 1 ko comment ki acquire ko to ye error show karega
# RuntimeError: release unlocked lock

#------------#--------------------#---------------#------------#----------#
# from threading import *
# import time
# l=Lock()
# def wish(name):
#    l.acquire()
#    for i in range(10): 
#     print("Good Evening:",end='')
#     time.sleep(2)
#     print(name)
#    l.release()

# t1=Thread(target=wish,args=("Dhoni",))
# t2=Thread(target=wish,args=("Yuvraj",))
# t3=Thread(target=wish,args=("Kohli",))
# t1.start()
# t2.start()
# t3.start() # at a time only one thread is allowed to execute wish() method 

# Problem with Simple Lock:
"""
- jo Standard Lock object woh care nahi karta ki konsa thread currently(Abhi) hold kar raha hai
Ager Lock hold hai Aur koi koi bhi thread isse hasil karne ki koisi kar raha hai.
To woh block hojayega .bhale woh pehle se lock ko hold kar raha ho 

"""

# from threading import *
# l=Lock()
# print("Main Thread trying to acquire Lock")
# l.acquire()
# print("Main Thread trying to acquire Lock Again")
# l.acquire()
#-------------------#-------------------R-LOCK**-----------------#----------------#---------
# R -Lock :- isme multiple times Acure karte hai to error nahi milega 
# And lock me error aayega???
# current running threding ke baare me detail Rakhta hai(information rakh ta hai)

# step 1. syntax:- R Lock  object create kiye
"""
from threading import*
mylock = RLock()
"""
# step 2. acquire lock using acquire(). 
"""
syntax:-
mylock.acquire() # jiske uper lock lagvana hai uske uper isse call kardena hai

"""
# step 3. Release lock using release().
"""
syntax:- 
mylock.release()
"""

# Example :- 
# from threading import *
# l=RLock()
# print("Main Thread trying to acquire Lock")
# l.acquire()
# print("Main Thread trying to acquire Lock Again")
# l.acquire()


"""
Ager number of acquire() calls and release() calls should be matched
then only lock will be released.

Note:
1. Only owner thread can acquire the lock multiple times
2. The number of acquire() calls and release() calls should be matched.
"""
from threading import *
import time
l=RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    l.release()
    return result

def results(n):
      print("The Factorial of",n,"is:",factorial(n))

t1=Thread(target=results,args=(5,))
t2=Thread(target=results,args=(9,))
t1.start()
t2.start()

"""
# Difference between Lock and RLock:

Lock:- 
1 Ek time pe only one thread accquired kar sakta hai owner bhi multiple times 
acquire Nahi kar sakta
2. Not suitable to execute recursive functions and nested access calls
3. ye sirf Lock or unblocked ki take-care karega lekin owner thread ki nahi 

RLock:-
1.RLock woh at the time  only one thread acquire kar sakta hai lekin ownwer thread same
Lock object ko multiple times acquire kar sakta hai.

2.Best suitable to execute recursive functions and nested access calls
3.RLock object will takes care Locked or unlocked or owner thread information bhi lega 
recursiion level.
"""
#---------------#---------------Synchronization by using Semaphore(सेमाफोर):**--------------#----------------#----

"""

Lock and RLock ,at time only one thred is allowed karega execute karne Lekin.
lekin kahi baar hamari requriment hoti hai at a time particular number of threads
are allowed to access Network connection so esi requirments ko handle karne hum
Semaphore concept ka use karte hai..
Semaphore is advanced Synchronization Mechanism.
Eg:- hum chahte hai kii Ek time pe isme 100 students website ko Access kare tab hum iska use karenge 
Not morethan 100> only equal karna ho tab hi hum iska use karenge

"""

# step 1. syntax:- Semaphore  object create kiye
"""
from threading import*
s = Semaphore()
"""
# step 2. acquire lock using acquire(). 
"""
syntax:-
s.acquire() # jiske uper lock lagvana hai uske uper isse call kardena hai

jitne time app acquire karoge utne time aapko release bhi karna padega.. 

"""
# step 3. Release lock using release().
"""
syntax:- 
s.release() # ye lock ko release kar dega...

Note :- Jab bhi counter acquire 1 se - decrease hojata hai            Eg:-  3-1 = 2
        jab bhi counter release karega woh 1 se + increase hojayega   Eg:-  3+1 = 4   
        EK time pe isko 3 Thread Acssess kar sakte hai
# """
# from threading import *
# import time
# obj = Semaphore(3)
# # creating instance
# def display(name):
#     # call acquire method
#     obj.acquire()
#     for i in range(5):
#         print('Hello')
#         print(name)
#         time.sleep(4)
#     # calling release method
#     obj.release()
#     # release:- increment count

# t1=Thread(target= display, args=('Thread-1',))
# t2=Thread(target= display, args=('Thread-2',))
# t3=Thread(target= display, args=('Thread-3',))
# t4=Thread(target= display, args=('Thread-4',))
# t5=Thread(target= display, args=('Thread-5',))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# print("hello world")

#---------------#---------------Synchronization by using BoundedSemaphore(सेमाफोर):**--------------#----------------#----

"""
kahi baar humne acquire kar rahe hai 1 or release kar rahe 3 to us time pe hamara programe 
crase na ho isliye iska use karna chahiye har time

Note: To prevent simple programming mistakes, it is recommended to use BoundedSemaphore
over normal Semaphore. bounded smaphore use karna chahiye..
"""

# from threading import *
# s=BoundedSemaphore(2)
# s.acquire()
# s.acquire()
# s.release()
# s.release()
# s.release()
# s.release()
# print("End")
#---------------#---------------Diffrence between Lock and semaphore**--------------#----------------#----
"""
at a time Lock object can acquired only one thread,
semaphore object acquired:- by fixed number of threads by counter value

Conclusion:
The main advantage of synchronization is we can overcome data inconsistency problems.But the
main disadvantage of synchronization is it increases waiting time of threads and creates
performance problems. Hence if there is no specific requirement then it is not recommended to
use synchronization.
"""
#---------------#---------------Inter Thread Communication**--------------#----------------#----

"""
some times requirement hoti hai threads ki communicate with each other.This concept
intherthread communication
"""

# we can implement interthread communication by using the following ways
"""
1. Event
2. Condition
3. Queue
etc"""
#---------------#-----------------Event Objects:------------#----------------#----
"""
Event object simplest communication mechanism between the threads
Ek Thread signals dega event ko other thereds wait karega uska

Event object:- 
event = threading.Event()
"""

# Methods Event class ki :-

"""
Methods of Event class:
1.set() --> internal flag value will become True and it represents GREEN signal for all waiting
threads.
2. clear() --> inernal flag value will become False and it represents RED signal for all waiting
threads.
3. isSet() --> This method can be used whether the event is set or not
4. wait()|wait(seconds) --> Thread can wait until event is set
"""

#-----------#--------------#--------Pseudo Code:---------#-------------#-----------#-------

"""
vent = threading.Event()
#consumer thread has to wait until event is set
event.wait()
#producer thread can set or clear event
event.set()
event.clear()
"""

from threading import *
import time
def producer():
    time.sleep(5)
    print("Producer thread producing items:")
    print("Producer thread giving notification by setting event")
    event.set()
def consumer():
    print("Consumer thread is waiting for updation")
    event.wait()
    print("Consumer thread got notification and consuming items")

event=Event()
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()


from threading import *

import time 
def trafficpolice():
    while True:
        time.sleep(10)
        print("Traffic police giving GREEN signal")
        event.set()
        time.sleep(20)
        print("Traffic police giving RED signal")
        event.clear()
def driver():
    num=0
    while True:
        print("Drivers waitning for GREEN Sinal")
        event.wait()
        print("Traffic signal is GREEN...Vehicles can move")
        while event.isSet():
            num=num+1
            print("Vehicle No:",num,"Crossing the signal")
            time.sleep(2)
        print("Traffic signal is RED..Drivers have to wait")


event=Event()
t1=Thread(target=trafficpolice)
t2=Thread(target=driver)
t1.start()                    
t2.start()                    



