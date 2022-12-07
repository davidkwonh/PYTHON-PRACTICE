class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark!')

    def getLegs(self):
        return self._legs


#   class Chihuahua extends the Dog class

class Chihuahua(Dog):
    #   If the child glass defines attributes or methods that coincides
    #   with parent, the child class overwrites it
    def speak(self):
        print(f'{self.name} says : Yap yap yap!')

    def wagTail(self):
        print('Vigorous wagging!')

#   EXTREMELY USEFUL WHEN U HAVE A CLASS YOU WANT TO USE BUT IT NEEDS A COUPLE OF EXTRA TWEAKS

mylist = list()


class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)


uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList)

#   Extending the Parent Class Practice

class UniqueList(list):

    def __init__(self):
        #   There are problems with declaring a new constructor with the parent constructor
        #   solve it by declaring the parent constructor with super()
        super().__init__()
        self.someProperty = 'Unique List!'

    def append(self, item):
        if item in self:
            return
        super().append(item)


uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)