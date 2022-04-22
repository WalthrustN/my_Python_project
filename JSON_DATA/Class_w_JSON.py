import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Nate', 28)  # because JSON doesnt understand this, we have to use a function to encode it to something JSON


# understands.


def encode_user(o):  # because it is not JSON Serializable. Have to create custom encoding function.
    if isinstance(o, User):  # checks is the object is an instance of the User Class.
        return {'name:': o.name, 'age': o.age, o.__class__.__name__: True}  # Creating python logic the JSON mod can
        # convert into JSON
    else:
        raise TypeError('Object of the type User is not JSON serializable.')


userJSON = json.dumps(user, default=encode_user)  # default:If specified, default should be a function that gets called
# for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a
# TypeError. If not specified, TypeError is raised.

print(userJSON)

## second method
from json import JSONEncoder


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):  # checks is the object is an instance of the User Class.
            return {'name:': o.name, 'age': o.age, o.__class__.__name__: True}  # Creating python logic the JSON mod can
        return JSONEncoder.default(self, o)


userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

# Third Method
userJSON = UserEncoder().encode(user)
print(userJSON)

user = json.loads(userJSON)
print(user)
print(type(user))
