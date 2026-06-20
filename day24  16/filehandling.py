'''
files helps store data permanently
file handling:
is a process of
1.creating files
2.reading the files
3.writing files
4.updating files
using python
why file handling?
data disappers after the program ends


with files:
1.store data perm
2.data sharing possible
3.reports/logs can be generate

types of files ???
text files:
1.  .txt
2.  .csv
3.  .py
4.  .json
2.binary files:
1.images
2.videos
3.pdf's

#opening the files:
syntax:
file = open("filename","mode")
'''
# #r will tell to python that
# #line doesnt have any escaping 
# file = open(r"C:\Users\vissa\Desktop\python class\day24  16\data.txt","r")
# print(file)

'''
file modes
mode            meaning
r              reading the file
w              writing
a              append
x              create
r+             read+write
w+             write+read
a+             append+read
rb             read binary
wb             write binary
'''
# try:
#     file = open(r"C:\Users\vissa\Desktop\python class\day24  16\data1.txt","r")
#     data = file.read()
#     print(data)
#     file.close()
#     file.close()
# except FileNotFoundError as e:
#     print("no file found",e)    

#write mode: w
# file = open(r"C:\Users\vissa\Desktop\python class\day24  16\data.txt","w")
# file.write("hello students")
# file.close()


#creates file if not exists
#deletes the old and add new content


#append - mode: adds the data at end
# file = open(r"C:\Users\vissa\Desktop\python class\day24  16\data.txt","a")
# file.write("\nhow are you")
# file.close()


# #create mode - x
# file = open("newfile.txt","x")
# #gives fileexistserror if already available


#read ()
file = open("newfile.txt","r")
print(file.read())
file.close()

#read line()
file = open("newfile.txt","r")
print(file.readline())
file.close()

#3.readlines()-reads multiple lines
file = open("newfile.txt","r")
lines = file.readlines()
print(lines)
#readlines converts into list


#write()-->write the data to file
# file = open("newfile.txt","w")
# file.write("manish\n")
# file.write("rahu\n")
# file.close()


#writelines():write list data
# names = ["rahul\n","anjali\n","rajesh"]
# file = open("newfiles.txt","w")
# file.writelines(names)
# file.close()

#pointer methods:
#returns the current cursor position
#tell()
# file = open("newfiles.txt",'r')
# print(file.tell())
# file.read(5)
# print(file.tell())
# file.close()


#seek():moves the cursor position
# file = open("newfiles.txt","r")
# file.seek(3)
# print(file.read())
# file.close()

#with open()
# with open("newfiles.txt","r") as file:
#     print(file.read())
#automatic closing

#student record system
# name = input("enter student name:")
# marks = input("enter marks")
# with open("newfile.txt","a") as file:
#     file.write(name +  "" + marks+ "\n")    
# print("record saved")


#list --employee details:
# employees = ["narendra 100000","bala 120000","moin 1000000"]
# with open("newfile.txt","w") as file:
#     for emp in employees:
#         file.write(emp + "\n")
# print("report generated")      
'''
CSV-->Comma Separated Values
used:excel,reports,databases

Example:
name,age,branch
meghana,20,cse
rahul,22,cse
'''
import csv

with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["Rahul",23,"CSE"])
    writer.writerow(["Sravani",24,"CSE"])
#read csv
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#  #binary file handling
# file = open("image.jpeg","rb")
# data = file.read()
# print(data)
# file.close()       