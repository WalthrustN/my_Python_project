import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


##  def __str__(self): 'User is {}'.format(self.name) ##why doesnt this work


user = User('Nate', 28)  # because JSON doesnt understand this, we have to use a function to encode it to something JSON
# understands.

## second method
from json import JSONEncoder


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):  # checks is the object is an instance of the User Class.
            return {'name:': o.name, 'age': o.age, o.__class__.__name__: True}  # Creating python logic the JSON mod can
        return JSONEncoder.default(self, o)


# userJSON = json.dumps(user, cls=UserEncoder)
# print(type(userJSON))
# print(userJSON)

# Third Method
userJSON = UserEncoder().encode(
    user)  # for this we encoded the python class object(User) becuase JSON doesnt understand this format,
#
print(type(userJSON))
print(userJSON)

user = json.loads(userJSON)
print(user)
print(type(user))  # This will come out as a dict or dictionary class. But what if we wanted to convert it back to an


# object of the class User (how it originally was).

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    else:
        return dct


user = json.loads(userJSON, object_hook=decode_user)
print(user)
print(type(user))
