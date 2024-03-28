#searching
#sorting


#!problem1
#?input
user_input = [1,2,3,4,5,6,7,8,9,11]
 #check to see if a certain number exist in the user input array
n = 1

#linear search
result = False #a variable to keep track of your answer

for e in user_input:
    if e == n:
        result = True
if result == True:
    print('found')
else:
    print('not found')
