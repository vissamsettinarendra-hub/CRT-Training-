'''Problem 1: Employee Productivity Analyzer
Topics Covered: Strings, Dictionaries, Lists, Functions, Sorting, OOPs
Problem Statement
A company tracks employee activities using the format:
Employee Name: TaskCompleted
The activities are stored in a list.
You need to generate a productivity report.
Rules
1. Count the number of tasks completed by each employee.
2. Employee names are case-insensitive.
3. Print employees in descending order of tasks completed.
4. If two employees have the same task count, print them in alphabetical order.
Input
7
John:Login
Alice:Testing
john:Development
Alice:Documentation
Bob:Testing
John:CodeReview
alice:BugFix
Output
john 3
alice 3
bob 1
Constraints
1 ≤ N ≤ 10^4
Skills Tested
 String Parsing
 Dictionaries / Hashing
 Frequency Counting
 Sorting with Custom Logic
 Functions
 '''
# #with using functions:
# def productivity_report(n, activities):
#     task_count = {}

#     for activity in activities:
#         name, task = activity.split(":")
#         name = name.lower()   # case-insensitive

#         if name in task_count:
#             task_count[name] += 1
#         else:
#             task_count[name] = 1

#     result = sorted(task_count.items(), key=lambda x: (-x[1], x[0]))

#     for name, count in result:
#         print(name, count)


# n = int(input())
# activities = []

# for _ in range(n):
#     activities.append(input())

# productivity_report(n, activities)



#without functions
# n = int(input())

# d = {}

# for i in range(n):
#     s = input()
#     name = s.split(":")[0].lower()

#     if name not in d:
#         d[name] = 1
#     else:
#         d[name] += 1

# lst = []

# for name in d:
#     lst.append((d[name], name))

# lst.sort(reverse=True)

# for count, name in lst:
#     print(name, count)


#2problem
'''
Problem 2: Smart Sales Window
Problem Statement
A retail company records daily sales.
Given an array representing sales for N days and a target value K, find the length of the longest
continuous period whose total sales equal K.
If no such period exists, print -1.
Input
8
3 1 2 4 2 1 1 3
8
Output
4
Explanation
Subarray:
1 2 4 1
has sum 8 and length 4.
Constraints
1 ≤ N ≤ 10^5
-10^4 ≤ arr[i] ≤ 10^4'''


# n = int(input())

# arr = list(map(int, input().split()))

# k = int(input())

# d = {0: -1}
# s = 0
# max_len = -1

# for i in range(n):
#     s += arr[i]

#     if (s - k) in d:
#         length = i - d[s - k]
#         if length > max_len:
#             max_len = length

#     if s not in d:
#         d[s] = i

# print(max_len)


# #using two pointers
# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())

# left = 0
# curr_sum = 0
# max_len = -1

# for right in range(n):
#     curr_sum += arr[right]

#     while curr_sum > k and left <= right:
#         curr_sum -= arr[left]
#         left += 1

#     if curr_sum == k:
#         length = right - left + 1
#         if length > max_len:
#             max_len = length

# print(max_len)



#3problem:
'''
Problem 3: A company generates employee IDs as numbers. An ID is considered special if it is
divisible by both 3 and 5.
Given a range of numbers from 1 to N, find how many special IDs are present.
Input Format
A single integer N.
Output Format
Print the count of special numbers between 1 and N (inclusive).'''
n = int(input())

count = 0

for i in range(1, n + 1):
    if i % 15 == 0:
        count += 1

print(count)