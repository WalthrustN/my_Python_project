# Errors and Exceptions
print("Type Error\n")
# a = 5 + '10'

print("Module Not Found Error\n")
# import superduper

print('Name Error\n')  # variable is not defined yet
# a = 7
# b = c

print('File Not Found\n')
# open('afile.txt')

print('Value Error\n')
d = [1, 2, 3, 4]
# d.remove(5)
print('Index Error\n')
# d[4]

print('Key Error\n')
mydict = {'name': 'Nathaniel'}
# print(mydict['age'])

print('Raising Exceptions\n')
x = -5
# if x < 0:
# raise Exception('x should be positive')
print('Assertion Error\n')
# assert (x>=0), 'x is not positive'

print('Try & Exception\n')
# try:
#    5 / 0
# except:
#    print('an error happened\n')

print('Try & Exception 2\n')
# try:
#    5 / 0
# except Exception as e:
#   print(e + '\n')

print('multiple exceptions\n')
try:
    a = 5 / 1
    b = c + '10'
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up ...')
