'''
task:
A company wants to generate employee salary reports
write a program to:
1.Accept employee details
2.Store them in employee.txt
3.calculate total salary expenditure
(total=0+salary)
4.display employee report
sample input:
enter the employee name: meghana
enter the salary:50000

output:
Employee Report
meghana 50000
Total expenditure:50000
'''
class Employeereport:
    def add_employee(self):
        try:
            name = input("enter the name:")
            salary = float(input("enterr the salarly:"))
            with open("employee.txt","a") as file:
                file.write(name + " " + str(salary)+"\n")
            print("employee added") 
        except ValueError as e:
            print("invalid input",e)
    def genertate_report(self):
        total = 0
        try:
            with open("employee.txt","r") as file:
                for line in file:
                    name,salary = line.split()
                    print(name,salary)
                    total += float(salary)   
            print("total expenditure:",total)
        except FileNotFoundError:
            print("employee file missing")       
o =Employeereport()
o.add_employee()
o.genertate_report()                


'''
task:
word frequency analyzer
a company wants to analyze the text
write a python program:
1.read contents from data.txt
2.count the frequency of each word
3.display most repeated words
4.handle the exception'''


# class WordAnalyzer:

#     def analyze(self):
#         try:
#             with open("data.txt", "r") as file:
#                 content = file.read().lower()

#             words = content.split()

#             freq = {}

#             for word in words:
#                 freq[word] = freq.get(word, 0) + 1

#             print("Word Frequencies:")

#             for word, count in freq.items():
#                 print(word, count)

#             max_word = max(freq, key=freq.get)

#             print("Most Repeated Word:", max_word)
#             print("Frequency:", freq[max_word])

#         except FileNotFoundError:
#             print("data file missing")

#         except Exception as e:
#             print("Error:", e)


# o = WordAnalyzer()
# o.analyze()



# class WordAnalyzer:

#     def analyze(self):
#         try:
#             with open("data.txt", "r") as file:
#                 content = file.read().lower()

#             words = content.split()

#             freq = {}

#             for word in words:
#                 if word in freq:
#                     freq[word] +=1
#                 else:
#                     freq[word] = 1
#             print("word frequuencies")
#             for key,value in freq.items():
#                 print(key,":",value)
#             maximum = max(freq,key=freq.get)
#             print("most repeated word",maximum)
#         except FileNotFoundError as e:
#             print("file not found",e)
# o = WordAnalyzer()
# o.analyze()                              


'''
login authentication system
a company wants to store user credentials
write a program:
1.take the input from the users.txt
2.login using username and password
3.validate the credentials from file
4.handle invalid login attempts
'''
# class Loginauthentication:
#     def register(self):
#         try:
#             username = input("enter the username")
#             password = input("enter the password")
#             with open("users.txt","a") as file:
#                 file.write(username + " " + password+"\n")
#             print("registration successful")
#         except ValueError as e:
#             print("invalid user",e)
#         except ValueError as e:
#             print("invalid password",e)
#     def login(self):
#         try:
#             username = input("enter the username:")
#             password = input("enter the password:")
#             found = False
#             with open("users.txt","r") as file:
#                 for line in file:
#                     u,p = line.strip().split()
#                     if (username == u and password == p):
#                         found = True
#                         break
#             if found:
#                 print("login successful")
#             else:
#                 print("invalied credentials")
#         except FileNotFoundError as e:
#             print(e)
# o = Loginauthentication()
# o.register()
# o.login()           


'''
task:
a company stores sever logs in a file 
write a python program:
1.read log.txt
count:
total lines
error messages
warning messages
info messages
display analysis report

log format:
C
error database failed
warning low memory

report:
count?
'''
class Severlog:
    def sever(self):
        try:
            with open("log.txt","r") as file:
                lines = file.readlines()

                ERROR_count =0 
                WARNING_count = 0
                INFO_count = 0
                for line in lines:
                    if 'ERROR' in line:
                        ERROR_count +=1
                    elif 'WARNING' in line:
                        WARNING_count +=1
                    elif 'INFO' in line:
                        INFO_count +=1
                print("LOg report")
                print("totallines:",len(lines)) 
                print(ERROR_count)
                print(WARNING_count)
                print(INFO_count)
        except FileNotFoundError as e:
            print(e)
o = Severlog()
o.sever()                       


    

