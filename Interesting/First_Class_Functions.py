# A First Class Function is a function that supports all operations available to other entities, like being passed in
# an argument, being returned from a function and being assigned to a variable. If a function accepts other functions
# as arguments or returns functions as their result, that's what you call a higher order function.


# creating a function
def square(x):
    return x * x


# assign the result of a function to a variable
r = square(5)
print(r)

# assign a function to a variable
f = square
print(f)
print(f(4))


## An example of higher order function and first class.
# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result
#
# squares = my_map(square, [1, 2, 3, 4, 5])
# print(squares)
#
# def cube(x):
#     return x**3
#
# cubes = my_map(cube,[1, 2, 3, 4, 5])
# print('squares', squares, 'cubes', cubes, sep='-',  end='\n\n')

## end of higher order function and first class.


## return a function from another function
def logger(msg):
    def log_message():
        print('Log', msg)

    return log_message


log_hi = logger('hi')

print(log_hi)  # this will show that log_hi returns a function.


# Another example of returning a function from another function

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')

## end of function being returned from another function
