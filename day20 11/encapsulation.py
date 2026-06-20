'''
what is encapsulation?
binding data and method together into a single unit

and:
restricting direct access to data

encapsulation protects data from 
1.unauthorized access
2.accidental modifications

similarly in oops :
data is hidden inside the classmaccessed using methods

key idea
data + methodes
    |
combined into a single unit
    |
controlled access

features of encapsulation:
1.security
2.data hiding
3.controlled access
4.better maintenance
5.better organization

'''

#no encapsulation
# balance = 50000

# balance = -50000

#encapsulation
# class Bank:
#     def __init__(self):
#         self.balance = 10000
#     def deposit(self,amount):
#         self.balance +=amount
#     def show_balance(self):
#         print(self.balance)        
# b1 = Bank()  
# b1.deposit(5000)
# b1.show_balance()
 #data  and methods are bound together


 #data hiding
 # #restricting access to direct variables
'''
goal:prevent the data modifications misues of data

access modifiers in python:
1.public
2.protected: _ single _ underscore
3.private: __ double __underscore 
'''
#public:members can be accessible everywhere
#default access type in python
# class Student:
#     def __init__(self):
#         self.name = "narendra"
# s1 = Student()
# print(s1.name) 
'''
access anywhere
no restriction
default behaviour
'''
#protected: _ single _ underscore
#should not be accessed directly outside the class
# 
# class Student:
#     def __init__(self):
#        self._marks = 99
# s1 = Student()
# print(s1._marks)       
'''
python protected members are not exactly protected
_marks: protected by convention

please dont access it directly

where to use?
1.during inheritance
2.for internal  usage'''


'''
private:__ underscore
used for: strong data hiding
'''
# class Student:
#     def __init__(self):
#         self.__marks = 90
# s1 = Student()
# print(s1.__marks)

#name mangling
'''
__marks
|
_Student__marks
'''
'''
prevent:
accidential direct access 
accidential overriding
'''
#can i access private var inside the class
# class Student:
#     def __init__(self):
#         self.__marks = 98
#     def show(self):
#         print(self.__marks)
# s1 = Student()
# s1.show() #accessed within the same class           

#try to access using name mangling
# class Student:
#     def __init__(self):
#         self.__marks = 95
# s1 = Student()
# print(s1._Student__marks)       
'''
self.__marks
   |
python will convert
   |
self._Student__marks
   '''
'''
access modefiers   |   syntax    |   accessible outside
1.public             variables        yes
2.protected         _variable        yes(convention only)
3.private           __variable      no directly
'''
#task
#create a class named "bankaccount"
#balance -->private
#deposit
#withdraw amount
#check for balance
#print balance using name manling

# class BankAccount:
#     def __init__(self):
#         self.__balance = 10000   # private variable

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")

#     def show_balance(self):
#         print("Balance:", self.__balance)


# b1 = BankAccount()

# b1.deposit(5000)
# b1.withdraw(3000)
# b1.show_balance()
# print(b1._BankAccount__balance)

'''
getters and setters:
getter -- read the data
setter --> modify/update the data

#why use?
student.marks = -90
no validation '''
#without getters and setters
# class Student:
#     def __init__(self):
#         self.marks = 99
# s1 =Student()
# s1.marks = -50 #accepted
# print(s1.marks)
 
#using getters and setters
# class Student:
#     def __init__(self):
#         self.__marks = 98
#     #getter method
#     def get_marks(self):
#         return self.__marks
#     #setter method
#     def set_marks(self,value):
#         if value >= 0:
#             self.__marks = value
#         else:
#             print("invalid marks")
# b1 = Student()
# print(b1.get_marks())
# b1.set_marks(95)
# print(b1.get_marks())
# b1.set_marks(-95)
# print(b1.get_marks())

#task:create a class bankaccount
#create getter for returning balance
#create setter for updating balance
#amount >=0

# class Bank:
#     def __init__(self):
#         self.__balance = 10000
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("insufficient balance")
# b1 = Bank()
# print(b1.get_balance())   
# b1.set_balance(15000)  
# print(b1.get_balance())       

# class Student:
#     def __init__(self):
#         self.__marks = 90
#     #getters
#     @property
#     def marks(self):
#         return self.__marks 
#     @marks.setter
#     def marks(self,value):
#         if value > 0:
#             self.__marks = value 
#         else:
#             print("invalid marks")
# s1 = Student()
# print(s1.marks)

# s1.marks = 93
# print(s1.marks)

# s1.marks = -88
# print(s1.marks)

'''
students marks validator
create a class student class
requirements:
private var --> __marks
methode set_marks(marks)
methode get _marks()

rules:
marks must be btw 0 - 100
other wise print

invalid marks
example: input[85]-->85
205--> invalid marks
# '''
# class Student:
#     def __init__(self):
#         self.__marks = 0

