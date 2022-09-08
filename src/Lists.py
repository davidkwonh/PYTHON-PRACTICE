#   List Practice
myList = [1,2,3,4,5]
print(myList[3:])   #   Slicing syntax is great
print(myList[0:6:2])#   third value is step size
print(myList[::2])  #   Same thing

for i in range(100):
    print(i)

myList = list(range(100))
print(myList[::-5]) #   Slicing reverse
myList.append(32)
myList.insert(3, "WHO KNEW U COULD PUT THIS IN")
myList.remove("WHO KNEW U COULD PUT THIS IN")
myList.pop()    #   removes last item on list
while len(myList):   #   While items in list
    print(myList.pop())

a = [1,2,3,4,5]
b = a
a.append(6)
print(b)
#   affects both variables

b = a.copy
a.append(6)
print(b)
print(a)