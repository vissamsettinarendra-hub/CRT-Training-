'''
CSV-->Comma Separated Values
used:excel,reports,databases

Example:
name,age,branch
meghana,20,cse
rahul,22,cse
'''
# import csv

# with open("students.csv","w",newline="") as file:
#     write = csv.writer(file)
#     write.writerow(["Name","Age","Branch"])
#     write.writerow(["Rahul",23,"CSE"])
#     write.writerow(["Sravani",24,"CSE"])
#read csv
# with open("students.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


#binary file handling
# file = open("sixpack.jpg","rb")
# data = file.read()
# print(data)
# file.close()

'''
Task1:count words in a file
with open("data.txt","r") as file:
     content=file.read()
     words=len(content.split())
     print(words)

'''
# with open(r"C:\Users\vissa\Desktop\python class\day24  16\data.txt", "r") as file:
#     content = file.read()
#     words = len(content.split())
#     print("Words:", words)

'''
Task-2:
count the lines in a file
'''
# with open(r"C:\Users\vissa\Desktop\python class\day24  16\data.txt", "r") as file:
#     lines = len(file.readlines())
#     print("Lines:", lines)
'''
task-3:search a word in a file
'''

# word = input("Enter the word: ")

# with open(r"C:\Users\vissa\Desktop\python class\day24  16\data.txt", "r") as file:
#     content = file.read()

# if word in content:
#     print("Word found")
# else:
#     print("Word not found")

# '''
# task 4:copy one file to another
# '''
# Task 4: Copy one file to another

# Task 4: Copy one file to another

# with open(r"C:\Users\vissa\Desktop\python class\day24  16\first.txt", "r") as source:
#     content = source.read()

# with open(r"C:\Users\vissa\Desktop\python class\day24  16\second.txt", "w") as destination:
#     destination.write(content)

# print("File copied successfully")

 
# with open("first.txt", "r") as file1:               wrong
#     content = file1.read()

# with open("second.txt", "w") as file2:
#     file2.write(content)

# print("File copied successfully")

'''
task:
count character in afile
'''
# with open(r"C:\Users\vissa\Desktop\python class\day24  16\data.txt", "r") as file:
#     content = file.read()
#     characters = len(content)
#     print("Number of characters:", characters)


'''
student record management:
a college wants to maintain student
records permently
write a python program to
1.accept student_name and marks
2.store records in a file
named students.txt
3.display all records
4.handle file exception properly
'''


# try:
#     name = input("Enter student name: ")
#     marks = int(input("Enter marks: "))

#     with open("students.txt", "a") as file:
#         file.write(f"{name} - {marks}\n")

#     print("Record saved successfully")

# except ValueError:
#     print("Marks must be a number")

# except Exception as e:
#     print("Error:", e)

# try:
#     print("\nStudent Records:")
    
#     with open("students.txt", "r") as file:
#         for record in file:
#             print(record.strip())

# except FileNotFoundError:
#     print("students.txt file not found")

# except Exception as e:
#     print("Error:", e)


class Studentmanager:
    def add_student(self):
        try:
            name = input("name:")
            marks = input("marks:")
            with open("students.txt","a") as file:
                file.write(name + " " + marks)
            print("records added")
        except Exception as e:
            print(e)
    def display_records(self):
        try:
            with open("students.txt","r") as file:
                content = file.read()
                print("Students records:")
                print(content)
        except FileNotFoundError as e:
            print(e)
o = Studentmanager()
o.add_student()
o.display_records()                                      