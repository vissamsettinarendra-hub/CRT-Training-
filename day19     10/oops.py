'''
oops - object oriented programming (paradigm)

programs are organized  using objects
objects contains:
1.data (variables)
2.behaviour(functions/methods)

oops not only focuses on function but also real world entities
car->object
student->object

each object here:
will have properties and actions
            |             |
            variable     methods

earlier the programming was written without oops

1.difficult to manage the large level projects
2.code duplication 
3.less security
4.difficult maintance

oops solve the above problems
1.classes
2.objects
3.encapsulation
4.inheritance
5.abstraction
6.polymorphism
'''

#procedural programming
# name = "ramya"
# marks = 30
# def display():
#     print(name,marks)
# display()

#oop approach:
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print(self.name, self.marks)

# # Object
# s1 = Student("nani", 44)
# s1.display()   # method call

#data+functions:
'''
advantages:
1.code reuasability
2.better organisation - modular and structure
3.security ->encapulation
4.easy maintenance:update,debug
5.real world modelling
6.scalability:large applications
 



fullstack:
frontend: html,css,js,react js
backend:python,node+express
database:mysql,postresqul,orcale,mongodb
python-flask,django,fastapi,streamlit,gradio
'''
'''
class: blueprint of an object
collection of var, methods??

blueprint:
can be used to build many houses

'''
# class ClassnName:
#     pass

'''
class: keyword creates class
classnames:identifiers
pass:empty block
'''
#object:instance of a class
      #or
#actual memory representation of class

# class Student:
#     pass
# #create an object
# obj = Student
# print(obj)


'''
obj --> instance name (object)
Student-->class name
'''
# class Car:
#     brand = "Audi"
#     #method
#     #self:refers to the current object
#     def start(self):
#         print("car started")
# #create the objects
# #both objects has different memory locations
# c1 = Car()
# c2 = Car()        
# c1.start()
# c2.start()
# c1.brand#class --> object searches for brand inside the class

#task:create a class named as employee
#create var company name and name_employee
#create two methodes to access name and company_name
#create two objects and access var and methodes
# class Employee:
#     company = "moinlal"
#     name_employee = "moin"
#     def num(self):
#         print("company name",self.company)
#     def sum(self):
#         print("employee name",self.name_employee)  
# s = Employee()

# s.num()
# s.sum()

# print(s.company)
# print(s.name_employee) 



'''
constructor: __intit__()
special method
automatically called when object is create
used : initializing the object data

'''
# class Student:
#     def __init__(self):#constructer 
#         print("constructor is called")
# s1 = Student()  

#example with constructor
# class Student:
#     def __init__(self):
#         self.name = "narendra"
#         self.age = 21
# s1 = Student()
# print(s1.name)
# print(s1.age)
        
#constructor with parameters
# class Student:
#     #constructor
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = Student("naredra",30)
# print(s1.name)
# print(s1.age)        

'''step by step
1.object memory allocated
2.__init__ is called automatically
3.self points to object
4.variables initialized
4.object returned
'''
'''
#default constructor
class Test:
      def __init__(self):
          print("default constructor")
t = test()

parametrized constructor

class Test:
    def __init__(self):
        self.x = 100

t = Test()
print(t.x)

constructor                   |      normal method
automatically called                manually call it
name fixed:__init__                 any name
used for initialization            used for opeerations
executes during object            
'''
# class Student:
#     def __init__(self):
#         print("constructor")
#     #normal method
#     def display(self):
#         print("normal method")
# s1 = Student()        
# s1.display()

'''
instance variables:
varibles that belong to the object 
seperate copy created for every object

they store:
object - specific data

student | name | marks|
s1        nani   90
s2        don    95
each object stores its own data

'''
# class Student:
#     def __init__(self,name,marks):
#         #instance variables
#         self.name=name
#         self.marks=marks
# s1 = Student("manoj",95)
# s2 = Student("nani",99)
# print(s1.marks,s1.name)
# print(s2.marks,s2.name)

