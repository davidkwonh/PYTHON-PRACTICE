# #   classes practice using animals
#
# class Dog: # classes usually start with capital letters
#     def __init__(self, name): # initialization, whenever class Dog is called, this initialization function is calle
#         self.name = name
#         self.legs = 4
#
#     def speak(self): # declaring self in the parameter gives access to all other functions and variables in class
#         print(self.name + " says: Bark!")
#
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