# print('Replace with String - positional\n')
import itertools

first_name = 'Alex'
last_name = 'Marshall'
print('My name is {}.'.format(first_name))
print('My name is {} {}.\n\n'.format(first_name, last_name))

print('Replace with String using Index\n')
print('My name is {0} {1}.'.format(first_name, last_name))
print('My name is {1}, {0}. First name {0}\n\n'.format(first_name, last_name))

# print('Alignment: Align Left, Right, Middle\n')
# print("""{:<} align Left (default is align left, so this is optional)
# {:>n} align Right with n padding spaces
# {:^n} align Middle with n padding spaces\n""")

print('align left - these both do the same thing\n')
cases = [5, 16, 294]
for case in cases:
    print('Number of cases: {}'.format(case))
for case in cases:
    print('Number of cases: {:<}'.format(case))
print('\n')

print('align right with 5 total spaces\n')
for case in cases:
    print('Number of cases:{:>5}'.format(case))
print('\n')

print('align center with 10 total spaces\n')
for case in cases:
    print('Number of cases:{:^10}'.format(case))
print('\n')

# print('''Integers & Floats
# {:d} Integer variable
# {:5d} Integer with padding of 5
# {:f} Floating point variable\n''')

length = 26
print('Length is {:d}.'.format(length))

# align right, padding=6, integer
print('Length is {:>6d}.'.format(length))

# named variable, align center, padding=4, integer
print("In dog years, I'm {age:^5d}.\n".format(age=8))

# print('integer with commas')
print('Distance to moon is {:,d} miles.\n'.format(238900))

radius = 4.78
print('Radius is {:f} inches.'.format(radius))

# round to 1 decimal place, float
print('Radius is {:.1f} inches.'.format(radius))

# padding=6 (pads with leading 0's), round to 1 decimal
print('Radius is {:06.1f} inches.'.format(radius))
# [{:06.1f} tells us that all characters will adD up to 6 and will be lead with 0s with 1 rounded decimal place.

# padding=5 decimal places
print('Radius is {:.5f} inches.'.format(radius))

# positive & negative signs
a, b, c = 15, -9, 33
print('A is {:+d}.  B is {:+d}.  C is {:-d}.'.format(a, b, c))

# {+3d} shows pos or neg sign, padding=3.
# {: d} prints neg or a leading space if positive.
print('A is {:+3d}.  B is {:+4d}.  B is {: d}.\n\n'.format(a, b, b))

##print('Named Placeholders\n')
print("{name} is a {job}.".format(name='Mekael', job='Carpenter'))
name = 'Mekael'
job = 'Carpenter'
print("{n} is a {j}.".format(n=name, j=job))

# Or use a dictionary, and ** unpacks the dictionary.
jobs = {'name': 'Mekael', 'job': 'Carpenter'}
print("{name} is a {job}.".format(**jobs))

# passing in a list is clean and easy
scores = [78, 96, 83, 86]
print('Score 2 is {s[1]}\n\n'.format(s=scores))

# Scientific Notation
print('My big number is {:e}'.format(874.577))
print('A bigger number is {:E}\n\n'.format(602214090000000000000000))

# Binary & Hexadecimal
# {:b} converts decimal to binary {:x} converts decimal to hex. Or use upper case X for capitals.
print('The binary equivalent of 79 is {:b}'.format(79))
print('The Hexadecimal equivalent of 183 is {:X}'.format(183))

print(scores, jobs)

# link for reference = https://github.com/joeyajames/Python/blob/master/String%20Formatting.ipynb
help(itertools.cycle)
