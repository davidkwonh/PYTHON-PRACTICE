#Boolean Practice

bool(1)
#   anything other than 0 in bool() will be true
print(bool(0))

print(bool(-1))

print(bool(1j))

print(bool(0j))

print(bool('True'))

#   Prints True because it is a string
print(bool('False'))

#   Only empty strings return false
print('')

bool([])
bool({})
#   returns false

bool(None)
#   returns false

myList = [1,2]
if bool(myList):
    print("myList have values")

a = 5
b = 5
if a - b:
    print('a and b are not equal')

a == b

#   boolean logic
