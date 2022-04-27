# In this project, we make a class object called user from a Class User(notice the capitalized User which is the
# name of the Class). The key part of this project is what we do with this Class Object user. We convert its attributes
# to a dictionary. From the Dictionary, we convert it to a JSON String with help from a JSON module. So the process goes
# Python Class Object ---> Python Dictionary ---> JSON String
# The reason for this is because the module can not convert a class object to a JSON String.
# When we use json.dumps we are converting Python Dictionary ---> JSON String.
# When we use json.loads we are converting JSON String ---> Python Dictionary.

# ? Im having difficulty with json loads. As I can not change my JSON Str back to Python Class Object.

import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


##  def __str__(self): 'User is {}'.format(self.name) ##why doesnt this work


user = User('Nate', 28)  # because JSON doesnt understand this, we have to use a function to encode it to something JSON


# understands.

# first method changing Python class object to a python dictionary so it can be JSON serializable.
def encode_user(o):  # because it is not JSON Serializable. Have to create custom encoding function.
    if isinstance(o, User):  # checks is the object is an instance of the User Class.
        return {'name:': o.name, 'age': o.age, o.__class__.__name__: True}  # Creating python logic (dictionary) the
        # JSON mod can convert into JSON
    else:
        raise TypeError('Object of the type User is not JSON serializable.')


# userJSON = json.dumps(user, default=encode_user)  # default:If specified, default should be a function that gets called
# for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a
# TypeError. If not specified, TypeError is raised.

## second method
from json import JSONEncoder


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):  # checks is the object is an instance of the User Class.
            return {'name:': o.name, 'age': o.age, o.__class__.__name__: True}  # Creating python logic the JSON mod can
        return JSONEncoder.default(self, o)


# userJSON = json.dumps(user, cls=UserEncoder)

# Third Method
userJSON = UserEncoder().encode(user)
print(type(userJSON))
print(userJSON)

user = json.loads(userJSON)
print(user)
print(type(user))  # This will come out as a dict or dictionary class. But what if we wanted to convert it back to an


# object of the class User (how it originally was).

def Decode_User(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=Decode_User)

# Reference ---> Intermediate Python Programming Course (Youtube) 2:59:03 ??Help
