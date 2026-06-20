'''
tuple: collection of ordered elements
#immutable:
# tuple:more faster then list
# allow duplicates

feature     list  tuple
duplicates   yes   yes
ordered      yes    yes
performance  slow   fast
syntax        []    ()

#indexing:
t = (1,2,3,4)
     0 1 2 3 

t[0]     
'''
t = (1,2,3,3.12)
print(t)

print(t[0])


#check the mutability

#t[0] = 9

#tuple pack and unpack

#packing

t = (10,20,30)

#unpacking

a,b,c = t
print(a)
print(b)
print(c)

#tuple  methods

t.count(10)
print(t)
t.index(20)
print(t)
'''
why use tuple?--> fixed data
list: dynamic data

can tuple consist of a list?

what is the difference between append and extend

append: indvidual elements
extend: multiple elements

# difference btw list and tuple

# sort vs sorted


'''
n = ([1,2,3],10,3.14)

n[0].append(20)
print(n)

s = [1,2,3]

s.append([4,5,6])
print(s)

d = [(10,20),(30,40)]
print(d)


