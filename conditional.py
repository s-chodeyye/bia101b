#a calculator application made using
# variable and if statements
#steps
#1.get input from user
#2. do calculation based on user input
#3. give output to the user


print('above user input------------')
userInput = ''

print('* for multipication')
print('+ for addition')
print('- for subtraction')
print('/ for division')


whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input -type', type(whatUserTyped))


if whatUserTyped == "+":
    print('Doing Addition')
    print('doing more addition')

if whatUserTyped == "-":
    print('Doing Subtraction')
    print('doing more subtraction')

