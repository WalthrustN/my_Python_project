# Strings: Ordered, Immutable, Text Representation
from timeit import default_timer as timer

my_string = "      how, are, you, doing"
my_list = my_string.split(",")
print(my_list)
my_string = my_string.strip()
print(my_string)

print(my_string.startswith('h'))
print(my_string.endswith("doing"))
print(my_string.find("o"))
print(my_string.count("o"))
print(my_string.replace("how", "What"))
new_string = ''.join(my_list)
new_string.strip()
print(new_string)

my_list = ['a'] * 6
print(my_list)

start = timer()
my_string = ''
for i in my_list:
	my_string += i
print(my_string)
stop = timer()
print(stop - start)

# good
start = timer()
my_string = ''.join(my_list)
print(my_string)
stop = timer()
print(stop - start)

var = 3.12345
vars2 = 2.178
vars3 = 1.4537
my_string2 = "the variable is %.2f" % var
# %.2f is a place holder for a floating variable with 2 decimal places,
# %d for int, %s for str
print(my_string2)

my_strong3 = "The variable is {:.2f} and {:.2f}"
print(my_strong3.format(vars3, vars2))

