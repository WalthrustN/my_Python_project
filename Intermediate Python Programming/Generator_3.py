# Prime Number Generator

import itertools

def prime_numbers():
    # Handle the first prime number because other than 2 every prime number is odd
    yield 2
    prime_cache = [2] #Cache of prime numbers

    #Loop over positive, odd integers
    for n in itertools.count(3,2):
        isPrime = True

        #Check if the positive odd integers are divisible by the cache.
        for p in prime_cache:
            if n % p == 0:
                isPrime = False
                break
                

        if isPrime == True:
            prime_cache.append(n)
            yield n

for p in prime_numbers():
    print(p)
    if p > 100:
        break



    #Loop over positive, odd integers





