'''
a university wants to automate student
result processing
the program should accept:
1.marks of 5 subjects
2.raise exception
if
1.marks are negative
2.marks exceed 100
3.non numeric input
4.calculate average and grade
rules:
avg >= 75 ->distinction
avg >= 60 ->first class
avg >= 40 ->pass'''
# class NegativeMarksError(Exception):
#     pass

# class MarksExceedError(Exception):
#     pass


# marks = []

# try:
#     for i in range(1, 6):
#         m = float(input(f"Enter marks of subject {i}: "))

#         if m < 0:
#             raise NegativeMarksError(
#                 "NegativeMarksError: Marks cannot be negative."
#             )

#         if m > 100:
#             raise MarksExceedError(
#                 "MarksExceedError: Marks cannot exceed 100."
#             )

#         marks.append(m)

#     avg = sum(marks) / 5

#     print("Average =", avg)

#     if avg >= 75:
#         print("Grade: Distinction")
#     elif avg >= 60:
#         print("Grade: First Class")
#     elif avg >= 40:
#         print("Grade: Pass")
#     else:
#         print("Grade: Fail")

# except ValueError:
#     print("ValueError: Non-numeric input is not allowed.")

# except NegativeMarksError as e:
#     print(e)

# except MarksExceedError as e:
#     print(e)

# class Invalidmarkserror(Exception):
#     pass
# class Student:
#     def __init__(self):
#         self.marks = []
#     def input_marks(self):
#         try:
#             for i in range(5):
#                 marks = int(input(f"enter subject {i+1} marks"))
#                 if marks <  0 or marks > 100:
#                   raise Invalidmarkserror("marks should be blw 0 and 100 ")
#                 self.marks.append(marks)
#             average = sum(self.marks)/5
#             print("average:",average)
#             if average >= 75:
#                 print("distinction")
#             elif average >= 60:
#                 print("first class")
#             elif average >= 40:
#                 print("pass")
#             else:
#                 print("fail")
#         except ValueError:
#             print("only numerics are allowed")
#         except Invalidmarkserror as e:
#             print(e) 
# o = Student()
# o.input_marks()                                

'''
task:
an ecomers company validate order processing
the system should accepet
1.product stock
2.payment status
3.delivery address
raise exception if:
1.stock unavailable
2.payment failed
3.address is empty
if all vaidation pass:
    print("order successfully placed")
    
    '''
# class InvalidProductStock(Exception):
#     pass

# class PaymentFailed(Exception):
#     pass

# class EmptyAddress(Exception):
#     pass


# class Order:
#     def process_order(self):
#         try:
#             stock = int(input("Enter product stock: "))
#             payment = input("Enter payment status: ")
#             address = input("Enter delivery address: ")

#             if stock <= 0:
#                 raise InvalidProductStock("Stock unavailable")

#             if payment.lower() != "success":
#                 raise PaymentFailed("Payment failed")

#             if address.strip() == "":
#                 raise EmptyAddress("Address is empty")

#             print("Order successfully placed")

#         except ValueError:
#             print("Stock should be numeric")

#         except InvalidProductStock as e:
#             print(e)

#         except PaymentFailed as e:
#             print(e)

#         except EmptyAddress as e:
#             print(e)


# o = Order()
# o.process_order()


# class Outofstockerror(Exception):
#     pass
# class paymentfailederror(Exception):
#     pass
# class Invalidaddresserror(Exception):
#     pass
# class Order:
#     def __init__(self,stock,payment_status,address):
#         self.stock = stock
#         self.payment_status = payment_status
#         self.address = address
#     def place_order(self):
#         try:
#             if self.stock <=0:
#                 raise Outofstockerror("product is unavaliable")   
#             if not self.payment_status:
#                 raise paymentfailederror("payement is failed")
#             if self.address.strip() == "":
#                 raise Invalidaddresserror("address can not be empty")
#             print("order placed successfully")
#         except Outofstockerror as e:
#             print(e)
#         except paymentfailederror as e:
#             print(e)
#         except Invalidaddresserror as e:
#             print(e)
# stock = int(input("Enter stock: "))
# payment = input("payment status(yes/no): ")
# address = input("Enter address: ")
# payment_status = payment == "yes"

# o = Order(stock, payment_status, address)
# o.place_order()                        


'''
task:
a company wants to create a
file anazyler tools
the program should accept
1.accepet file name from user
handle:
1.file not found
2.permissin denied
3.empty file
display:
number if lines:len(file.splitlines())
number of words:len(file.split)
number of characters'''
# class EmptyFileError(Exception):
#     pass
# class FileAnalyzer:
#     def analyzer(self,filename):
#         try:
#             file = open(filename)
#             content = file.read()

#             if content.strip() == "":
#                 raise EmptyFileError("File is empty")
#             lines = len(content.splitlines())
#             words = len(content.split())
#             characters = len(content)
#             file.close()
#             # Disply the outputs
#             print("Lines : ",lines)
#             print("Words : ",words)
#             print("characters : ",characters)

#         except (FileNotFoundError, EmptyFileError, PermissionError) as e:
#             print(e)

# filename = input("Enter the fileName : ")
# f = FileAnalyzer()
# f.analyzer(filename)
