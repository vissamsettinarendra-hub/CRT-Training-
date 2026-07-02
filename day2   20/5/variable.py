x = 100
print(x)

_name = "Manish"  #valid
print(_name)

#2name : should not start with numbers

first_name = "Manish" #valid

# @name : should not start with special characters

age = 26
Age = 28 #case sensitive

print(Age)

# if : keywords cannot be used as variables names

#input by default takes strings
a = input("enter the value")
b = input("enter the number")
print(a+b)
#10
#20
#1020

#typecasting:conversion of one dt another
x = int(input("enter the value of x:"))
y = int(input("enter the value of y"))
print(x+y)

name = input("enter the name")
print("hello",name)

#string ----> float
price = float(input("enter the price"))
print(type(price))

#int ---> string

x = str(100)

#write a program to perform avg of a number:

x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
z = int(input("enter the value of z:"))

avg = (x+y+z)/3

print(avg)