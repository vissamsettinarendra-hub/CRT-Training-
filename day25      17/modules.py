'''
module:
a module is simple a python 
file containing code

why?
1.large file
2.hard to maintain
3.diffcult to resue

modules:
reusability
organinzation
readability
collaboratio
'''
# import calculator

# print(calculator.add(1,2))
# print(calculator.sub(20,5))

#task: create a module named as greeting
# import greeting
# greet1 = greeting.greet()
# print(greet1)

# #task
# from day20 11 import new
# print(new.hello())

#built in methods
import math
print(math.sqrt(33))
print(math.factorial(5))


#from import 
from math import sqrt,pow
sqrt(3)
pow(2,2)

#all the attributes from math
from math import*
# from looping import new
# new.hello()

#collection of modules is called package
import datetime as dt
print(dt.datetime.now())

'''
module         meaning
1.math          mathematices
2.random        randomvalues
3.date&time     datetime
'''
'''
#package:
package is afolder containing multiple modules
school/
  student.py
  teacher.py
  management.py

main.py-->from school import student

__init__.py
purpose:
special file used to identfy package
1.marks directory as package
2.runs initializzation code
3.control the import

'''
# #importing from package
# from school import student
# student.show_student()

#builtin methods
import math
#round upward
print(math.ceil(5.2))

#floor()-->
print(math.floor(5.2))

#constants
print(math.pi)
print(math.e)

#task:area of circle 
import math
r = 7
area = math.pi*r*r
print(area)

#random builtin methode
#used for random values

import random
#randint()
print(random.randint(1,100))

#choice()
fruits = ["Apple","Banana","Pineapple"]
print(random.choice(fruits))

#random()--->0.0 - 1.0
print(random.random())

#shuffle()
cards = [1,2,3,4]
random.shuffle(cards)
print(cards)


#task: built the dice simulator
import math
print(random.randint(1,6))


#date?
import datetime
print(datetime.date.today())

#custome date
d = datetime.date(2026,6,18)
print(d)

#build the age calculator
import datetime
birth_year = 2006
current_year = datetime.date.today().year
print(current_year-birth_year)