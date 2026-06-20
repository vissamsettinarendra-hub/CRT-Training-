'''
analogy:
you are give with 2 programs where it is generating
the output

how will you decide which one to use?
1.faster program
2.less memory
3.efficient


# algorithic complexity == effficiency

two types:
1.time complexity: faster results in google

2.space complexity:

mark  zukerberg --->css 20kb
       /       \
     a = 19kb   b = 18kb
        10lpa      30lpa
           
       dua===>  200cr
        70 lakhs --20lakhs --50lakhs
                           
time complexity?
time complexity measures how the running
time grows as the size of input

3 - techniques to measure  how the running the grows as

'''
#stop watch method:
import time
start = time.time()

for i in range(1,1001):
    print(i)
print(time.time()-start)    
'''
#problems in above techniques

1.different systems diff time
2.different compliers/diff interpreters
3.background apps effects time
4.internet/cpu/gpu/affect the performance
'''

#technique 2 counting the num of operations

# not measure the time in seconds but counts operations

def c_to_f(c):
    return c * 9 / 5 + 32

#mul = 1
#div = 1
#add = 1

#example2
def mysum(x):
    total = 0 #-->1op
    for i in range(x+1):
        total = total+i #2op
    return total
#x-->input
# 1+2x  x = 10 -->21 op
# 
# #technique 3  oder of growth
'''
notations:
asymptotic notations

1.big Oh o():calc the upper bound (worst time complexity)
2.omega notation : bestbcase complexity
3.theta: avg case complexity

'''














'''


for i in range
'''

#n^2+10000n+3^1000
#O(n^2)