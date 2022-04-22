# Python objects are translated to JSON according to a conversion table.
# PYTHON                              JSON(JAVA SCRIPT OBJECT NOTATION)
# dict                                object
# list, tuple                         array
# str                                string
# int, long, float                   number
# TRUE                               true
# False                              false
# None                               null

# Importing Json module
import json

# person in this case is a python object(dictionary)
person = {'name': 'Nathaniel', 'age': 28, 'city': 'New York', 'hasChildren': False,
          'titles': ['engineer', 'programmer']}

# Converting a Python Object(person) to a Json Object(personJson) and sorting the keys alhpabetically.
# personJson = json.dumps(person, indent=4, separators=('; ', '= '), sort_keys=True)
personJson = json.dumps(person, indent=4, sort_keys=True)  ##I took separators out because with it converting
# personJson doesnt work.
print(personJson)

# creating a writable file, converting and dumping the contents of person(python object) to (JSON object) on the file.
# with open('person.json', 'w') as file:
#    json.dump(person, file, indent=4)

## Decoding Deserialization - converting json back to a python object.
# person = json.loads(personJson)
# print(person)

# using json.load to convert a JSON file to python though a variable called person. person holds the python equivalent.
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
