'''
generators

example 

youtuble: dosen't loads the whole video
loads by:
small chunks
when needed

simply generator work in the same format 

problem with list
list = [1,2,3,4,5]

entire list is stored in memory

nums = [i for i in range(100000)]

python consumes:
high memory
slower

generator :
produces values one at a time only when it is needed save memory

yield keyword:
yield pauses the function and returns 

return: end function
yield:pauses function
'''

#example:
# def numbers():
#     yield 1
#     yield 2
#     yield 3
# x = numbers()
# print(x)    

# #access the numbers
# print(next(x))
# print(next(x))

'''
1.first next()
yield 1 -->1
function paused

2.second next()
resume from previous position
yield 2-->2
function pause

3.third next()
resume from previous position
yield 3-->3
pause again

generators:
remembers the variables
remember line position
continue from the same place

#diff blw return and yield

return                                    yield
ends the function                          pauses the function
returns the single value by one           will return multiple values
no state memory                          remembers the '''

# def test():
#     return 1
#     return 2
# print(test())

# def numbers():
#     yield 1
#     yield 2
# for i in numbers():
#     print(i)
#for loop uses iter(),next() internal

#create the generator for even numbers
# def Evennumbers(limit):
#     num = 2
#     while num<=limit:
#         yield num
#         num+=2
# e = Evennumbers(10)
# for i in e:
#     print(i)

'''
#memory efficiency
nums = [i for i in range(100000) ]
generator 
nums = (i for i in range(100000))
only the current value

#lazy evaluation
values are generated when neede generators are lazy 


'''

#write a program for fibonaacci using generator

# Fibonacci series using generator

# def fibonacci(limit):
#     a, b = 0, 1

#     while a <= limit:
#         yield a
#         a, b = b, a + b

# x = fibonacci(20)

# for i in x:
#     print(i)











#create a custom iterator for even numbers

# class EvenNumbers:
#     #constructor method
#     def __init__(self,limit):
#         self.num = 2
#         #max limit
#         self.limit=limit
#     #this method makes the object iterable
#     # it returns the iterator object itself    
#     def __iter__(self):
#         return self
#     #next value during iteration 
#     def __next__(self):
#         if self.num>self.limit:
#             raise StopIteration
#         x = self.num
#         self.num +=2
#         return x
# e  = EvenNumbers(10)
# for i in e:
#     print(i)     







#create a custom iterator for even numbers

# class EvenNumbers:
#     #constructor method
#     def __init__(self,limit):
#         self.num = 2
#         #max limit
#         self.limit=limit
#     #this method makes the object iterable
#     # it returns the iterator object itself    
#     def __iter__(self):
#         return self
#     #next value during iteration 
#     def __next__(self):
#         if self.num>self.limit:
#             raise StopIteration
#         x = self.num
#         self.num +=2
#         return x
# e  = EvenNumbers(10)
# for i in e:
#     print(i)     







#create a custom iterator for even numbers

# class EvenNumbers:
#     #constructor method
#     def __init__(self,limit):
#         self.num = 2
#         #max limit
#         self.limit=limit
#     #this method makes the object iterable
#     # it returns the iterator object itself    
#     def __iter__(self):
#         return self
#     #next value during iteration 
#     def __next__(self):
#         if self.num>self.limit:
#             raise StopIteration
#         x = self.num
#         self.num +=2
#         return x
# e  = EvenNumbers(10)
# for i in e:
#     print(i)     







