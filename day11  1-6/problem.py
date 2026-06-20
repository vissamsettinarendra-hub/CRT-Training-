'''
print the elemente greater than previous element
# '''
# n=int(input())
# a = list(map(int,input().split()))
# b=[]
# i = 0
# for a[i] in range(n):
#     if a[i]>a[i-1]:
#         c =True
#     else:
#         c =False
#     b.append(c)   
# print(b) 


'''
count the multiples of three
'''
# n =int(input())
# a = list(map(int,input().split()))
# s= []
# count = 0

# for i in a:
#     if i % 3 == 0:
#         count += 1
#         s.append(i)
# print(s)        
# print(count)


'''

find the absolute diff b/w first element and last element in the list
'''

# n =int(input())
# a = list(map(int,input().split()))   
# print(abs(abs(a[0]-abs(a[-1]))))

'''
elements which appers only once
'''
# n =int(input())
# a= list(map(int,input().split()))
# count= 0
# for i in a:
#     if a.count(i) == 1:
#         print(i,end=" ")

'''
move all the negative numbers to the left
'''
# a= list(map(int,input().split()))
# a.sort()
# print(a)      

    # or
# a = list(map(int,input().split()))
# negative = []
# positive = []
# for i in a:
#     if i<0:
#         negative.append(i)
#     else:
#         positive.append(i)
# result = negative+positive
# print(*result)   #unpacking of list 


'''
find the frequency of the element
'''
# a = list(map(eval,input().split()))
# freq = {}
# for i in a:
#     if i in freq:
#         freq[i]= freq[i]+1
#     else:
#         freq[i]=1
# for key in freq:
#     print(freq[key])



'''
rotate list by k positions
given and k integer,rotate the 
list to the left by k position
'''   
# a = eval(input())
# arr = list(map(eval, input().split()))
# k = eval(input())

# k = k % a
# arr = arr[-k:] + arr[:-k]

# print(*arr)   
    #or


a = list(map(eval, input().split()))
k = eval(input())

for i in range(k+1):
    first = a.pop(0)
    a.append(first)
print(a)
print(len(a))