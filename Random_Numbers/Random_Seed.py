import random

# used to generate pseudo random numbers. Pseudo Random because the numbers seem random but are reproducible.
# random.seed is a function that shows how this works.
# These numbers are reproducible and not recommended to use for security, instead use the secret module.

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(3)
print(random.random())
print(random.randint(1, 10))

random.seed(3)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
