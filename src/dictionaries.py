from collections import defaultdict


animals = {'a': "aardvark", 'b': "bear , 'c' : cat"}
print(animals['a'])
animals['d'] = "DOGS"
print(animals['d'])
print(animals)

animals['a'] = "antelope"

print(animals.keys())
print(animals.values())

#   animals['e'] #returns error because no e value

#   print(animals.get('e'))     #   Prints a None obj
len(animals)

# Dictionaries can hold multiple values
animal_lists = {'a': ["aardvark", "abra","alpaca"], 'b': ["bear"], 'c': "cat"}
print(animal_lists)

animals['b'].append("bison")

if 'c' not in animal_lists:
    animal_lists['c'] = []

animals['c'].append('cat')


#   Default Dictionary
animals = defaultdict(list)

#   Did not have to declare a new list because of ^
animals['e']. append('elephant')
animals['f']