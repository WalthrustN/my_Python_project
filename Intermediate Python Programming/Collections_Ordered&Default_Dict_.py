from collections import OrderedDict
from collections import defaultdict

ordict = OrderedDict()

ordict['b'] = 2
ordict['d'] = 4
ordict['g'] = 7
ordict['i'] = 9
ordict['c'] = 3

print(ordict)
# Ordered dictionary gives you the order according to which elements you added first. fifo
# since im using a verison that is more advanced than previous ones, I can just use an ordinary dictionary. It will work
# the same. To make it a dictionary just change ordict = OrderedDict() to ordict = {}


print("Default Dictionary")
DD = defaultdict(float)

DD["default"] = 4
DD["diction"] = "special"
print(DD["anyUnusedVariable"])

print(DD)
# Similar to the the usual dictionary, but the only difference that it has default values for the ones not set yet.
# In a default dict, when you ask for the value of a key that has not been created you get a default value, which
# depending on the data type you specify can be different.

GG = defaultdict(str)

GG["1"] = "HOT"
GG['2'] = "WARM"
GG['4'] = "COLD"

print(GG["20"])

GG = defaultdict(int)

print(GG["reason"])

