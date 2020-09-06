# Strings are a data type heavily used in python
# They have a wide varity of methods that simplfy the way of working with them

first_name = 'Jesus'
last_name = "smith"     #Notice we can use either '' or "" to define a string

# We can print an f-string which are a nice way to print string variables
print(f'{first_name},{last_name}')

# f-string can be enclosed in '' or "" as well
# Using methods in a f-string

# The title method Capitalizes the first letter of each word in the string
print(f'{first_name},{last_name.title()}')