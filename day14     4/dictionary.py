'''
what is dict?
mutable-->can be modified
tuple-->collection of ordered elements
immutable-->can't be modified

dict:collection of key valuenpairs
dict={}
#dict is mutable and immtable
# here keys are immutable and values are mutable
# not allow duplicates of -->keys
# values can be duplicates --->values 

no fixed indexing
timecomplexity is:O(1)
uses hashing technique to search hence O(1)

why we use dict?
1.labels
2.properties
3.mapping the relationships 
example 
list = ["narendra",23,21]
#creation of dictionary
student ={
        "name":"narendra",
        "rollno":23,
        "age":21}
'''
# student ={
#         "name":"narendra",
#         "rollno":23,
#         "age":21
# }
# print(student)

#another formate
# student = dict(name = "ramya",age=21,branch="cse")
# print(student)

# #another formate
# data = {}
# print(data)


# print(student["name"])
# print(student["age"])

'''
features      list      dict
ordered        yes      no
access(indexing)yes     key no
arr[0]          yes     student[key]'''

employee = {}
employee["name"]="lokesh"
employee["age"]=21
print(employee)

#update the value
student = dict(name = "ramya",age=21,branch="cse")
print(student)
# employee["age"]=24
# print(employee)


#delete the value
# employee.pop("age")
# print(employee)

#2nd method delete
# del student["branch"]
# print(student)

#dictionary methodes
# key()--->returns the key
# print(student.key())

#values()--->return all the values
# print(student.values())

#items()--> return all the items in dict
print(student.items())

#access  the elements
print(student.get("branch"))


#update()--->to add multiple elements
student.update({"roll no": 40,"college":"city"})
print(student)

#popitem:removes the last inserted pair
student.popitem()
print(student)


#looping on dict
for i in student:
    print(i)

#iterating on values 
for value in student.values():
    print(value)   
for key,value in student.items():
    print(key,value) 


#nested dict:dict inside the dict     
students = {
    "s1":{
        "name":"nani",
        "branch":"ds"
    },
    "s2":{
        "name":"manoj",
        "branch":"ece"
    }
}
print(students)   
print(students["s1"]["name"])


#can i store list inside the dict?
student = {
    "name":"sai",
    "marks":[40,60,89,76]
}
print(student)

#you can store multiple dict in list
students = [
    {"name":"don","branch":"ece"},
    {"name":"moon","branch":"cse"}
]
students[0]["name"]
print(students)
print(students[0]["name"])

#dict comprehension

#{key:values for variables in iterable}
squares = {x:x*x for x in range(1,11)}
print(squares)

#keys: rules
'''
int
string
tuple
list-->you can't use
dict -->

student = {
1:"nani",
"roll no":23,
(1,2):"tuple",
[1,2,3]:"list"#can't use
{"name":"nani"}:"hello"#cant use
}'''

'''
'''