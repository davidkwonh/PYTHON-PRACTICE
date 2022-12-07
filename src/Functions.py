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

#   Text manipulation using functions

text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#   makes the string lower case
def lowercase(text):
    return text.lower()

#   makes the string without any punctuations
def removePunctuation(text):
    punctuations = ['.', '-', ',', '*']
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

#   makes the string without a single new line
def removeNewlines(text):
    text = text.replace('\n', ' ')
    return text

#   removes words longer than three characters
def removeShortWords(text):
    return ' '.join([word for word in text.split() if len(word) > 3])

#   removes words longer than 6 characters
def removeLongWords(text):
    return ' '.join([word for word in text.split() if len(word) < 6])


#   creating an object processingFunctions that uses the functions as variables
processingFunctions = [lowercase, removePunctuation, removeNewlines, removeLongWords]

for func in processingFunctions:
    text = func(text)

print(text)

#   Lambda functions
#   one line functions and it is an implied return
who = (lambda x: x + 3)(5)
print(who)

myList = [4,6,2,6,8,65,3]
#   Lambda function called sorted()
sorted(myList)

myList = [{'num': 3}, {'num': 2}, {'num': 1}]
sorted(myList, key=lambda x: x['num'])

