#   functions in python
import math
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


def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2


performOperation(2, 3, 'sum')

#   add parameters but dont always want to define operator
def performOperation(num1, num2, operation='sum', message='HMM?'):
    print(message)
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2


performOperation(2, 3)  #auto defaults to sum
performOperation(2,3,'multiply')

#   keyword arguments must come after positional arguements but can be in any order after
performOperation(2,3,message='HOW IS THIS POSSIBLE?',operation='multiply')


#   anticipating a lot of passed in variables
def preformOperation(*args):
    print(args)

performOperation(1,2,3)

#   pointer to a reference of what is passed
#   only works for positional arguements not keyword

def preformOperation(*args,**kwargs):
    print(args,kwargs)
preformOperation(1,2,3, operation = 'sums')
#printed as a dictionary

#rewrite preformOperation for ultimate flex
def performOperation(*args, operation='sum'):
    if operation == 'sum':
        return math.fsum(args)
    if operation == 'multiply':
        return math.prod(args)
preformOperation(1,2,3,4, operation ='sum')

#   HOW TO GET ALL LOCAL VARIABLES WITHOUT POINTERS
def performOperation(num1, num2, operation='sum'):
    print(locals())




print(globals())
#   prints all global variables

message = 'Some global data'


def function1(varA, varB):
    print(message)
    print(locals())


def function2(varC, varB):
    print(message)
    print(locals())


function1(1, 2)
function2(3, 4)

#   manipulating global and local variables
message = 'Some global data'
varA = 2


def function1(varA, varB):
    message = 'Some local data'
    print(varA)
    print(message)
    print(locals())


def function2(varC, varB):
    print(varA)
    print(message)
    print(locals())


function1(1, 2)
function2(3, 4)

#   functions within a function

def function1(varA, varB):
    message = 'Some local data'
    print(varA)

    def inner_function(varA, varB):
        print(f'inner_function local scope: {locals()}')

    inner_function(123, 456)


function1(1, 2)

#   using locals() to see what are the contents of a function
def function1(varA, varB):
    message = 'Some local data'
    print(varA)

    def inner_function(varA, varB):
        print(f'inner_function local scope: {locals()}')

    print(locals())
    inner_function(123, 456)


function1(1, 2)

#   Variables as functions

x=5

#   function as a var, same thing as treating a function as an object

def x():
    return 5
