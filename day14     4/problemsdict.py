'''
text = "apple banana pineapple strawberry banana apple"

find the frequency of words?
store in dict
output= {"apple":2,"banana:2","pineapple":1,"strawberry":1}
'''
# text = "apple banana pineapple strawberry banana apple"
# freq = {}
# for word in text.split():
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print(freq)


#shallow copy:
# student = {
#     "name":"nani",
#     "rollno":22
# }
# b=student.copy()
# print(b)

# student["rollno"] = 10
# print(student)
# print(b)

# c = student
# print(c)
# student["rollno"]=11
# print(c)

#why dict is faster
#hashing --> dict stores data in hashtable
#time complexity:O(1)
#searching -->O(1)
#insert,deleting --->O(1)

# data = {
#     "a":1,
#     "a":2
# }
# print(data)

'''
crest a dict with employee
details
now add branch and phone num at a time
fetch all the key and values using loop
make sure to copy before deleting any pair 
pop the last added pair 
print the pair without deleting

addon: make employee a nested dict with multiple employees
each employee has task with arr=[1,2,3]
now print key values using looping

'''

# employee = {"name":"bala reddy",
#             "id": 2234567
# }
# employee.update({"phoneno": 9391565186,"addres": "koduru"})
# print(employee)
# for key in employee:
#     print(key)
# for value in employee.values():
#     print(value)
# for key,value in employee.items():
#     print(key,value)




# students = [
#     {"name":"nani","branch":"cse"},
#     {"name":"bala","branch":"it"}
# ]
# for student in students:
#     print(student)
#     for key, value in student.items():
#         print(key, value)   


'''
group anagram
input:["eat","tea","tan","ate","nat","bat"]
output:[[eat,tea,ate],[tan,nat],[bat]]
'''
# anagrams = {}
# for word in ["eat","tea","tan","ate","nat","bat"]:
#     key = "".join(sorted(word))
#     if key in anagrams:
#         anagrams[key].append(word)
#     else:
#         anagrams[key] = [word]
# print(list(anagrams.values()))

'''
Problem
top k frequent elements
input[1,1,1,2,2,3]
k =2
output[1,2]
'''
# a = [1,1,1,2,2,3]
# k = 2
# freq = {}
# for num in a:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# top_k = [item[0] for item in sorted_freq[:k]]   
# print(top_k)

# a = [1, 1, 1, 2, 2, 3]
# k = 2

# freq = {}

# for i in a:
#     freq[i] = freq.get(i, 0) + 1

# for _ in range(k):
#     maximum = max(freq, key=freq.get)
#     print(maximum, end=" ")
#     del freq[maximum]

a = [1, 1, 1, 2, 2, 3]
k = 2
freq = {}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
#sortnby the frequency descending      
result =sorted(freq,key=freq.get,reverse=True)
print(result[:k])      
