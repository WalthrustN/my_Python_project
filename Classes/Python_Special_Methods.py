# Special methods
# These methods allow us to emulate some built-in behavior in python. Also how you implement operator overload.

class Employee:
    num_of_emps = 0
    raise_amount = 1.25

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):  # 4, 5 method
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


## now that we have a __str__ method it uses this representation rather than __repr__.

emp1 = Employee('Corey', 'Schafer', 60000)
emp2 = Employee('Nathaniel', 'Walthrust', 70000)

print(1 + 2)
print('a' + 'b')

# the behavior is different when we add two strings together then when we add integers. When we add strings the strings
# become concatenated, But when we add two integers they just add the numbers. Depending on what objects we work with
# the addition has different behavior.

# special methods are almost always surrounded by double underscores so people gsve the nickname dunder.
# Dunder repr and str methods
# str is meant to be a readable representation of an object and meant to be a display for the end user.
# repr is an unambiguous representation of the object and should be used for debugging and logging. Meant to be seen by
# developers. calling __str__ (the string representation) on an employee will just use __repr__ as a fallback.

print(emp1)
print(emp1.__str__())
print(emp2.__repr__())
print(emp1 + emp2)
print(emp2.__len__())
