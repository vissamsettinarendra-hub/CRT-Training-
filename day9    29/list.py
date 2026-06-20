# '''
# what a is list?
# list: collection of ordered elements
#                     mutability
#                     /     \
#                   mutable    immutable
#                     |          |
#                  can modify    cant mofify
# list is mutable
# allows duplicate--> yes list allows duplicate
# #dynamic in size

# #syntax:
# list_name = [elements]

# #stores heterogenous elements

# '''
# numbers = [10,20,30,40,10.4]
# print(type(numbers))

# data = [10,10.4,"python",True]
# print(data)

# #accessing the elements

# a = [10,20,30,40]

# print(a[0])
# print(a[2])

# #check the mutability

# a[0] = 60

# print(a)

# #negative indexing
# a = [10,20,30,40]
#    # -4 -3 -2 -1
# print(a[-1])
# print(a[-2])

# #slicing:

# #list[start:end:step]

# print(a[0:3])
# print(a[:3])
# print([a[::2]])

# #list methods

# #append:
# b = [10,20]
# b.append(30) #add

# #extend:
# b.extend([40,50,60])
# print(b)

# #insert -->adds the elements at specific 
# b.insert(2,20) 
# print(b)

# #remove -- >removes the element
# b.remove(20)
# print(b)
# #pop --> removes the elements eith index
# b.pop(0)
# print(b)

# #clear --> deletes all elements
# b.clear()
# print(b)

# #index -->returns the position

# print(b.index(20))

# #count  -->count the occurance of the element
# b.count(20)
# print(b.count(20))

# #reverse 
# b.reverse()
# print(b)

# #copy: 
# b = b.copy()
# print(b)

# #sorting i list

# a = [5,0,2,4,3,1]
# #sort()  --->sorts in ascending order
# a.sort()
# print(a)

# #descending order:
# a.sort(reverse=True)
# print(a)

# # #sorted:created a new list
# # #sort:
# # b = sorted(a)
# # print(b)
# '''
# task:create a list with 5 bestfriend
# 1.add a new friend just introduced
# 2.remove the 2 friend just had a fidht
# 3. add 3 close frnds at a single time
# 4.sort the friend in alphabetical order
# 5.dalete the friend at index 5
# 6.copy the friend list in a new list
# 7.then perform clear on previous list
# '''
# new = ["nani","shark","manoj","sai","dk"]
# new.append("reddy","mon")
# print(new)
# new.remove("shark")
# new.remove("dk")
# print(new)
# new.extend(["sai","manoj","dk"])        
# print(new)
# new.sort()
# print(new)
# new.pop(5)
# print(new)
# new1 = new.copy()
# print(new1)
# new.clear()
# print(new)

#nested list?
a = [[1,2,3],[4,5,6]]
   #    0      1
print(a[0][0])
print(a[1][1])


#iteration over the list
a = [10,20,30,40]

for i in a:
    print(i)

#range:
for i in  range(len(a)):
    print(a[i])

#list comparehension:

#[expression for variable in iterable]       

#example:
squares = [x*x for x in range(1,6)]
print(squares)

