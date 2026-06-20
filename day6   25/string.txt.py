'''
string: one of the most important topic

strings are the sequence of characters:
encolsed --> '',"",''''''
                             mutability
                             /      \
                          mutable   immutable
                            |         |
                           change    can't change
stings are immutable
                          example:
                          name = "rarendra kumar"
                          name[0] = "n"   -->error
memory space
#  S T R I N G
   0 1 2 3 4 5 

   #accessing order
   str[0]
''' 

name = "narendra"
print(name)
print(name[0])

print(name[0:2])
print(len(name))

str = "college"
      #0123
print(len(str))

#slicing:
#str[atart,end,step]

print(str[0:3])
'''
str = "C O L L E G E"
       0 1 2 3 4 5 6 
       -7 -6 -5 -4 -3 -2 -1
str[-1:-4]
str[6:3]

str[-1]  -->last character 

str[-2]  -->second last charecter

str[10]   -->index error

#ommiting start
str[:3] -->col

#string [3:] -->lege

#step slicing:
str[0:6:2]  --->cle
str[0:6:1]  --->colleg

#reverse your name
'''
name = "nani"
print(name[::-1])

'''
#string traversal:
name = "c h a l a p a t h i"
        0 1 2 3 4 5 6 7 8 9 
for i in name:
    print(name[i])

    output:
    c
    h
    a
    l
    a
    p
    a
    t
    h
    i

for i in range(len(name)):   10
    print(name[i])                 i = 0-9



'''
for ch in range(len(name)):
    print(ch,name[ch])

print(name.upper())
print(name.lower()) 
#title()--->first litter capital
#str = "python programming"
print(name.title())

#capitalize()
#only first letter will get capital
print(name.capitalize())

college_name = " chalapathi "
#strip -- removes extra spaces
print(college_name.strip())

#replace:

text = "I Love Programming"
print(text)
print(text.replace("Love","Hate"))
replaced_text = text.replace("Love","Hate")
print(replaced_text)

fruit = "banana"
#find the frequency of a
print(fruit.count("a"))

#startswith -->
print(name.startswith("n"))

#endswith -->
text = "python"
print(text.endswith("on"))

#split()
text = "python C java"
print(text.split())
seperated = text.split()
print(type(seperated))

new = "-".join(seperated)
print(new)

#searching inside the strings

#find()  -->
print(new.find("python"))

#using membership operaqtor
print("python" in new)

#index()
text = "python"
print(text.index("p"))

#which is safe find() or index?

#string formatting
name = "vijay"
age = 20

#f - strings
print(f"My name is {name} and age is {age}")

#old college
print("Name:",name, " and age is:",age)

#format()
print("Welcome {}".format(name))

#escaping characters or sequence

print("hello \n world")
print("hello \t world")

#R- stings(regex regular expressions)
path = r"c://downloads/photos/pic.jpeg"
'''
r -->tells to your interpreter that there are no escaping characters in path
'''

#swapcase() ---?
text = "bala  bavadeep reddy"
print(text.swapcase())

#casefold() --->stonger lower conversion
print(text.casefold())

#center --->
print(text.center(50))


#task:create a string with your friends name 
#split the names to in a list
#join the string "_"
#traverse over the string and find index
#of the person name starting with "a"
#print the person name 
#count the len of the name and check "a" occurance
#print the frnd name with 30 spaces in center
name = "nani bala harish abhi"
print(name.split())
print(type(name))
variable = name.split()
print(type(variable))
name = "_".join(variable)
print(name)
# for i in range(len(name)):
#     print(name[i])
# print(name.index("h"))
for i in variable:
   if i.startswith("a"):
      print(i)
      print(len(i))
      print(i.center(30))
   


#task: reverse your name or a string without using slicing


#slicing:

name = "narendra"
print(name[::-1])

#dont use slicing
'''
                        logic
                          |
        read the characters from the end of the string
                          |
       start adding each char (from end) to a
                         |
                      print the var                                        
        '''
name = "narendra"
reverse = ""
for i in range(len(name)-1,-1,-1):
   reverse = reverse + name[i]
print(reverse)


#problem - 2  palindrome

original = input("enter the string")
reversed = original[::-1]
if original == reversed:
   print("palindrome")
else:
   print("not palindrome")   

'''
find the frequency of the character

s = "banana

target = "a"

frequency = 3

  '''
text = input("enter some text")

target = input("enter the target")
count = 0

for ch in text:
   if ch == target:
      count = count+1

print(count)       