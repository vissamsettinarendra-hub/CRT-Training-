#decision making ability
#control flow decides
#1.how many times to execute what to execute

#human analogy:
'''
if it rains --> take umbrella
if marks > 40 --> pass
if password correct --> login

'''

#program  also needs decision making ability
#control flow: determines
#which atatements to execute and in what order
'''

3- types of control flow
1. sequential:top to bottom execution
2. conditional: decision making
3.looping: repetition

'''
#if --> to check condition
#& executes if condition is true
#syntax:
#if condition:
 #   statements
 
 # #example:
age = 21 
if age > 20:
    print("eligible")
'''
execution flow
      condition true?

      execution the block
'''

x = 10

if x>5:
    print("Hello")

#if-else :what if state becomes flase

#if condition:
#   statement
#else:
#    statements

#example:  even/odd

#take input
num = int(input("enter the number"))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")    

'''
execution flow 
                     condition ?
                     /        \
                     true    flase
                       |       |
                       even   odd 
'''

#elif ladder
#multiple conditions: mutiple decisions

#if condition:
#   statement-1
#elif condition-2:
#   statements
#else:
#   statement

#task: build a student grading system
marks = int(input("enter the marks"))
if marks >= 90:
    print("grade A")
elif marks >= 80:  
    print("grade B") 
elif marks >= 70:
    print("grade C")
elif marks >=60:
    print("grade D")
else:
    print("grade F")
    '''
    '''             


