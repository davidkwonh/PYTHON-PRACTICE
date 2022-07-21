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
my_set = {1,2,4,5,6}
type(my_set)
print(my_set)

#redundancies are taken out
oops = {1,2,3,4,3}
print(len(oops))
#order and redundancies doesn't matter for logic
print({1,2,3,4} == {4,3,2,1,1,2,3,4,3,2,1})

#github practice