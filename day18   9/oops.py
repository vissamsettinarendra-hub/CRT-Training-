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
class Employee:
    company = "moinlal"
    name_employee = "moin"
    def num(self):
        print("company name",self.company)
    def sum(self):
        print("employee name",self.name_employee)  
s = Employee()

s.num()
s.sum()

print(s.company)
print(s.name_employee) 