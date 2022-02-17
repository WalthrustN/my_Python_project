import itertools

# itertools module includes product, permutations, combinations, accumulate, groupby, and infinite iterators

print("Product from itertools module")
a = [1, 2]
b = [3]

prod = list(itertools.product(a, b, repeat=1))
print(prod)

print("\n")

prod = list(itertools.product(a, b, repeat=2))
print(prod)

print("\n")

prod = list(itertools.product(a, b, repeat=3))
print(prod)

print("\n")

print(('Permutations from itertools module'))

a = [1, 2, 3, 4]
perm = itertools.permutations(a, 2)
print(list(perm))

print("\n")

perm = itertools.permutations(a, 3)
print(list(perm))

print("\n")

print(('Combinations from itertools module'))
comb = itertools.combinations(a, 2)
print(list(comb))

combwr = itertools.combinations_with_replacement(a, 2)
print(list(combwr))
print("\n")

print(('Accumulate from itertools module'))
import operator

acc = itertools.accumulate(a)
print(a)
print(list(acc))

acc2 = itertools.accumulate(a, func=operator.mul)
print(list(acc2))

acc3 = itertools.accumulate(a, func=max)
a.insert(2, 5)
print(list(acc3))
print("\n")

print(('Groupby from itertools module'))


def smaller_then_3(x):
    return x < 3


group_obj = itertools.groupby(a, key=smaller_then_3)
for key, value in group_obj:
    print(key, list(value))

print('\n')
persons = [{'name': 'Nathaniel', 'age': 28}, {'name': 'Ariel', 'age': 28}, {'name': 'Najee-Ana', 'age': 26},
           {'name': 'Ojani', 'age': 23}]

persons_groupby = itertools.groupby(persons, key=lambda x: x['age'])
for key, value in persons_groupby:
    print(key, list(value))

print('\n')
print(('Count, Cycle, and repeat from itertools module'))

for i in itertools.count(10):
    print(i)
    if i == 15:
        break

print('\nCycle')

c = [1, 2, 3, 4, 5, 6]
rotatec = itertools.cycle(c)
print(type(rotatec))
print(list(rotatec))

print('\nRepeat')
for i in itertools.repeat(3, 5):
    print(i)
