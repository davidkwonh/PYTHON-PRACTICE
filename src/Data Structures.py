my_list = [1,2,3,4]# initializing a list
print(my_list) #printing list

#order matters in a list
oops = [4,3,2,1]
print(my_list==oops)

#   String Lists and len() function
stringlist = ["what","am", "I", "doing"]
print(stringlist)
print(len(stringlist))

#   Creating a list of lists using arrays
listoflist = [[1,2,3], [True, False], []]
print(listoflist)
print(len(listoflist))

#sets elements in a list are unique
my_set = {1,2,4,5,6,6,6,2,3,3}
rdmset = {"fudge", 'avc', 1, 2, 3}
type(my_set)
print(my_set)
print(rdmset)

#redundancies are taken out
oops = {1,2,3,4,3}
print(len(oops))
#order and redundancies doesn't matter for logic
print({1,2,3,4} == {4,3,2,1,1,2,3,4,3,2,1})

#   tuples
#   Constraints is that tuples cannot modify
tuple = (1,0)
print(type(tuple))

#   tuple.append(3) DOES NOT WORK
#   WHY TUPLE
#   efficient memory because exactly two pairs and cannot add  more
#   lists have append feature in which memory is set aside for more
#   (x,y) coordinates


#   Dictionaries
#   key in dictionaries have to be unique
dictionary = {
    'a': "a great time",
    'b': "gut feeling",
    'c': 32,
    'a': "fudge"
}
print(dictionary['c'])
print(dictionary)

#   Sets unique values while dictionaries have unique keys
#   order is irrelevant
