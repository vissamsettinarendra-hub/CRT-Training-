
'''
Error:An erroe is a problem in the program causing abnormal termination
1. Syntax Error(Mistakes in code i.e human made)
2. Run time Errors ---Exceptions
    ---> Occurs while executing 
Eg : 
a = 10
b = 0
c = a/b --->Zero Division error

3. Logical Errors:
Program runs but gives wrong output

Eg:
print(2*(3+5))

what is exception handling ?
Exception hadling is a mechanisa, to handle runtime errors 

without exceptions 
1. program crashe
2. poor user experince
3. Data loss possible 

with exception:
1.progrma will execute normally
2.proper error message
3.safer application

# Basic syntax for Exception:

syntax:

keyword:try,catch,finally,raise


try :
    risky code
except:
    handiling code

'''#let write our first program
# try 
#risk code will be inside try
#if exception occurs ->execpt executs 

#above is not a good practice
#hides actual problem
#diffcult to debug
# try:
#     num = int(input("enter the number"))
#     print(10/num)
# except ZeroDivisionError:
#     print("cannot divide with 0")
# except ValueError:
#     print("input should not be a string")

'''
commom python exception:
1.ZeroDivisionError --->Divide with 0
2.ValueError--->Invalid input
3.TypeError -->wrong datatype
4.IndexError--> Invalid Index
5.KeyError--> Invalid dictionary key
6.FileNotFoundError--->File Missing
7.AttributeError --->Invalid Attribute
8.NameError--->Variable is not desfined
'''

#example:
# try:
#     l = [30,50,40]
#     index  = int(input("enter the index:"))
#     print(l[index])
# except IndexError:
#     print("Index out of range")
# except ValueError:
#     print("please enter the integer")         


'''#else: if no execption occurs
# try:
#     Code
# except:
#     handling
# else:
#     success  
''' 


#example:
# try:
#     l = [30,50,40]
#     index  = int(input("enter the index:"))
#     print(l[index])
# except IndexError:
#     print("Index out of range")
# except ValueError:
#     print("please enter the integer")         

# else: 
#     print("no execption occured")        

#another example:
# try:
#     num  = int(input("enter number:"))
#     result = 100/num
# except ZeroDivisionError:
#     print("Zero")
# else:
#     print(result)        

#finally
'''
finally block executes always
used for:
'''
# try:
#     num  = int(input("enter number:"))
#     result = 100/num
# except ZeroDivisionError:
#     print("Zero")
# else:
#     print(result)   
# finally:
#     print("execution completed")    

#ATM machine:
# try:
#     print("transation is processing")
# except:
#     print("transaction failed")
# finally:
#     print("thaks for using ATM")

# try:
#     a = 10/0
# except ZeroDivisionError as e:
#     print("error:",e)       

# try:
#     print("outer try")
#     try:
#         num = int(input("enter the number"))
#         print(10/num)
#     except ZeroDivisionError as e:
#         print("error:",e)
# except:
#     print("outer exception")

#raise:used to manually
#generate exception

# age = int(input("enter the age:"))
# if age<18:
#     raise ValueError("age should be 18 or grater")
# print("eligible")

#why custom exceptions;
# class MyException(Exception):
#     pass

#bank applications:

# class Insufficientbalance(Exception):
#     pass
# balance = 5000
# withdraw = int(input("enter the amount"))
# if withdraw > balance:
#     raise Insufficientbalance("not enough balance")
# print("withdraw successfull")

# class InvalidAgeError(Exception):
#     pass

# try:
#     age = int(input("Enter age: "))

#     if age < 18:
#         raise InvalidAgeError("Age must be 18 or above")

#     print("Eligible to vote")

# except InvalidAgeError as e:
#     print("Error:", e)

#exception with oops concept
#exceptions are mostly used with methods

#student result system
# class Student:
#     def __init__(self,marks):
#         self.marks = marks
#     def calculate_result(self):
#         try:
#             average = sum(self.marks)/len(self.marks)    
#             print(average)
#         except ZeroDivisionError as e:
#             print("error:",e)
# s1 = Student([])
# s1.calculate_result()                

#login system:
# class Loginsystem:
#     def login(self,username,password):
#         try:
#             if username !="Moin":
#                 raise ValueError("invalid username")
#             if password != "Moin2004@$":
#                 raise ValueError("invalid password")
#             print("login successful")
#         except ValueError as e:
#             print("error:",e)
# l = Loginsystem()


#generic exceptions:
# try: 
#     print(10/0)
# except Exception as e:
#     print(e)    


'''
task:
accept account balance and withdrawl amount
rasie exception if:
1.withdrawl amount is -ve
2.withdrawl amount exceeds balance
3.withdrawl amount exceeds daily
limit of 25000
4.display remaining balance if transaction successful
'''
# class InvalidWithdrawal(Exception):
#     pass

# class InsufficientBalance(Exception):
#     pass

# class DailyLimitExceeded(Exception):
#     pass

# try:
#     balance = float(input("Enter account balance: "))
#     withdraw = float(input("Enter withdrawal amount: "))

#     if withdraw < 0:
#         raise InvalidWithdrawal("Withdrawal amount cannot be negative")

#     if withdraw > balance:
#         raise InsufficientBalance("Withdrawal amount exceeds account balance")

#     if withdraw > 25000:
#         raise DailyLimitExceeded("Daily withdrawal limit is 25000")

#     balance -= withdraw
#     print("Transaction Successful")
#     print("Remaining Balance:", balance)

# except InvalidWithdrawal as e:
#     print("Error:", e)

# except InsufficientBalance as e:
#     print("Error:", e)

# except DailyLimitExceeded as e:
#     print("Error:", e)