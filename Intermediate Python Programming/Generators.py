# Have you ever had to loop over a large pile of data, A list so large it would crash your work station.
#Or searching for an element in an infinte list of possilibities. Theres a better way to handle these situations
#Generators

#Generators are functions that act as iterators. It generates the elements in a loop. Its an on demand iterable.

def f():
    return 1
    return 2
    return 3

def g():
    yield 1
    yield 2
    yield 3

print(g())
print(list(g()))

for x in g():
    print(x)









