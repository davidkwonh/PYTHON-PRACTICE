# for loops

myList = [1,2,3,4,5]
for item in myList:
    print(item)

#   practicing pass and continue

animalLookup = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
    'c': ['cat'],
    'd': ['dog'],
}

for letter, animals in animalLookup.items():
    pass

for letter, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print(f'Only one animal: {animals[0]}')

#   Break if you find what you need while traversing

for letter, animals in animalLookup.items():
    if len(animals) > 1:
        print(f'Found {len(animals)}: {animals}')
        break

#   finding prime numbers between 2 and 100
for number in range(2, 100):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f'{number} is prime!')

#   Adding a boolean and its messy code for extra check

for number in range(2, 100):
    found_factors = False
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            found_factors = True
            break
    if not found_factors:
        print(f'{number} is prime!')