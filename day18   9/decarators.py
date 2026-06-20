'''
decorators :
adds the extra functionality without changing the original function


gift wrapper
extra layer , beauty
decarator = wrapper around the function

#why decorators are needed?
logging:
authentication,
timing
validation


if no decorators 
1.repeted code
2.messy programs
 '''

#in python -->function are treated like variables    

# def greet():
#     print("hello students")
# x = greet    
# x()

# def outer():
#     def inner():
#         print("inner side")
#     inner()
# outer()  


# def outer():
#     def inner():
#         print("inner side")
#     return inner()
# x =outer
# x()
'''
outer() called
|
returns the inner function
|
stored in x
|x()-->executes inner
'''

'''
example 
#simple decorator'''
# def decorator_function(original_function):
#     def wrapper():
#         print("before function call")
#         original_function()
#         print("after function call")
#     return wrapper
# #original function :
# def greet():
#     print("hello students")
# #apply manually
# decorated = decorator_function(greet)
# decorated()

'''
greet()
|
decorator_function()
|
wrapper created
|
extra functionality is added

shortcut syntax:
special symbol:@
 ''' 
# @decorator_function
# def greet():
#     print("hello students") 

#example2:
# def smart_divide(func):
#     def wrapper():
#         print("checking before div")
#         func()
#         print("division is completed")
#     return wrapper 
# @smart_divide
# def divide():
#     print(10/2)   
# divide()    

# #example3:
# def decorator_function(original_function):
#     def wrapper(name):
#         print("before function call")
#         original_function(name)
#         print("after function call")
#     return wrapper

# @decorator_function
# def greet(name):
#     print("hello",name)
# greet("name")    


# #timer decorator:
# import time
# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("execution time",end-start)
#     return wrapper
# @timer
# def test():
#     for i in range(10000):
#         pass

# test()


#example2:
def login_required(func):
    def wrapper():
        print("checking  the user login")
        func()
    return wrapper
@login_required
def dashboard():
    print("welcome to dashboard")
dashboard()    