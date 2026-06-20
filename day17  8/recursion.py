'''
recursion is a programming technique where a function calls itself to solve smaller version 
of the same problem
function ->calls itself -->again -->again
some components like:
1.base condition:
condition where the recursion stops

2.recursive case:
function calls itselfs with a smaller input
'''
# def hello(n):
#     if n==0:#base case
#         return
#     print("Hello")
#     #recursive call
#     hello(n-1)
# hello(5) 
'''
call stack:LAST(last in first out)
stores function calls in memory

every function call:
gets added to stack
removed after the completion

def fun1():
    print("func1")
    func2()
def func2():
    print("func2")
func1()  

main
 func1
 func2

'''
# def count(n):
#     if n==0:
#         return
#     print("before:",n)
#     count(n-1)
#     print("after:",n)
# count(5)
#added in stack and removed from stack if work is done    
'''
      |count0|
      |count1|
      |count2|
      |count3|
      |count4|
      |count5|
before:5#top down
before:4
before:3
before:2 
before:1
after:1#bottom up
after:2
after:3
after:4
after:5
'''
'''
5! = 5x4x3x2x1
    (n-1)!*(n-2)-------n

    fact(n)=fact(n-1)*n

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
call stack
|     |
|     |
|fact(1)|pop   1
|fact(2)|pop   1*2
|fact(3)|pop   1*2*3
|fact(4)|pop   1*2*3*4
|fact(5)|pop   1*2*3*4*5=120


factorial(5)=factorial(4)*n
factorial(4)=factorial(3)
factorial(3)=factorial(2)
factorial(2)=factorial(1)
'''
#task sum of n numbers
# def sum(n):
#     if n == 0:      # base case
#         return 0
#     return n + sum(n - 1)
# print(sum(5))
#sum(5)=5+sum(4)
#sum(4)=4+sum(3)


#fibonacci:
#5 = 5+4+3+2+1
#fib(n)=fib(n-1)+fib(n-2)
#fib(5)=fib(4)+fib(3)
#fib(4)=fib(3)+fib(2)
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     return fib(n-1) + fib(n-2)

# print(fib(6))

#task:reverse the string
# def reverse_string(s):
#     if s == "":      # base case
#         return ""

#     return reverse_string(s[1:]) + s[0]

# print(reverse_string("hello"))

'''#task 
given with n = 1234
perform the sum of all the digits
1234=1+2+3+4=10
'''
# def digit_sum(n):
#     if n == 0:      # base case
#         return 0

#     return n % 10 + digit_sum(n // 10)

# n = 1234
# print(digit_sum(n))

'''
task:
check palindrome string using recursion
input:"madam"
output:true
'''
# def palindrome(s):
#     if len(s) <= 1:      # base case
#         return True

#     if s[0] != s[-1]:
#         return False

#     return palindrome(s[1:-1])

# s = input()
# print(palindrome(s))

'''
#task:
print the numbers from N to 1
N = 5
5 4 3 2 1  
'''
# def print_numbers(n):
#     if n == 0:      # base case
#         return 1

#     print(n, end=" ")
#     print_numbers(n - 1)

# n = int(input())
# print_numbers(n)


'''
task
find the largest element in an array using recursion
input:[3,9,2,15,7]
output:15
arr = [3,9,2,15,7]
call n arr[n-1]  what it does                 returns
     5 arr[4]=7  max(7,find_max(arr,4))        wait
     5 arr[3]=15  max(15,find_max(arr,3))        wait
     5 arr[2]=2  max(2,find_max(arr,2))        wait
     5 arr[1]=9  max(9,find_max(arr,9))        wait
     5 arr[0]=3  max(3,find_max(arr,3))        wait
unwinding:
5.returns  5
4.max(9,3)  = 9
3.max(2,9) = 9
2.max(15,9) = 15
1.max(7,15) = 15

final output:15
'''
# def max_element(arr, n):
#     if n == 1:          # base case
#         return arr[0]

#     return max(arr[n-1], max_element(arr, n-1))

# arr = [3, 9, 2, 15, 7]
# print(max_element(arr, len(arr)))

'''
task check array is stored or not using recursion
input:[1,2,3,4,5]
output:True
'''
def search(arr, n, key):
    if n == 0:          # base case
        return False

    if arr[n - 1] == key:
        return True

    return search(arr, n - 1, key)

arr = [1, 2, 3, 4, 5]
key = 3

print(search(arr, len(arr), key))