#   Dictionary Comprehensions

animalList = [('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog)')]
animals = {item[0]: item[1] for item in animalList}
#          Key    : Value
print(animals)

#   cleaner code of ^
animals = {key: value for key, value in animalList}
#   unpack variables matches elements in data structure

#   animal dictionary > list
animals.items()
#   dictionary items
list(animals.items())

#   change structure of each item in list
print([{'letter':key, 'name':value} for key,value in animals.items()])

