#   functions in python
print("Hello World")

#   defininig a fucntion
def x3(number):
    return 3*number #returning a value
print(x3(32))

def multiply(num1, num2):
    return num1*num2
print(multiply("fudge",3))

randomlist = [1,2,3,]

def appendFour(list):
    list.append(4)
    # it does not have to return a value

appendFour(randomlist)
appendFour(randomlist)
print(randomlist)

print(print("woohoo")) # returns no value but returns None, has its own type