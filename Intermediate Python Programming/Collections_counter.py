# Collection: Counter, namedtuple, OrderedDict, defaultdict, deque
from timeit import default_timer as timer
from collections import Counter
from collections import namedtuple


# Counter = counts the number of times a character comes up in a string

a = "aabbaaaabbcccddnnnnfffff"
aCounter = Counter(a)
print(aCounter)
print(aCounter.values())

start = timer()
print("Most common from counter")
print(aCounter.most_common(5))
print(aCounter.most_common(5)[0])
print(aCounter.most_common(5)[0][0])
stop = timer()
print(stop - start)

print("Elements as list")
print(list(aCounter.elements()))

print("Named Tuple")
Point = namedtuple('Point', "x, y, zim, d")
pt = Point(1, -4, 5, 78)
pt2 = Point(3, 8, 3, "57")
print(pt)
print(pt2)

str(pt.x)
print(type(pt.x))
print(type(pt2.d))
