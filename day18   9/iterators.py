'''

iterators:
gives one element at a time on demand
python refers iterators:
memory efficiency
controlled access

iterable:is an object can be looped
1.list
2.tuple
3.set
4.dict
5.string
example:
nums = [10,20,30,40]

for a in nums:
    print(x)

syntax:
iterable_object = [1,2,3,4]
it=iter(iterable_object)
print(it)    

'''
# iterable_object = [1,2,3,4]
# it=iter(iterable_object)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
'''
list
|
iter()
|
iterator

x =[1,2,3,4]

for x in nums:
    print(x)
it = iter(nums)
while True:
     try:
       x = next(it)
       print(x)
    except stopiteration:
    break       
how loop in python works internally
iterators ---will be use
'''
# nums =[1,2,3,4]

# it = iter(nums)
# while True:
#     try:
#        x = next(it)
#        print(x)
#     except StopIteration:
#        break 

# nums = [2,3,4]

# it = iter(nums)
# print(next(it))

name = "python"
# it =iter(name)
# print(next(it))

# t =(1,2,3)
# it = iter(t)
# print(it)

# d = {"a":10,"b":20}
# it =iter(d)
# print(next(it))
# print(next(it))

#no iterator

nums = [i for i in range(100000)]

#huge memory

#iterator approach
nums = iter(range(100000))

#only the current element will be processed

#creating a custom iterator
#count

# class count:
#     #constructor
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         x = self.num
#         self.num+=1
#         return x
# #object creation    
# c = count()

# print(next(c))
# print(next(c))
# print(next(c))


#limit
# class count:
#     #constructor
#     def __init__(self,limit):
#         self.num=1
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num>self.limit:
#             raise StopIteration
#         x = self.num
#         self.num+=1
#         return x
# #object creation    
# c = count(5)

# for i in c:
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







