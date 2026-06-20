# '''
# sum of the elements
# given a list of integers, find sum
# '''
# a =[10,20,30]
# total = 0

# for i in a:
#     total += i
# print(total)
# #O(n)=time complexity
# '''
# find the maximum element in a list
# b = [10,50,90,40]
# find max?
# '''
# b = [10,50,90,40]
# max = b[0]


# for i in b:
#     if i > max:
#         max = i
# print(max)    
# '''
# count the even numbers in list
# '''
f = [1,2,3,5,6,7,8,9,10]
count = 0

for i in f:
    if i % 2 == 0:
        count +=1
        print(count)        



r = [1,2,3,4]

print(r[::-1])

'''
remove the duplicates
'''

o = [5,6,1,7,7,8]

result = []
for i in o:
    if i not in result:
        result.append(i)
print(result)        

'''
find the second largest number
'''

a = [10,40,80,90,30]
max = a[0]
second_max = a[0]           

for i in a:
    if i > max:
        second_max = max
        max = i
    elif i > second_max and i != max:
        second_max = i

print(second_max)

print(max)    

'''
check if list is sorted without using built condition
'''
c = [10,20,30,40]
is_sorted = True            
for i in range(len(c)-1):
    if c[i] > c[i+1]:
        is_sorted = False
        break           
print(is_sorted)        


        