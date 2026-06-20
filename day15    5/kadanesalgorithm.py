'''
kandane's algorithm:max sub arrays problems
a= [2,-1,3,-2,4]
find the contigious sud array with max sum
subarry: [-1,3,-2] right
         [2,3] invalid

subarrays     sum
[2]           2
[2,-1]        1
[2,-1,3]      4
[2,-1,3,-2]   2
[2,-1,3,-2,4] 6

i=1
[-1]        1
[-1,3]      2
[-1,3,-2]   0

'''
'''
kadane's algorithm main idea

at every element we decide:

two choices:
1.continue previous sub array
         (or)
2.start a new subarray

current_sum = -5
next_element = 10

-5+10 = 5  #discarding the pervious (-ve)
next == 10
arr = [2,-1,3,-2,4]

current_sum = 2
max_sum = 2

index:1
    -1
    choice1:extend the array
    2+(-1)=1

    choice2:stat anew array
    -1
 current_sum=4
 max_sum = max(2,4)=4   
index3:-2
choice1: extend the arry
     2+(-1)=1+3=4+(-2)=2
     choice2:start a new array
     -2
current_sum = max(4,2)=4
max_sum = max(4,4)=4

index4:4
choice:extend the array
  2+(-1)=1+3=4-2=2+4=6
  choice2:start a new array
  4
current_sum = 6
max_sum=max(4,6)=6


formulas
current_sum=max(arr[i],current_sum+arr[i])
max_sum = max(max_sum,current_sum)

'''

# arr=[2,-1,3,-2,4]
# current_sum = arr[0]
# max_sum = arr[0]

# for i in range(1,len(arr)):
#     current_sum=max(arr[i],current_sum+arr[i])
#     max_sum = max(max_sum,current_sum)

# print(max_sum)


'''
problem: maximmum winning streak
a cricket player gains or loses points in each match

positive ---> won points
negative ---> lost points

the coach wants to find the continuous winning streak with maximum performance

but instead of returning the sum ,return the:
maximum score
starting index
ending index

example:

input:
scores = [-2,4,-1,5,-3,2]

output:

maximum score =8
start index = 1
end index = 3

subarray:
[4,-1,5]

'''
# scores = [-2, 4, -1, 5, -3, 2]

# current_sum = scores[0]
# max_sum = scores[0]

# start = 0
# end = 0
# temp_start = 0

# for i in range(1, len(scores)):

#     # Start a new subarray or extend the current one
#     if scores[i] > current_sum + scores[i]:
#         current_sum = scores[i]
#         temp_start = i
#     else:
#         current_sum += scores[i]

#     # Update maximum
#     if current_sum > max_sum:
#         max_sum = current_sum
#         start = temp_start
#         end = i

# print("Maximum Score =", max_sum)
# print("Start Index =", start)
# print("End Index =", end)
# print("Subarray =", scores[start:end+1])

# a = [-2, 4, -1, 5, -3, 2]
# current_sum=a[0]
# max_sum=a[0]
# start=0
# end=0
# temp_start=0
# for i in range(1,len(a)):
#     #either starting a new sub array or extending
#     if a[i] > current_sum+a[i]:
#         current_sum = current_sum+a[i]

#         #new possible starting index 
#         temp_start=i

#     else:
#         current_sum = current_sum+a[i]

#     #update the maximum
#     if current_sum > max_sum:
#         max_sum=current_sum
#         #save the index values
#         start = temp_start
#         end= i
# print(max_sum)
# print(start)
# print(end)
# print(a[start:end+1])              


'''
problem -5
maximum product subarray
input:[2,3,-2,4]
output:6  2*3
print(index)
'''
arr = [2, 3, -2, 4]

max_prod = arr[0]
min_prod = arr[0]
result = arr[0]

start = end = temp_start = 0

for i in range(1, len(arr)):

    if arr[i] < 0:
        max_prod, min_prod = min_prod, max_prod

    if arr[i] > max_prod * arr[i]:
        max_prod = arr[i]
        temp_start = i
    else:
        max_prod = max_prod * arr[i]

    min_prod = min(arr[i], min_prod * arr[i])

    if max_prod > result:
        result = max_prod
        start = temp_start
        end = i

print("Maximum Product =", result)
print("Start Index =", start)
print("End Index =", end)
print("Subarray =", arr[start:end+1])