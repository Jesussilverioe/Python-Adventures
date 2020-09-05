num = [1,2,3,4]

# Regular loop without range
# Range is define as FROM - TO interval. The loop will iterate withing that interval 

for x in num:
    print(x)
    for y in 'abc':
        print(x, y)

# Using range in a for loop

for i in range (1, 11) :
    print (i)


# While loop. In a while loop you define the condition to stop the loop.
# One has to be very careful no the enter in a infinate loop
t = 0
while t <= 10:
    print(t)
    t += 1