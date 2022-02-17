# Writing a function that makes functions using a lambda expression,

def build_quadratic_function(a, b, c):
    "Returns the function a^2x + bx + c as a lambda function"
    "x is the argument, in this lambda syntax."
    return lambda x: a*x**2+b*x+c

f = build_quadratic_function(2, 3, -5)

print(f(2))

#Another way to use a lambda function
print(build_quadratic_function(3, 4, 2)(1))

