'''
What is program ?
A program is a set of istructions stored on a disk

print("hello")

storing on a disk ????


python hello.py
hello

what is process?
when a program starts executing it becomes a process 
running ?
python hello.py
hello

os--Operating system

Chrome:
vscode:
spotify:
each one is a separate process


characteristics:
1. Independent
2. Separate memory
chrome:1.8GB, VS-code-500MB
3. Heavy a weight:
Memory allocaion
resource allocation
cpu scheduling


What is a thread ?
a thread is smllest unit of execution inside a process

restaurant == process
workers inside res = threads

worker1 - tasking the orders
worker2 - cooking
worker3 -billing
worker4 - cleaning

visually:
process:
chrome:
    +thread1
    +thread2
    +thread3
process                   thread
1.independent             part of process
2.heavy weight            light weeight
3.seperate memory         shared memory
4.slow                     fast
5.expensive                cheap
6.communication diffcult   easy

why threads are faster?
threaads will share the memory
process needs seperate memory allocation

concurrency?
teacher checking the notebooks
student A
student B
student C

concurrency:
A
B
C
A
B
C
one at a time
rapidly switching
appear simultaneously

parallelism:
cashier 1 ---> customer 1
cashier 2 ---> customer 2
cashier 3 ---> customer 3
truly simultaneous

CPU1 --->task a
CPU2 --->task b
CPU3 --->task c

A
B
A
B
A
B

parallelism:
cpu1 - AAA
cpu2 - BBB

one chef cooking
soup
fried rice

paralleism:
chef1 - soup
chef2 - noodles
cheef3 - fried rice

python thread will use ---concurrency
due to GIL - Global Interpreter Lock

'''

#creation of threads
import threading
#function created (do's nothing)
# def display():
#     print("hello")
# #thread object (creation)
# t = threading.Thread(target = display()) 
# t.start() 



#multiple threads
# import threading
# def task():
#     print("thread running")
# t1 = threading.Thread(target=task)    
# t2 = threading.Thread(target=task) 
# t3 = threading.Thread(target=task) 
# t1.start()
# t2.start()
# t3.start()


#thread with loops
# def numbers():
#     for i in range(5):
#         print(i)
# t = threading.Thread(target=numbers)
# t.start()        

# #two threads with diff task
# def even():
#     for i in range(0,10,2):
#         print("Even:",i)
# def odd():
#     for i in range(1,10,2):
#         print("odd:",i)
# t1 = threading.Thread(target=even)
# t2 = threading.Thread(target=odd)
# t1.start()
# t2.start() 
'''
os scheduler decides:
which thread to runs first
'''
# import threading
# print(threading.current_thread())               

#naming of threads:
import threading
# def task():
#     print(threading.current_thread().name)
# t = threading.Thread(target=task,name="Student_Thread")
# t.start()    

#passing arguments:
# def square(n):
#     print(n*n)
# t = threading.Thread(target=square,args=(5,))
# t.start()  


#to delay the threads
# import time
# print("start")
# time.sleep(3)
# print("end")


import threading
import time
def task():
    for i in range(5):
      print(i)
      time.sleep(1)
t = threading.Thread(target=task)
t.start()  


# #retry mechanism
# while True:
#    try:
#       connect()
#    except:
#       time.sleep(5) 



