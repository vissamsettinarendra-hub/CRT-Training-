
# name=input("enter the name")    
# reverse=""
# for char in name:
#     reverse=char+reverse
# print(reverse)
# if(reverse==name):
#     print("given number is a palindrome")
# else:
#     print("not a palindrome")





#vowel
'''
count the vowles in a string
s = "narendra"
vowels = a,e,i,o,u
'''
# text = input("enter the name:")
# v = ("a,e,i,o,u")
# count=0
# for i in text:
#     if i in v:
#         count+=1
# print(count)

text = input("enter some text")

target = input("enter the target")
count = 0

for ch in text:
   if ch == target:
      count = count+1

print(count)     
