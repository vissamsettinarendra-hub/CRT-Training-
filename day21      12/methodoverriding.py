'''
#method overriding?
redefining a parent class method inside the child class

-same method name
-same parameters
child class method changes the behaviour of parent class method

speak()
'''
# class Animal:
#     def sound(self):
#         print("animal makes sound")
# class Dog(Animal):
#     #same name as parent class
#     def sound(self):
#         print("dog barks")
# d1 = Dog()
# d1.sound()

'''
#important rule:
method name should be same
'''
'''
super():super function
accessing parent class methods
'''
# class Parent:
#     def show(self):
#         print("parent method")
# class Child(Parent):
#     def show(self):
#         #call the parent method
#         super().show()
#         print("child method")  
# c1 = Child()
# c1.show() 

#is it possible to override the constructor?
# class Parent:
#     def __init__(self):
#         print("parent constructor")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("child constructor")  
# c1 = Child()


# class Parent:
#     def __init__(self,name):
#         self.name = name
# class Child(Parent):
#     def __init__(self,name):
#         super().__init__(name)
#         print("child constructor")  
# c1 = Child("bala reddy ") 
# print(c1.name) 

'''
MRO:method resolution order order in which python searches methods
'''

class A:
    def show(self):
        print("class A")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
c1 = D()
c1.show()
#prints order
print(D.mro())