#     @property
#     def marks(self):
#         return self.__marks

#     @marks.setter
#     def marks(self, value):
#         if 0 <= value <= 100:
#             self.__marks = value
#         else:
#             print("Invalid marks")


# s1 = Student()

# s1.marks = 85
# print(s1.marks)

# s1.marks = 205
# print(s1.marks)


'''
employee salarly manager
create a class named as employeee
requirements:
1.private var -__salarly
2.salarly should not be < 15000
3.method increase_salary(percent)

if invalid:
invalid salarly

input:20000 
percent:10
output:22000 '''

# class Employee:
#     def __init__(self):
#         self.__salary = 0
#     def set_salary(self,salary):
#         if salary >=15000:
#             self.__salary = salary
#         else:
#             print("invalid salary")
#     def increase_salary(self,percent):
#         self.__salary +=(self.__salary*percent/100)  
#     def get_salary(self):
#         return self.__salary
# salary = int(input())
# percent = int(input())
# e = Employee()
# e.set_salary(salary)
# if salary >= 15000:
#     e.increase_salary(percent)
#     print(e.get_salary())                       
          



'''
password manager
create a class password manager:
rules:
1.minimum 8 characters
2.one uppercase
3.one lowercase
4.one digit

if invalid
weak password
else:
password set succesfully
'''         
# class PasswordManager:
#     def __init__(self):
#         self.__password = ""

#     def set_password(self, password):
#         if (len(password) >= 8 and
#             any(ch.isupper() for ch in password) and
#             any(ch.islower() for ch in password) and
#             any(ch.isdigit() for ch in password)):
            
#             self.__password = password
#             print("Password set successfully")
#         else:
#             print("Weak password")

#     def get_password(self):
#         return self.__password


# p1 = PasswordManager()

# p1.set_password("Narendra123")
# print(p1.get_password())

# p1.set_password("abc")



# class PasswordManager:
#     def __init__(self):
#         self.__password = ""

#     def set_password(self, password):
#         upper = False
#         lower = False
#         digit = False

#         if len(password) < 8:
#             print("Weak password")
#             return

#         for ch in password:
#             if ch.isupper():
#                 upper = True
#             elif ch.islower():
#                 lower = True
#             elif ch.isdigit():
#                 digit = True

#         if upper and lower and digit:
#             self.__password = password
#             print("Password set successfully")
#         else:
#             print("Weak password")

#     def get_password(self):
#         return self.__password


# password = input()

# p = PasswordManager()
# p.set_password(password)
            


'''
task4:
ecommerce shopping cart 
create a class shoppingcart
features:
1.private var -__total
2.add items
3.remove the items
4.apply discount


rules:
1.total should never become zero
2.discount only if total > 1000
methodes
1.add_item(price)
2.remove_item(price)
3.apply_discount(percent)
4.get_total()
'''
# class ShoppingCart:
#     def __init__(self):
#         self.__total = 0

#     def add_item(self, price):
#         if price > 0:
#             self.__total += price
#             print(f"Added item: ₹{price}")

#     def remove_item(self, price):
#         if price > 0 and self.__total - price >= 0:
#             self.__total -= price
#             print(f"Removed item: ₹{price}")
#         else:
#             print("Cannot remove item. Total should not become negative.")

#     def apply_discount(self, percent):
#         if self.__total > 1000:
#             discount = self.__total * percent / 100
#             self.__total -= discount
#             print(f"Discount of {percent}% applied.")
#         else:
#             print("Discount applicable only if total > 1000")

#     def get_total(self):
#         return self.__total


# # Testing
# cart = ShoppingCart()

# cart.add_item(500)
# cart.add_item(800)

# print("Total:", cart.get_total())

# cart.apply_discount(10)

# print("Total after discount:", cart.get_total())

# cart.remove_item(300)

# print("Final Total:", cart.get_total())

class ShoppingCart:
    def __init__(self):
        self.__total = 0

    def add_item(self, price):
        if price > 0:
            self.__total += price
        else:
            print("Invalid item price")

    def remove_item(self, price):
        if 0 <= price <= self.__total:
            self.__total -= price
        else:
            print("Invalid removal amount")

    def apply_discount(self, percent):
        if self.__total > 1000:
            discount = self.__total * percent / 100
            self.__total -= discount
        else:
            print("Discount applicable only if total > 1000")

    def get_total(self):
        return self.__total


# Main Program
cart = ShoppingCart()

n = int(input("Enter number of items: "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    cart.add_item(price)

remove_price = float(input("Enter amount to remove: "))
cart.remove_item(remove_price)

discount = float(input("Enter discount percentage: "))
cart.apply_discount(discount)

print("Final Total:", cart.get_total())