#   Practice with Tuples

mySet = {'a','b','c'}
print((mySet))

#   remove duplicates to a list by changing it into a set
myList = [1,2,3,2,3,2,3,5,3]
myList = list(set(myList))
print(myList)
#   Sets can only contain unique values
#   randomized, order doesn't matter
#   subscribtable is when an object that can be obtained through index

mySet.add('d')
#   different from append, add tosses it to the list

'd' in mySet

len(mySet)
mySet.pop()  #   not at the end but obtains a random element

while len(mySet):
    print(mySet.pop())

mySet.discard('d')
#   doesn't return error despite being empty



#   TUPLES REVIEW
myTuple = ('a','b','c')
print(myTuple)

#   orderable and subscriptable but cannot be modified

#   myTuple[2] = 'd'
#   return error
#   more efficient list and exact memory allocation

def returnMultipleValues():
    return (1,2,3)

print(type(returnMultipleValues()))

myTuple = 1,2,3
type(myTuple)
#   returns tuple because defaulted
a,b,c = returnMultipleValues()
print(a)
print(b)
print(c)

