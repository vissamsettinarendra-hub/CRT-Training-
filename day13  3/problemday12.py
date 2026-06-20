'''
a=[1,4,20,3,10,5]
target = 33
found=False
for i in range(len(a)):#0 1 2 3 4 5
    current_sum=0
              #0-6
    for j in range(i,len(a)):#0 1 2 3 4 5
        current_sum = current_sum+a[j]
            #0+4+20+3+10+5=42
            #0+4+20+3+10=37
            #0+20+3+10=33
#check for target
        if current_sum == target:    
            found = True
            break
    if found:
        print(a[i:j+1])
        break
        '''

'''#sliding window approach for above

a=[1,4,20,3,10,5]


window      sum 
[1]=    1           sum<target
[1,4] = 5           sum<target
[1,4,20]=25         sum<target
[1,4,20,3]= 28      sum<target
[1,4,20,3,10]=30    sum>target
[4,20,3,10]=37      sum>target
[20,3,10]=33        sum==target
'''
# a=[1,4,20,3,10,5]
# target=33
# left = 0
# current_sum=0
# for right in range(len(a)):
#     current_sum=current_sum+a[right]
#     while current_sum>target:
#         current_sum=current_sum-a[left]
#         left = left+1
#     if current_sum==target:
#         print(a[left:right+1]) 
#         break   

'''
find the length longest continuos subarray that contains no repeating elements
input :[1,23,1,2,3,4]
output:4
example:sbstring
input:["abcabcbb"]
output:4
in brute fore
'''
# s = "abcabcbb"

# max_len = 0

# for i in range(len(s)):
#     seen = set()

#     for j in range(i, len(s)):
#         if s[j] in seen:
#             break

#         seen.add(s[j])
#         max_len = max(max_len, j - i + 1)

# print(max_len)

# a = [1,2,3,1,2,3,4]

# max_len = 0

# for i in range(len(a)):
#     seen = set()

#     for j in range(i, len(a)):
#         if a[j] in seen:
#             break

#         seen.add(a[j])
#         max_len = max(max_len, j - i + 1)

# print(max_len)


#using sliding window 
# a = [1,2,3,1,2,3,4]

# left = 0
# seen = set()
# max_len = 0

# for right in range(len(a)):
#     while a[right] in seen:
#         seen.remove(a[left])
#         left += 1

#     seen.add(a[right])
#     max_len = max(max_len, right - left + 1)

# print(max_len)



# s = "abcabcbb"

# left = 0
# seen = set()
# max_len = 0

# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left += 1

#     seen.add(s[right])
#     max_len = max(max_len, right - left + 1)

# print(max_len)


 

        
