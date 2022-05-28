def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)
decorated_display()


# the variable decorated_display which passes in our display function through our decorator_function() 's closure.
# In the example the decorator_function returns the wrapper function without the closure.

# by adding a @decorator_function in the line above defining the function display(), it equates to
# display = decorator function(display). Same thing

@decorator_function
def display_info(name, age):
    print('display info ran with arguments ({1}, {0})'.format(name, age))


display_info('Nathaniel', 28)

# We run into problems when we try to decorate the display_info(name, age) function due to the fact it has arguments.
# Now that the function has arguments we have we have to add the syntax *args, **kwargs which stand for arguments and
# keyword arguments. These syntax needs to be passed through the original_function() and the wrapper() function.
