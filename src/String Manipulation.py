#   Slicing
import math

intro = "My name is David Kwon"

intro[0]
intro[1]

#get characters up to 7
intro[:7]
intro[0:7]

#get characters from index 11
intro[11:]

myList = [1,2,3,4,5]
myList[2:4]

len(myList)

"My number is: " +str(5)

f'My number is {5}'
f'My number is {5} and twice that is {2*5}'
f'Pi is {math.pi:2f}'

#   multiline python str

myString = '''
long block text
I can add newlines
text doesnt stop until \'\'\'
\n
'''

print(myString)
print(myList)