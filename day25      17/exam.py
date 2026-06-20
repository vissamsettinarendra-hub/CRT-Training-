'''
*problem statement:
given an integer array arr of size N,
find the count of elements whose value is
grater than all of its prior elements
the 1st element is always considered in the count
example:
input: arr = {7,4,8,2,9}
output:3'''

# n = int(input())
# arr = list(map(int, input().split()))

# count = 1          
# max_element = arr[0]

# for i in range(1,n):
#     if arr[i] > max_element:
#         count += 1
#         max_element = arr[i]

# print(count)

n =  int(input())
a = list(map(int, input().split()))
left = 0
right = n-1
while left<right:
    if a[left] == 0 and a[right] != 0:
        a[left],a[right]=a[right],a[left]
        left +=1
        right -=1
    elif a[left] != 0:
        left +=1
    else:
        right -=1
print(*a)
