#Take an input from the user
s = input("enter the string")

#creat an empty dictionary
#this dict will store character -->frequency(count)

freq = {}

#loop over the string to count the frequency

for char in s:
    #check if the character already exist?
    if char in freq:

        #if present , increase the frq count by 1
        freq[char] +=1

    else:
        #if value appears for the first time
        #add it to the dict with the count 1
        freq[char] = 1

#step-2: find the non repeating character  

#example:

'''     
input = "aabbcddee"   

dict after the loop
{
   'a':2
   'b':2
   'c':1
}

'''
#variable : create a variable to store if non
# repeating character is found or not

found = False

#again loop through the original string
#this keeps the order of the string
for char in s:
    #check if the character freq is 1
    if freq[char] == 1:
        #print the first non repeating character
        print("first non repeating char",char)

        found = True

        break
#step-3 if char were found

if found == False:
    print("no non repeating character were found")    
