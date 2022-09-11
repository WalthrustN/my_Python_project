# * Asterisk Operator
# Asterisks can be used for many ways: multiplication and power operations, the creation of list or tuples,for unpacking
# lists or dictionaries into function arguements, for unpacking containers into a list or merging two dictionaries.

result = 5 * 7
print(result)

result = 2 ** 4
print(result)

zeros = [0] * 10
print(zeros)
zeros_ones = (0, 1) * 10
print(zeros_ones)
ab = 'ab' * 10
print(ab)


def foo(a, b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)

# for unpacking examples go to Function Arguments/Basics

# unpacking containers
numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning)

# numbers was seperated into two objects. beginning and last, but because beginning has a star in front of it, it is
# seen as a group of arguments(list).

# another example
numbers = [1, 2, 3, 4, 5, 6]
beginning, *middle, secondlast, last = numbers
print(middle)

# merging lists and tuples
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

# merging dictionaries
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}

my_dict = {**dict_1, **dict_2}
print(my_dict)
