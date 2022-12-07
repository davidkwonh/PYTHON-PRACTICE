# #   classes practice using animals
import math
class Dog: # classes usually start with capital letters

    _legs = 4   #   _ signifies variables that are static and don't require change
                #   static variables because they are unchanging in each instance, constants and fundamental business logic
    def __init__(self, name): # initialization, whenever class Dog is called, this initialization function is calle
        #   instance attributes declared because they are the attributes of every instance of the class
        self.name = name

    def getLegs(self):
        return self._legs

    def speak(self): # declaring self in the parameter gives access to all other functions and variables in class
        print(self.name + " says: Bark!")




myDog = Dog('Rover')
myDog._legs=3
print(myDog.name)
print(myDog.getLegs())
print(Dog._legs)













# mydog = Dog("muffy") #function and variables are lowercase, class names are capitalized
# wholetthedogsout = Dog("boots")
#
# # if you have a class instance, and use.function, the instance is passed on as the first variable of the function
#
# mydog.speak()
#
# wholetthedogsout.speak()


#   Object Oriented Programming (OOP)
#   the class instances are objects
#   the variables are the attributes
#   the functions are methods or class methods



#   Simple program that utilizes OOP to create a BMI Calculator with user inputs

class Whoami:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def bmi(self):
        return (self.weight/(self.height**2))


name = (str(input("Enter thy name: ")))
age = (int(input("Enter thy age: ")))
weight = (float(input("Enter thy mass in kg: ")))
height = (float(input("Enter thy tallness in cm: ")))

rando = Whoami(name,age,weight,height)
rando.name = name
rando.age = age
rando.weight = weight
rando.height = height
print(name + " You're BMI is: " + str(rando.bmi()))     #   str() necessary because bmi() is of type float

#   static and instance attributes

class Orientation:
    pi = 3.14

    def __init__(self, x_pos, y_pos, degrees):
        self.x_pos = x_pos
        self.y_pos = y_pos
        #   Requires the declaration of Orientation class instead of self because static function rather than an instance function
        self.x_dir, self.y_dir = Orientation.getUnitVectorFromDegrees(degrees)

#   STATIC FUNCTION HENCE NO self. is necessary

    def getUnitVectorFromDegrees(degrees):
        radians = (degrees / 180) * Orientation.pi
        return math.sin(radians), -math.cos(radians)

    def getNextPos(self):
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir


myOrientation = Orientation(5, 5, 75)
myOrientation.getNextPos()


class Orientation:
    pi = 3.14

    def __init__(self, x_pos, y_pos, degrees):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir, self.y_dir = self.getUnitVectorFromDegrees(degrees)

    # One can use the static decorator to declare to python that this is a static var rendering the self.getUnitVectorFromDegrees as a static function

    @staticmethod
    def getUnitVectorFromDegrees(degrees):
        #   using static variable pi of Orientation class
        radians = (degrees / 180) * Orientation.pi
        return math.sin(radians), -math.cos(radians)

    def getNextPos(self):
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir


myOrientation = Orientation(5, 5, 75)
myOrientation.getNextPos()