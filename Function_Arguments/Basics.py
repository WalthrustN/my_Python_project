# The difference between arguments and parameters.
# Positional and Keyword Arguments
# Default Arguments
# Variable Length Arguments (*args, **kwargs)
# Container unpacking into function arguments
# Local vs Global Arguments
# Parameter passing (by value or reference)


# The difference between arguments and parameters.
from training.Strings import my_list


def print_name(name):
    print(name)


print_name('Alexis')


# name is the parameter and 'Alexis' is the argument. Parameters are the variables used when defining a function.
# When we call the function we use the argument(s).


# Positional and Keyword Arguments
def foo(a, b, c):
    print(a, b, c)


foo(1, 2, 3)

# 1, 2, 3 are positional arguments. They take the position of parameters a, b, and c.
foo(a=2, b=3, c=4)


# (a=2, b=3, c=4) are keyword arguments.

# Default Arguments
def foo(a, b, c, d=3):
    print(a, b, c, d)


foo(4, 6, 3)


# This has a default argument of d=3. Default arguments begin with the default parameters written after the normal ones.


# Variable Length Arguments (*args, **kwargs)
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, 6, seven=7, eight=8)


# *args is a tuple where you can pass any number of position arguments.
# **kwargs is a dictionary where you can pass any number of positional arguments.


# Container unpacking into function arguments
def foo(a, b, c):
    print(a, b, c)


# my_list = (0, 1, 2)
my_list = [4, 8, 12]
my_dict = {'a': 0, 'b': 1, 'c': 2}
print(*my_list)
foo(**my_dict)


# the length of the container must match the parameters given. foo has 3 parameters and so does my_list.


# Local vs Global Arguments

def foo():
    global number
    x = number
    number = 3
    print('number inside function', x)


number = 4
foo()
print(number)


# To modify the a variable outside the function, the variable has to be global. If not it will just function locally.
# In this example number = 4, then we perform foo() and x = 4 and number then turns to 3 and we print 'number inside
# function x'. With this end to the function foo(), we finally do our last command line which is print(number) and we
# print 3.


# Parameter passing (by value or reference)
def foo(x):
    x = 5
    print(x)


var = 10
foo(var)
print(var)


# Mutable objects like lists or dictionaries can be changed with a method. But if you rebind the reference in the method
# Then the outer reference will still point to the original object and is not changed.Immutable objects like strings or
# integers cannot be changed within a method. But Immutable objects contained within a mutable object can be reassigned
# within a method.

# 10 is an integer which is an immutable object and cannot be changed so with foo(var) called it doesnt change var into
# 5 globally.

def fool(a_list):
    a_list.append(4)


my_list = [1, 2, 3]
fool(my_list)
print(my_list)


# Mutuable Objects can be modified within a function


def fool(a_list):
    a_list = [100, 200, 300]
    a_list.append(4)
    a_list[0] = -100


my_list = [1, 2, 3]
fool(my_list)
print(my_list)


# when we created a.list we created a local Alist of variables. We rebinded the reference in the method, then the outer
# method does not get changed.

def fool(a_list):
    a_list += [100, 200, 300]
    a_list.append(4)
    a_list[0] = -100


my_list = [1, 2, 3]
fool(my_list)
print(my_list)


## different then this because you can not assign the parameter passing a value globally from inside the function.

def fool(a_list):
    a_list = a_list + [100, 200, 300]
    a_list.append(4)
    a_list[0] = -100


my_list = [1, 2, 3]
fool(my_list)
print(my_list)
