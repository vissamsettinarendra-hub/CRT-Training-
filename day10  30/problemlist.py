'''
find the largest odd number

'''

# f = [1,2,4,6,9]
# max = f[0]
# for i in f:
#     if i % 2 != 0:
#         i>max
#         max=i
# print(max)


'''
creat a list of squares
'''
# a =[2,3,4,5,6]
# square_list = []
# for i in a:
#         square_list.append(i*i)
# print(square_list)        

'''
check wheather the given exist in list 
'''                
# b = [10,20,30,40]
# k = eval(input())
# found = False
# for i in b:
#     if i==k:
#         found = True
#         break
# if found:
#     print("element found")    
# else:
#     print("element is not found")    
    

'''
find the common elements in both the list
'''
a = [1,2,3,4,5]
b = [3,4,5,6,7]

# for i in a:
#     if i in b:
#             print(i)


'''
swap the first and last element in a list
'''            
# a = [1, 2, 3, 4, 5]

# a[0], a[-1] = a[-1], a[0]

# print(a)

'''

find the avg of the number in a list
note: take the input frim the user in list
'''
# n = int(input())
# a = list(map(int, input().split()))
# total = 0
# for i in a:
#     total+=i
# average = total/n   
# print(average)


'''
find all the odd numbers in a list
note: take the list as input from user
'''
# n = int(input())
# a = list(map(int, input().split()))
# for i in a:
#     if i%2 != 0:
#         print(i, end = " ")

'''
find the sum of the digits of each element in a list
'''

# a = [10, 20, 30]

# for num in a:
#     digit_sum = 0
#     for digit in str(num):
#         digit_sum += int(digit)
#     print(digit_sum)


#        or

           

# a = [10, 20, 30, 40]

# for i in a:
#     total = 0
#     num = i

#     while num > 0:
#         total += num % 10
#         num //= 10

#     print(total)
         
'''
find the samllest even number in a list
'''
# a = [1,2,3,4,5]

# l = []
# for i in a:
#     if i % 2 == 0:
#         l.append(i)

# print(min(l))


        #or  
# n = int(input())
# a = list(map(int, input().split()))       
# min = 99999

# for i in a:
#     if i%2 == 0:
#         if i < min:
#             min=1
# print(min) 



'''
find the number of elements greater than avg
'''
# n = [1,2,3,4,5,6]
# total = 0
# for i in n:
#     total +=i
# average = total/6 
# while True:
#     if average < i:
#         print(average)
#         break


# n = [1, 2, 3, 4, 5, 6]

# total = 0
# for i in n:
#     total += i

# average = total / len(n)

# count = 0
# for i in n:
#     if i > average:
#         count += 1

# print(count)    

'''
find the differnce between largest and smallest number in a list
'''
# n = [10,20,30,40,50]
# print(max(n)-min(n))


'''
count the numbers ending with 5
'''

# n = [25,33,44,65]

# count = 0

# for i in n:
#     if i % 10 == 5:
#         count += 1

# print(count)

'''
replace the replace the negative with zeros
'''
# n = [1,-2,8,5,-7]

# for i in range(len(n)):
#     if n[i]<0:
#         n[i] = 0
# print(n)        
'''
product of all the elements in list
'''
n = [1,2,3,4,5]
product = 1
for i in n:
    product*= i
print(product)    