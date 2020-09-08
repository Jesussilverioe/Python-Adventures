# Pratice creating functions
# Functions make a program easier to write, read, and fix code.
# importing other functions can be helpful in order to use methods from other people's code
import sys as sy
#useful modules from standard library
import datetime     #date and time module
import math         #mathematics operations module
import calendar     #calendar module e.g isleap() function
import os           #operating system module
import random       #random module to perform operations randomly

#import antigravity  #import to open a web browser on a funny page (joke in a python community)

# Function to print a string
def somefunc():
    print ("This is a Function!!!!")

somefunc()
friends = ['edwin', 'ammar', 'jesus']
def ReturnFunc():
    return "This is return by a function."

def keyValFunc(arg1, arg2):
    print(f' This is argument one: {arg1}\n This is argument two: {arg2}.')


val = random.choice(friends)
#stringVal = ReturnFunc()

#using the random fuction to select a random item from the list friends
print(random.choice(friends))
#print (stringVal)

value = 'ammar is a Professional Developer'
print (value.title())

# In python we can also call the function with a keyword which specifies the values for the arguments
# NOTE: the arguments have to match the names of the parameters in the function definition

keyValFunc(arg1 = "Hello", arg2 = "World!")
