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

# When setting default values, the default values go at the end of the parameters
def keyValFunc(arg1 = '', arg2 =''):
    print(f' This is argument one: {arg1}\n This is argument two: {arg2}')


val = random.choice(friends)
#stringVal = ReturnFunc()

#using the random fuction to select a random item from the list friends
print(random.choice(friends))
#print (stringVal)

value = 'ammar is a Professional Developer'
print (value.title())

# In python we can also call the function with a keyword which specifies the values for the arguments
# NOTE: the arguments have to match the names of the parameters in the function definition
# If the function has default values the function can be called without argumentrs

keyValFunc()

# Return a value function. Functions can return values that can be collected 
# from where the function was called

# Functions can return any data type
def get_formatted_name(first_name, last_name, middle_name = ''):
        if middle_name:
            full_name = f'{first_name} {middle_name} {last_name}'
        else:
            full_name = f'{first_name} {last_name}'
            
        return full_name.title()

# In this function call the last parameter is optional. if not passed, the parameter would have a default value.
name = get_formatted_name('alice', 'maurice', 'parker')
print(name)

students = {'jhon', 'michael', 'peter'}

def getStudents(stu):
    print('The students are: ')
    for students in stu:
        print(students)

getStudents(students)

# Creating a function that returns a dictionary
def MakePerson(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

person = MakePerson('patricia', 'queen')
print(person)