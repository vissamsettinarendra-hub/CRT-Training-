'''what is inheritance ?
It is a mechanisam where one class acquires the propertys of another class.
                        OR
One class reuses the features and propertys of another class

Simple Undersatnding of Inheritance :
A child class can use variables and methods of parent class without wrinting code or progrma


Example: 
vehicals:
car, bike, bus

All vehicles have to be start(),stop()
No needed to write repeated code for different type of vehicles

write code once 
    |
    |
use no of times

Importence or Advantages or Why Inheritance

1. Code reusability
2. Reducing the code duplication
3. Better Organisation
4. Eassy maintainence


Terms:
parent-> Base class or super class
child-> sub class or derived class


            parent
              |
            child

'''

# Syntax
# class parent:
#     pass

# class child(parent):
#     pass

# Basic Example:
# class Animal:
#     def eat(self):
#         print("Animal is eating.")

# # child class
# class dog(Animal):
#     pass

# d = dog()
# d.eat()

'''
Dog class does not contain eat()
            |
    python searches in animal class
            |
    method is found and executed

'''

# no inheritance

# class dog:
#     def eat(self):
#         print("Eating")

# class cat:
#     def eat(self):
#         print("Eating")


# with inheritance 

# class Animal:
#     def eat(self):
#         print("Eating")

# class dog(Animal):
#     pass
# class cat(Animal):
#     pass
# c1 = cat()
# c1.eat()

#accessing the parent variables
# class Person:
#     def __init__(self):
#         self.name="glory"
# class Student(Person):
#     pass
# s1 = Student()
# print(s1.name)      
'''
types of inheritance in python:
1.single   inheritance
2.multiple  inheritance
3.multilevel  inheritance
4.hierarichal  inheritance
5.hybrid   inheritance

1.single   inheritance:
one child class inherites one parent
           parent
           |
           child

 '''
#example:
# class Animal:
#     def eat(self):
#         print("eating")
# class Dog(Animal):
#     def bark(self):
#         print("barking")
# d1 = Dog()
# d1.eat()
# d1.bark()  

'''
#2.multiple inheritance:
one child class inherits from multiple parents
           parent1      parent2
              \\          /
                 child

'''
# #example:
# class Father:
#     def money(self):
#         print("father's money")
# class Mother:
#     def gold(self):
#         print("mother's gold")
# class Child(Father,Mother):
#     pass
# c1 = Child()
# c1.money()
# c1.gold()


'''
#3.multilevel inheritance
inheritance chain of multiple levels
              grandparent
              |
              parent
              |
              child
'''
#example:
# class Gandparent:
#     def house(self):
#         print("grand parent house")
# class Parent(Gandparent):
#     def car(self):
#         print("parents car")
# class Child(Parent):
#     def bike(self):
#         print("child's bike")
# c1 = Child()
# c1.house()
# c1.car()
# c1.bike()                


'''
4.hierarichal  inheritance:
multiple child classes inherit from one parent
             parent
             /     \\
           child1   child2

'''
# class Animal:
#     def eat(self):
#         print("eating")
# class Dog(Animal):
#     def bark(self):
#         print("barking")
# class Cat(Animal):
#     def meow(self):
#         print("meow")
# c1 = Cat()
# c1.eat()

'''
5.hybrid   inheritance
two or more inheritance types
hierarichal  and multiple

                    A
                   /  \\
                  B    C
                  \\   /
                     D
                     '''
#example:
# class A:
#     def show_a(self):
#         print("class A")
# class B(A):
#     def show_b(self):
#         print("class B")
# class C(A):
#     def show_c(self):
#         print("class C")
# class D(B,C):
#     def show_d(self):
#         print("class D")
# d1 = D()
# d1.show_a()
# d1.show_b()
# d1.show_c()
# d1.show_d() 


#check the inheritance
# class Animal:
#     pass
# class Dog(Animal):
#     pass
# c1 = Dog()
# print(isinstance(c1,Dog))
# print(issubclass(Dog,Animal))

# class Parent:
#     def __init__(self):
#         print("constructor called")
# class Child(Parent):
#     pass
# c1 = Child()        
'''
1.methods
2.variables
3.constructor
'''

'''
create a parent class animal with method sound()
that should print animal makes sound

create a child class dog()
that inherits the animal

create object of dog and call
inherited sound()
'''
# class Animal:
#     def sound(self):
#         print("animal make sound")
# class Dog(Animal):
#     pass
# c1 = Dog()
# c1.sound()


