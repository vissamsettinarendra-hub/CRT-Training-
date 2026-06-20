#bitwise &
#1 only if both bits are 1
'''
A  B  A&B
0  0  0  
0  1  0
1  1  1 
1  0  0
'''
# 8 4 2 1

#5 --> 0 1 0 1
#3 --> 0 0 1 1
#& --> 0 0 0 1 ---> 1

print(5&3)
print(6&2)

'''
real life
permission systems,masking operations
checking flags
'''
#bitwise OR
# 1 if any one bit is 1

'''
A B A|B
0 0 0
0 1 1
1 1 1
1 0 1
'''

#example:
''' 
5 --> 0 1 0 1
3 --> 0 0 1 1
| --> 0 1 1 1 
'''
print(5|3) 
print(12|4) 

#bitwise XOR --> IMP interviews
#same bits --> 0
#differnt bits --> 1

#1 if both bits are different
'''
A B A^B
0 0 0
0 1 1
1 1 0
1 0 
'''
'''
6 --> 0 1 1 0
2 --> 0 0 1 0
^ --> 0 1 0 0
'''

print(6^2)  #4

#swap the numbers without using a 3rd variable
#input = 5, 3
#output = 3, 5
a = 5
b = 3

a = a+b
#a = 5+3 = 8
b = a-b#b =8-3 = 5
a = a-b
#a = 8-5 = 3

#perform bitwise operations using XOR operator
a = 5   
b = 3   
a = a^b  
b = a^b      
a = a^b 
print(a,b)

'''
a = a^b
#a = 5^3 --> 6
b = a^b
#b = 6^3-->  5
a = a^b
a = 6^5 -->3
'''
print(a,b)

#bitwise Not

# 0 -->1
# 1 -->0

print(~5)

# ~n = -(n+1)
print(~10) #-11

#low level memory operation

#<< left shift operator

#rule--> shift the bits to left
'''
5 --> 0 1 0 1
<< --> 1 0 1 0 -->10
'''

print(5<<1) #10

#formula ==> n<<k = n*2^k

#right shift : shift the bits to right

print(8>>1)
'''
8--> 1 0 0 0
     0 1 0 0-->4
'''

#forumula = n>>k = n/2^k
print(16>>2)
print(12>>6)

print(13>>7)
print(17>>8)

print