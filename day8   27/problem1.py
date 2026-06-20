'''
count the frequency of the characters
example:

input: aaabc
output:
a:3
b:1
c:1

dict = {'a':10,'b':3}
'''
string = input("enter the string")
            #a a b c 
            #0 1 2 3 
            #ch = 1
freq = {}#{a:1}

for ch in string:
    if ch in freq:
        #freq[a] = freq[a]+1
        freq[ch] +=1
    else:
        #freq[c] = 1
        freq[ch] = 1
for key in  freq:
    print(freq[key])

'''
find the maximum freq character?
example:
input: aaabcd
a:3
b:1
c:1
d:1
'''

  

string = input("enter the string")
            
freq = {}

for ch in string:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1
max_freq = 0
max_char = ""        
for key in  freq:
    print(freq[key])
    if freq[key] > max_freq:
        max_freq = freq[key]
        max_char = key

print(max_freq)
print(max_char)



