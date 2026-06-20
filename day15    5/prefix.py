# prefix sum : one of the most importan techniques used to solve subarray problems

# 1. Fast range sum queries
# 2. Optimisation
# 3. sliding window's alternative
# 4. sub array problems
# 5. compitative programming

# It reduces the repeated calculations and imporoves the time complexity

# What is prefix sum ?
# It stores the cumilative sum of the elements from the beginning of the array to every index

# Eg: [a0,a1,a2,a3,a4,.....]

# then:
# prefix[i] = arr[0]+arr[1]+arr[2]+arr[3]+ .....+arr[i]
'''problem:
 
       arr = [2,4,1,7,3]
              0 1 2 3 4
              
              find the sum from index 1 to 3
              output = 4+1+7= 12
              
              sum =prefix[r]-prefix[l-1]'''
#bruteforce approach              
# a =[2,4,1,7,3]
# l = 1
# r = 3
# total =0
# for i in range (l,r+1):
#     total = total+a[i]
# print(total)
# a = [2,4,1,7,3]
# n = len(a)
# #create a prefix array
# prefix=[0]*n
# #[0,0,0,0,0]
# prefix[0]=a[0]
# #[2,0,0,0,0]
# #build the prefix sum
# for i in range(1,n):
#     prefix[i]=prefix[i-1]+a[i]
# print(prefix)
# l =1
# r=3
# #range sum
# if l ==0:
#     ansewr = prefix[r]
# else:
#     ansewr = prefix[r]-prefix[l-1]
# print(ansewr)
    
     # Array
# a = [1,3,5,2,2]
# n = len(a)
# # Build Prefix Sum Array
# prefix = [0] * n
# prefix[0] = a[0]
# for i in range(1, n):
#     prefix[i] = prefix[i - 1] + a[i]
# # Queries (left, right)
# queries = [(1, 4), (2, 4), (0, 3)]
# for l, r in queries:
#     if l == 0:
#         answer = prefix[r]
#     else:
#         answer = prefix[r] - prefix[l - 1]
#     print(f"Sum from {l} to {r} =", answer)
'''find the equilibrium index using prefix sum
arr =[1,3,5,2,2]

left sum =1+3 =4
right sum =2+2=4
left sum == right sum

print equilibrim index
index =2 '''
# a = [1, 2, 3, 2, 2]

# n = len(a)

# # Build prefix sum
# prefix = [0] * n
# prefix[0] = a[0]

# for i in range(1, n):
#     prefix[i] = prefix[i - 1] + a[i]

# total_sum = prefix[-1]

# for i in range(n):
#     # left sum
#     if i == 0:
#         left_sum = 0
#     else:
#         left_sum = prefix[i - 1]

#     # right sum
#     right_sum = total_sum - prefix[i]

#     if left_sum == right_sum:
#         print("Equilibrium Index =", i)
#         break
# else:
#     print("No Equilibrium Index")



# a = [1,2,3,2,2]
# n = len(a)

# prefix = [0] * n
# prefix[0] = a[0]

# for i in range(1, n):
#     prefix[i] = prefix[i - 1] + a[i]
# total_sum = prefix[-1]
# #find the equilidrium index
# for i in range(n):
#     if i ==0:
#         left_sum=0
#     else:
#         left_sum=prefix[i-1]
#     right_sum = total_sum - prefix[i]
#     if left_sum == right_sum:
#         print("equilidrium index",i)  