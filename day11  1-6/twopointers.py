'''
two pointers:


one pointer is start
one pointer is end


operations:
swapping
moves toward the center


arr=[1,2,3,5,7,10,11,15]
        L R
     L>R

example:
sum of any two digits should be equal to equal to target
target =15
arr = [1,2,3,5,7,10,11,15]
       i,j
outer range(n)
inner range(i+1,n)
n = 5
a = [1,2,3,5,7,10,11,15]
target=15
num=len(a)
for i in range(n):
    for j in range(i+1,n):
     num = a[i]+a[j]
    if num == target:
        print("paid found:",a[i],a[j])
    else:
       print("not found")

arr = [1,2,3,5,7,10,11,15]
       L               R
       = 1+15=16
       R--
       14<target
       L++

       1+11=12<target
       2+11=13<target
       3+11=14<target
       5+11=16>target
       5+10=15==target
       a[L],[R]


 current_sum =arr[L]+arr[R]

     target =15      
'''
# a = [1,2,3,5,7,10,11,15]
# target=15
# left =0
# right= len(a)- 1
# while left < right:
#     current_sum = a[left]+a[right]

#     if current_sum==target:
#        print("pair is found:",a[left],a[right])
#        break
#     elif current_sum<target:
#        left+=1
#     else:
#        right -=1
# else:
#     print("no pair found")            

# a = list(map(int, input().split()))
# a.sort()  # Ensure the list is sorted
# target = 15
# left = 0
# right = len(a) - 1

# while left < right:
#     current_sum = a[left] + a[right]
#     if current_sum == target:
#         print("pair is found:", a[left], a[right])
#         break
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1
# else:
#     print("no pair found")



'''
reverse a list
two pointers approach
'''

# a = list(map(int, input().split()))
# left = 0
# right = len(a)-1
# while left<right:
#        a[left],a[right]= a[right],a[left]
#        left +=1
#        right -=1
# print(*a)    


'''
check an array is palindrome using two pointers
'''
# a = list(map(int, input().split()))
# left = 0
# right = len(a)-1
# palindrome=True
# while left<right:
#       if a[left]!=a[right]:
#           palindrome=False
#           break
          
#           left+=1
#           right-=1
# if palindrome:
#      print("palindrome") 
# else:
#      print("not palindrome")          
    
    
'''
move zeroes to the end of the list
i= 1,0,4,-2,0
0= 1,4,-2,0,0
'''
# a = list(map(int, input().split()))
# left = 0
# right = len(a)-1
# while left<right:
#     if a[left] == 0 and a[right] != 0:
#         a[left],a[right]=a[right],a[left]
#         left +=1
#         right -=1
#     elif a[left] != 0:
#         left +=1
#     else:
#         right -=1
# print(*a)


# a = list(map(int, input().split()))
# left = 0
# right = len(a)
# for right in range(len(a)):
# #     if a[right]!=0:
# #         a[left],a[right]=a[right],a[left]

# #         left +1
# # print        
    

# '''
# sort the binary array:
# example:
# input:[1,0,0,1,1,0,1]
# output:[0,0,0,1,1,1,1]
# '''  
# a = list(map(int, input().split()))
# left = 0
# right = len(a)-1
# while left<right:
#     if a[left] == 1 and a[right] == 0:
#         a[left],a[right]=a[right],a[left]
#         left +=1
#         right -=1
#     elif a[left] == 0:
#         left +=1
#     else:

#         right -=1
# print(*a)


'''
Problem: Pair Frequency Match

Given an array of N integers and a target value K,

4 find the number of unique pairs (i, j) such that:

5 i<j

6 arr[i] + arr[j] = K

7 A pair is considered unique based on values, not indices.

8 Input Format

9 First line contains integer N.

10 Second line contains N space-separated integers.

11 Third line contains integer K.

12 Output Format

13 Print the count of unique pairs whose sum equals K.

14

'''
# arr = list(map(int, input().split()))
# k = int(input())
# arr.sort()
# left = 0
# right = len(arr)-1
# count = 0
# while left < right:
#     current_sum = arr[left] + arr[right]
#     if current_sum == k:
#         count += 1
#         left += 1
#         right -= 1
#         while left < right and arr[left] == arr[left - 1]:
#             left += 1
#         while left < right and arr[right] == arr[right + 1]:
#             right -= 1
#     elif current_sum < k:
#         left += 1
#     else:
#         right -= 1
# print(count)


# a = list(map(int,input().split()))
# k = int(input())
# a.sort()
# left=0
# right=len(a)-1
# pairs = set()
# while left<right:
#     current_sum=a[left]+a[right]
#     if current_sum==k:
#         pairs.add((a[left],a[right]))

#         left +=1
#         right-=1
#     elif current_sum<k:
#         left+=1
#     else:
#         right -=1        
# print(len(pairs))        