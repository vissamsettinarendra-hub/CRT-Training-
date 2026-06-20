'''
what is abstraction?
hiding the internal implementation details
showing the essential features to user
                            or
                        what operation is done
                        how it does?
                        but not:
                        how operation is working internally
--->complexity is hidden from the user

why we use abstraction?
1.reduces the complexity
2.improves the security
3.better maintenance
4.cleaner code
5.standardization

#abstraction in python
python supports abs using
abstract classes
abstract methods

#ABC module
ABC --  adstract base class 

abstract class:
blueprint of a class
cannot creat object directly

#define basic common structure 

abstract can have:
1.abs methods
2.normal method


#abs method
method declared but:
      implementation not provided
child class must implement it 
example:
vechile

-->start()

'''

#ABC--->abstract base class
from abc import ABC,abstractmethod
#abstract class
# class Vehicle(ABC):
#     #abstract method
#     @abstractmethod
#     def start(self):
#         pass
# v = Vehicle() 

# class Vehicle(ABC):
#     #abstract method
#     @abstractmethod
#     def start(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("car started")
# c = Car()    
# c.start()

#example:2
from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# d = Dog()
# d.sound()

#multiple abstract methods
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Rectangle(Shape):
#     def area(self):
#         print("area formula")
#     def perimeter(self):
#         print("perimeter formula")
# a1 = Rectangle()
# a1.area()
# a1.perimeter()                

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#     #normal method
#     def sleep(self):
#         print("sleeping")
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# d2 = Dog()
# d2.sound()
# d2.sleep()                
  
#payment system
#pay()
# class Paymentgetway(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class Phonepay(Paymentgetway):
#     def pay(self):
#         print("paid using phonepay")
# class Paytm(Paymentgetway):
#     def pay(self):
#         print("paid using paytm")            
# pp = Phonepay()
# pt = Paytm()
# pp.pay()
# pt.pay()

'''
task:
create an abstract class paygateway
with two methods
1.pay
2.refund
but amount -- : parameter
create child class implementations
1.creditcardpay
2.upi pay'''

# class Paygateway(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     def refund(self,amount):
#         pass
# class Creditcardpay(Paygateway):
#     def pay(self,amount):
#         print(f"paid {amount} using card")  
#     def refund(self,amount):
#         print(f"refund {amount} to card")
# class Upipay(Paygateway):
#     def pay(self,amount):
#         print(f"paid {amount} using upi")
#     def refund(self,amount):
#         print(f"refund {amount} to upi")
# cc = Creditcardpay()
# upi = Upipay()

# cc.pay(500)
# cc.refund(200)

# upi.pay(1000)
# upi.refund(300)            

'''
task
create an abstract class employee
with abs methods:
calculate_salarly()
create:
fulltimeemployee
parttimeemployee
rules:fulltimesalary = 50000
parttimesalary = hours*500    '''

# class Employee(ABC):

#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class Fulltimeemployee(Employee):

#     def calculate_salary(self):
#         print("Salary:", 50000)

# class Parttimeemployee(Employee):

#     def __init__(self, hours):
#         self.hours = hours

#     def calculate_salary(self):
#         print("Salary:", self.hours * 500)

# hours = int(input())

# f = Fulltimeemployee()
# p = Parttimeemployee(hours)

# f.calculate_salary()
# p.calculate_salary()

'''
create an abstract class restaurant with methods:
prepare_food()
dlivery_time()
create child classes:
1.pizzashop
2.burgerr shop
display:
food preperation message 
delivery time
'''
# class Restaurant(ABC):

#     @abstractmethod
#     def prepare_food(self):
#         pass

#     @abstractmethod
#     def delivery_time(self):
#         pass

# class PizzaShop(Restaurant):

#     def prepare_food(self):
#         print("Preparing Pizza")

#     def delivery_time(self):
#         print("Delivery Time: 30 minutes")


# class BurgerShop(Restaurant):

#     def prepare_food(self):
#         print("Preparing Burger")

#     def delivery_time(self):
#         print("Delivery Time: 20 minutes")

# p = PizzaShop()
# b = BurgerShop()

# print("Pizza Shop")
# p.prepare_food()
# p.delivery_time()

# print("\nBurger Shop")
# b.prepare_food()
# b.delivery_time()


'''
ride booking application
class-->ride
method:
calculate_fare(distance)
child:
1.bikeride
2.carride
3.autoride
rules:
bike-->distance*10
car-->distance*20
auto-->distance*15
'''

# class Ride(ABC):
#     @abstractmethod
#     def calculate_far(self, distance):
#         pass

# class Bikeride(Ride):

#     def calculate_far(self, distance):
#         return distance * 10

# class Carride(Ride):

#     def calculate_far(self, distance):
#         return distance * 20

# class Autoride(Ride):

#     def calculate_far(self, distance):
#         return distance * 15


# distance = int(input())

# bike = Bikeride()
# car = Carride()
# auto = Autoride()

# print(bike.calculate_far(distance))
# print(car.calculate_far(distance))
# print(auto.calculate_far(distance))

'''
magic method /dunder methods
dunder-->double underscore
__double underscores
example:__init__
        __add__
why?
operator overloading    
+


-
/

print(10+10)#20
print("hello"+"world")#helloworld
'''  
#+
# class Number:
#     def __init__(self,value):
#         self.value = value
#     def __add__(self,other):
#         return self.value + other.value
# n1 = Number(20)
# n2 = Number(10)
# print(n1+n2)  
#make your objects work
# like built in type        


#string:
# class Student:
#     pass
# s1 = Student()
# print(s1)

#__str__
# class Student:
#     def __str__(self):
#         return "student object"
# s1 = Student()
# print(s1)

#len() method
# class Team:
#     def __len__(self):
#         return 5
# t1 = Team()
# print(len(t1))    

#==__equ__
# class Students:
#     def __init__(self,marks):
#         self.marks = marks
#     def __equ__(self,value):
#         return self.marks == value.marks    
# s1 =Students(90)
# s2 = Students(90)
# print(s1==s2)    

#repr -->official objecct repersentation
#debugging
#development

class Student:
    def __repr__(self):
        return "hello"
s1 = Student()
print(repr(s1))    
