'''
1.race condition
2.synchronization
3.Lock
4.RLock
'''
#why we need synchronization?
'''
balance = 1000
thread-1 --- withdraw 500
thread-2 ---withdraw 700

both are accessing the same variable
without proper control
incorrect balance
wrong transcations
data corrupt
to avoid the above we will use:
synchronization:
this is a process of controlling access to shared
resource so that only one thread modifies at a time

Lock:
shared resources: any variables,file,database,object
example:
count = 0
if multiple threads modifies count simultaneously

#Race Condition:
occurs when multiple threads access and modify
shared data simultaneously causing unperdictable
outputs'''
# count = 0
# count +=1
# print(count)

#write eith threads
# import threading
# count = 0
# def increment():
#     global count
#     count+=1
# thread = [] 
# for i in range(1000):
#     t = threading.Thread(target=increment)
#     thread.append(t)
#     t.start()
# for t in thread:
#     t.join()
# print(count)    

'''
#critical section:
# code section where shared resources are
# accessed is called critical section
# count +=1--->critical section
 
 
to avoid the race condition?
one thread should enter critical section at a time:
solution: Lock
synchronization mechanism :
that allows only one thread to execute a critical section at a time

thread A acquires Lock
other Threads will wait
Thread A release Lock
next thread gets lock

import threading
Lock = threading.Lock()

#to apply lock
lock.acquire()

#to release
lock.release
 '''
import threading
# count = 0
# Lock = threading.Lock()

# def increament():
#     global count 
#     for i in range(1000):
#         Lock.acquire()      #or we can use "with lock" avoid acquire and release
#         #critical section
#         count+=1
#         Lock.release()
# t1 = threading.Thread(target=increament)
# t2 = threading.Thread(target=increament)
# t1.start()
# t2.start()
# print(count)         
    
import threading
import time 
# def whish(name):
#     for i in range(10):
#         print("good eveing:",end=" ")
#         time.sleep(1)
#         print(name)
# t1 = threading.Thread(target=whish,args = ("nani",))    
# t2 = threading.Thread(target=whish,args = ("bala",))
# t1.start()
# t2.start() 


#bank example
# class Bank:
#     def __init__(self):
#         self.balance = 1000
#     def withdraw(self,amount):
#         if self.balance >= amount:
#             self.balance -= amount
# import threading
# class Bank:
#     def __init__(self):
#         self.balance = 1000  
#         self.lock = threading.Lock()
#     def withdraw(self,amount):
#         with self.lock:
#             if self.balance >=amount:
#                 self.balance -=amount 
#                 print(amount,"withdrawn")
#             else:
#                 print("insufficent balance")             
# bank = Bank()
# t1 = threading.Thread(target=bank.withdraw,args=(700,))
# t2 = threading.Thread(target=bank.withdraw,args=(500,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(bank.balance)
        
'''
Deadlock:
where the threads wait forever for locks
Thread 1
Lock A
waiting for Lock B

thread 2:
Lock b
waiting for Lock A

thread 1 -->waiting Lock A
thread 2 -->woiting Lock B
deadlock
Rlock:Recursive lock
Athread can acquire the same
lock multiple times

why Rlock:
Normal Lock
acquire once
release once

if same thread acquires again
deadlock


'''
# import threading
# lock=threading.Lock()
# def outer():
#     lock.acquire()
#     inner()
#     lock.release()
# def inner():
#     lock.acquire()
#     print("Inner")
#     lock.release()
# outer()
'''

outer() acquired the lock
inner() trying to acquire the smae lock
lock is already wait forever
'''
import threading

Lock = threading.RLock()

def inner():
    with Lock:
        print("Inner")

def outer():
    with Lock:
        print("Outer")
        inner()

outer()

