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
cunts = ['edwin', 'ammar', 'jesus']
def ReturnFunc():
    return "This is return by a function."

val = random.choice(cunts)
#stringVal = ReturnFunc()
print(random.choice(cunts))
#print (stringVal)

value = 'ammar is a cunt'
print (value.title())