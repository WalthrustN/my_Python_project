import random

# used to generate pseudo random numbers. Pseudo Random because the numbers seem random but are reproducible.

a = random.random()  # produces a random float from 0 to 1.
# a = random.uniform(2, 30)  # produces a random float from 2 to 30.
# a = random.randint(30, 37)  # produces a random integer from 30 to 37.
# a = random.randrange(30, 37)  # produces a random integer from 30 to 36.
b = random.normalvariate(2, 1)  # might be useful working in statics, uses mu and sigma to pick a number from a
# normal distribution

print(a)
print(b, end='\n\n')

mylist = list('ABCDEFGH')
print(mylist, end='\n\n')

c = random.choice(mylist)  # This will pick a random element from the list.
# c = random.sample(mylist, 3) #picks 3 unique elements from the list.
# c = random.choices(mylist, k=3) #picks 3 elements from the list(Elements can be reused).
random.shuffle(mylist)

print(c)
print(mylist)
