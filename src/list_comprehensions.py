myList = [1,2,3,4,5]
myList = [2*item for item in myList]
print(myList)

#   List comprehension is a for loops in one line
#   List comprehension with filters

myList = list(range(100))
filterList = [item for item in myList if (item%10 == 0)]
print(filterList)

#   string functions
myString = "My name is david. I live in CA"
myString.split('.')
myString.split()
def cleanWOrd(word):
    return word.replace('.', '').lower() #  chaining functions, lowercase and replace . with ''
[cleanWOrd(word) for word in myString.split()]
print([cleanWOrd(word) for word in myString.split() if len(cleanWOrd(word)) < 3])

#   nested list comprehension
print([[cleanWOrd(word) for word in sentence.split()] for sentence in myString.split('.')])
