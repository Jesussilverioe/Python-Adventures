#Dictionaries allow us to work with {key,value} pairs. Similar to hashmaps in C++

student = {  
    'Name' : 'jhon',
    'Age'  :  44,
    'Degree': 'Computer Science'

} 

print(student['Name'])
print(student.get('Name')) #accessing an element in a dictionary using the get() method

#loop to print all the {key, value} pairs
for key, value in student.items():
    print(key, value)