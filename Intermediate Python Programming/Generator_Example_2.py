import sys


def fibonacci(limit):
    # 0, 1, 1, 2, 3, 5, 8
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print(list(fibonacci(25)))
print(sys.getsizeof(fibonacci(100)))
fib = fibonacci(100)
for i in fib:
    print(i)
