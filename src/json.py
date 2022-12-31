#   Dealing with JSON files and strings
import json
from json import JSONDecodeError, JSONEncoder


jsonString = '{"a": "apple", "b": "bear", "c": "cat",}'

# json.load(jsonString)


#   making sure that our json string is parsed

try:
    json.loads(jsonString)
except JSONDecodeError:
    print('Could not parse JSON!')


#   Dumping python dictionary into JSON

pythonDict = {'a': 'apple', 'b': 'bear', 'c': 'cat',}
json.dumps(pythonDict)


#   Custom JSON Decorders

class Animal:
    def __init__(self, name):
        self.name = name

# pythonDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat'), }
# error because object opf type animal is not JSON Seriable

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        #   o is the object that needs to be decoded into JSON
        if type(o) == Animal:
            return o.name
        #   not animal then pass it to parent to default method
        return super().default(o)


pythonDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat'), }

# it needs to configure specific encoder by "cls"

json.dumps(pythonDict, cls=AnimalEncoder)