'''
task:
student and college
create a parent class college
class -->college name
create a child class student with:
instance var-->student_name
display:
1.college_name
2.student_name
'''
# class College:
#     def name1(self):
#         print("city")
# class Student(College):
#     def name2(self):
#         print("bala reddy")
# c1 = Student()
# c1.name1()
# c1.name2()


# class College:
#     college_name = "city"

# class Student(College):
#     def __init__(self, student_name):
#         self.student_name = student_name

#     def display(self):
#         print(self.college_name)
#         print(self.student_name)

# s1 = Student("bala reddy")
# s1.display()


'''
task:
create:
vechicle class with method start()
car class inheriting vehicle
sportscar class inheriting the car
add method:
speed()
inside the sports car:
call:
start()
speed( using sportscar object)'''
# class Vehicle:
#     def start(self):
#         print("vehicle started")
# class Car(Vehicle):
#     pass
# class Sportscar(Car):
#     def speed(self):
#         print("speed")
# sp = Sportscar()
# sp.start()
# sp.speed()

'''
employee skill system
create:
class programmer with method coding()
class designer with method designing()
create a child class employee inheriting
both classes
call both methods using employee objects
'''
# class Programmer:
#     def coding(self):
#         print("coder")
# class Designer:
#     def designing(self):
#         print("designer")
# class Employee(Programmer,Designer):
#     pass
# c1 = Employee()
# c1.coding()
# c1.designing()                


'''
task:
Employee Bonus Mgmt
A company wants to calc
yearly bonuses for 
different types of employees 

create a base class Employee:
with:
name , salary 
create method:
calculate bonus()

then create two child classes 
developer
Bonus = 20% of salary 
manager 
Bonus = 35% of salary 
write a program to:
1.Take employee details as input
2.create objects based on employee type
3.Display:
employee name 
role
Bonus amount 

input format:
role,name,salary

output format:
Name:<name>
Role:<role>
Bonus:<bonus>

Sample:
3
Developer Rahu1 50000
Manager   Sneha 80000
Developer Arjun 60000

output:
Name:Rahul
Role:Developer
Bonus:10000.00    '''
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def calculate_bonus(self):
#         return 0


# class Developer(Employee):
#     def calculate_bonus(self):
#         return self.salary * 0.20


# class Manager(Employee):
#     def calculate_bonus(self):
#         return self.salary * 0.35


# n = int(input())

# for _ in range(n):
#     role, name, salary = input().split()
#     salary = float(salary)

#     if role == "Developer":
#         emp = Developer(name, salary)
#     elif role == "Manager":
#         emp = Manager(name, salary)

#     print(f"Name:{emp.name}")
#     print(f"Role:{role}")
#     print(f"Bonus:{emp.calculate_bonus():.2f}")

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def calculate_bonus(self):
#         return 0


# class Developer(Employee):
#     def calculate_bonus(self):
#         return self.salary * 0.20


# class Manager(Employee):
#     def calculate_bonus(self):
#         return self.salary * 0.35


# n = int(input())
# employee = []

# for _ in range(n):
#     role, name, salary = input().split()
#     salary = int(salary)

#     if role == "Developer":
#         emp = Developer(name, salary)
#     elif role == "Manager":
#         emp = Manager(name, salary)

#     employee.append((role, emp))

# for role, emp in employee:
#     print(f"Name:{emp.name}")
#     print(f"Role:{role}")
#     print(f"Bonus:{emp.calculate_bonus():.2f}")
#     print() 


# class Course:
#     def __init__(self, student_name):
#         self.student_name = student_name

#     def access_level(self):
#         pass


# class FreeCourse(Course):
#     def access_level(self):
#         return "Limited Access"


# class PremiumCourse(Course):
#     def access_level(self):
#         return "Full Access"


# n = int(input())

# students = []

# for _ in range(n):
#     course_type, student_name = input().split()

#     if course_type == "Free":
#        obj = FreeCourse(student_name)
#     elif course_type == "Premium":
#         obj = PremiumCourse(student_name)

#     students.append((course_type, obj))

# for course_type, obj in students:
#     print(f"Student:{obj.student_name}")
#     print(f"Course_type:{course_type}")
#     print(f"Access:{obj.access_level()}")
#     print()
#     print()

               
           
