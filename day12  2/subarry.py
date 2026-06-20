'''
s ="college
[c]
[co]
[coll]
[colle]

a = [1,4,5,6,8,9]
[1]
#sub array:it should have a countinuity
[1,4]--->wrong

[4,5,6]--> yes

subsequence:
#elements are skipped
#any selected items

concept   sub array    subsequence
continuity  yes          no
skipping allowed  no     
order    yes            no
derivedfrom   continuos     derived from original array  

example:
a =[1,2,4,5,6,7,9,11]
subarry:[1,2,3]
subarry:[4,5,6,7]
sudsequence:[1,2,4,5]
'''


'''
problem
a=[2,1,5,1,3,2]
k =3

1.2 1 5 -->8
2.1 5 1-->7
3.5 1 3 -->9
4.1 3 2--->6
'''
# a = [2,1,5,1,3,2]
# k = 3
# max_sum=0

# for i in range(len(a)-k):
#     #6-3+1-->4#0 1 2 3
#     current_sum = 0
#     #inner -->adding the elements
#     b =[]
#     for j in range(i,i+k):#0 1 2
#                             #j=2
#         current_sum += a[j]
#         max_sum = max(max_sum,current_sum)
#         b.append(a[j])
#     print(b)
# print(max_sum)   

''' 

a = [2,1,5,1,3,2]
previous_sum+(-outgoing)+incoming element

'''
# a = [2,1,5,1,3,2]
# k=3
# window_sum = sum(a[:k])
# max_sum = window_sum
# for i in range(k,len(a)):
#     outgoing = a[i-k]
#     incoming = a[i]

#     window_sum = window_sum-outgoing+incoming
#     max_sum=max(max_sum,window_sum)
# print(max_sum)


'''
subarray
find the first continuos subarry whose sum equal to the target
'''
# a = [1,4,20,3,3,10,5]
# target = 33
# found = False
# for i in range (len(a)):
#     current_sum=0                                  not got
#     for j in range(i,len(a)):
#         current_sum=current_sum+a[j]
#         #check for target
#         if current_sum==target:
#             print(a[i:j+1])
#             found=True
#             break 
# if found:
#    break

#sliding window approach for above problem
    
            



    
    
         