'''
objects does not share instance variable
'''
#instance methodes:
# class Students:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# #instance method
#     def display(self):
#         print(self.name)
#         print(self.marks)
# s1 = Students("bala",98)
# s1.display()   


'''
#Dyanmic object properties adding the variables dynamically
after creating the object

class Student:
      pass
s1 = Student()

s1.name = "narendra"
'''
# class Student:
#     pass
# s1 = Student()

# s1.name = "narendra"
# s1.age = 21
# print(s1.age,s1.name)

'''
#class variables:
class Student:
    #class variable
    college_name = "city"
    def __init__(self,branch):
        #instance variable
        self.branch
    #normal method
    def display(self):
        print(self.college_name)


'''
#class variables:
# class Student:
#     #class variable
#     college_name = "city"
#     def __init__(self,branch):
#         #instance variable
#         self.branch = branch  #x local variable
#         #wont creates object data
#     #normal method
#     def display(self):
#         print(self.college_name)
# s1 = Student("cse")
# s2 = Student("eece")
# print(s2.college_name)
# print(s1.college_name)  
# s1.display()
'''
self:refers to current object
          or 
      reference variable pointing to current object     
'''
# class Student:
#     def display(self):
#         print("hello")
# s1=Student()
# s1.display()     
'''
s1.display()
   |
   student.display(s1)
   |
   self-s1(self points to s1)
'''  
# class Student:
#     def show(self):
#         print(self)
# s1 = Student()
# s2 = Student()
# print(s1)
# print(s2)
# s1.show()
'''
     student class
     -------------
     college = city#store in class memory
     -------------
     |         |
     s1        s2

class Employee:
     compang = "google"
     def display(self):
        print(self.company)
e = Employee()
two ways access:
print(e.company)
#no object use
print(Employee.company)
        '''

'''
#class methods:
works with class variables operate on class level data

@classmethod - decorator
'''
#basic example for class method
# class Student:
#     college = "city"

#     @classmethod
#     def show_college(cls): 
#         print(cls.college)

# Student.show_college()
'''
@classmethod:
decorator which tells python:
this method belong to class not object

self-->current object
cls-->current class

'''

#task: create a clas named as employee
#create one class var
#use @classmethod to apply
#on method company_name
#print the company name
#using multiple objects
# Create a class named Employee

# class Employee:
#     company = "Google"

#     @classmethod
#     def company_name(cls):
#         print("Company Name:", cls.company)

# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
# e1.company_name()
# e2.company_name()
# e3.company_name()


# class Employee:
#     company = "microsoft"

#     @classmethod
#     def company_name(cls, new_name):
#         cls.company = new_name

# Employee.company_name("google")
# print(Employee.company)       

# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
# e1.company_name()
# e2.company_name()
# e3.company_name()

'''
diff btw instance method and class method
instance method          |      class method
works on object  data            works on class data
uses self                      cls-- current class
need object                    directly using class
access the instance var        access class variable ''' 

# class Student:
#     college = "city"

#     # Instance method: refers to object
#     def instance_method(self):
#         print("instance method")

#     # Class method: refers to class
#     @classmethod
#     def class_method(cls):
#         print("class method") 

'''
static method:
doesn't uses :object, class
they are:
utility/helper methodes

not uses:
self,cls-->
example:
add()
muitiply()

@staticmethod --> decorator
'''

#static method example:
# class Calculator:
#     @staticmethod  #helper method
#     def add(a,b):
#         return a+b
# print(Calculator.add(10,20))  

#independent method
#logically belongs to class but no data required from class
# class Message:
#     @staticmethod
#     def greet():
#         print("hello students")
# print(Message.greet())       

'''
#task:
create a class named as student
create constructor
class variable
instance variables
instance method
class method
static method

'''


class Student:
    college = "City College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    @staticmethod
    def greet():
        print("Welcome to city")
s1 = Student("Narendra", 95)
s2 = Student("Nani", 90)

s1.display()
s2.display()

Student.show_college()

Student.greet()