'''
what is set?
collection of unordered unique elements
-->unordered
-->unique(never allows duplications)
why?
-->fast searching-->O(1)
-->duplicates removal

how to create a set?

'''
#creation of set
# numbers = {1,2,3,4,5}
# print(numbers)

# numbers={1,2,2,2,3,3,4,4,5}
# print(numbers)

# num = {1,2,2,2,3,3,4,4,5}
# unique=set(num)
# print(unique) 

# #checking the mutability
# # numbers[0]=10
# # print(numbers)
# #set unordered-->fixed indexing(no)
# numbers.add(10)
# #1st way 
# num = {1,2,3,4,5,}
# #2way
# s = set([1,2,3,4,5])
# #freq = {}
# #empty set
# s = set()
# s.add(1)
# print(s)

# #multiple elemente:
# s.update([2,3,4,5,6])
# print(s)

#removing the element
# s.remove(2)
# print(s)

#discard
# print(s.discard(10))
# print(s)

#pop():deletes the random element
#s.pop() 

#clear




# print(20 is s)# it gives boolen values
'''
what is hashing?
hashing will convert data into the unique hash value

python uses:
1.hash tables
2.hash functions
target =10
set = {1,2,3,4,10}
unlike linear search 
hash(10)
it directly jump to target

search,insert, delete-->O(1)


set operations:
1.union            |
2.intersection     &
3.difference        -
# '''
# a = {1,2,3,4}
# b = {5,6,7,8}

# print(a|b)#union
# print(a.union(b))

#intersection:&
# a = {1,2,3,4,5}
# b = {1,6,2,5,8}
# print(a & b)
# print(a.intersection(b))

#difference: 
# print(a-b)
# print(a.difference(b)) 

#symmetric difference:elements not common
# a = {1,2,3}
# b = {2,3,4}
# print(a^b)
# print(a.symmetric_difference(b))



# subset and superset
# a={1,2}
# b={1,2,3,4}
# print(a.issubset(b))
# print(b.issuperset(a))

# #frozenset:
# fs = frozenset([1,2,3,4,5])
# print(fs)

'''
feature    list   tuple  dictionary         set
ordered    yes     yes     no               no
muatbility  yes   no      yes               yes
duplicat    yes   yes    key:no value:yes   no
indexing    yes   yes     no                no

can i store list inside the set?
1.list
2.dict
3.set
 '''
'''
creat a list with squares of a numbers
convert the list with squares of a number
try to repeat the square two times
add the multiples of 2 to the same
set at a single time
--->seperate the set with 2 diff sets
multuples of 2
squares
now perform all the set operations on both'''
# Create a list of numbers
# nums = [1, 2, 3, 4, 5]

# # Squares of numbers
# squares = [x * x for x in nums]

# # Repeat squares two times
# squares = squares * 2

# # Multiples of 2
# multiples_of_2 = [x for x in range(2, 21, 2)]

# # Convert to sets
# square_set = set(squares)
# multiple_set = set(multiples_of_2)

# print("Square Set:", square_set)
# print("Multiples of 2 Set:", multiple_set)

# # Set Operations
# print("\nUnion:")
# print(square_set | multiple_set)

# print("\nIntersection:")
# print(square_set & multiple_set)

# print("\nDifference (Squares - Multiples):")
# print(square_set - multiple_set)

# print("\nDifference (Multiples - Squares):")
# print(multiple_set - square_set)

# print("\nSymmetric Difference:")
# print(square_set ^ multiple_set)


'''
problem
find the length ofmlongest consecutive sequence
input:[100,4,200,1,3,2]
output:[4]   '''
a = [100, 4, 200, 1, 3, 2]

s = set(a)
longest = 0

for num in s:
    if num - 1 not in s:  
        count = 1
        current = num

        while current + 1 in s:
            current += 1
            count += 1

        longest = max(longest, count)

print(longest)