import sys


# list object has to store the list memory so uses more memory
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


print(firstn(10))


# GENERATOR OBJECT uses less memoery
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
    pass


print(list(firstn_generator(10)))
print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(100)))
print(sys.getsizeof(firstn_generator(100)))  # less size
