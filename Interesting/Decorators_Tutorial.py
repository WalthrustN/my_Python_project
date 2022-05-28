# There a two different types of decorators, function decorators and class decorators. A decorator is a function that
# takes another function as an argument and extends the behavior of this function without modifying it.
# A Decorator is like a += operation because it adds to existing functionality.

# @mydecorator
# def dosomething():
#     pass

def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')

    return wrapper()


@start_end_decorator
def print_name():
    print('Nathaniel')


# print_name = start_end_decorator(print_name) #instead of this use the @start_end_decorator

print_name
