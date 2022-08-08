# property decorators

# getter = property
# setter = [attribute name].setter
# deleter = [attribute name].deleter

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # @property
    # def email(self):
    #     return self.first + '.' + self.last + '@company.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Allows you to use the method but is coded like an attribute. self.fullname. instead of self.fullname().

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Gives additional functionality to the attribute. Allows you to dynamically change attributes linked to fullname by
    # just changing self.fullname.

    @fullname.deleter
    def fullname(self):
        print('-----> Deleted Name!')
        self.fullname = None
        self.first = None
        self.last = None


# Gives additional functionality to the del keyword function

# With this property decorator (setter) we can set the attributes, first and last from the full name method. It will
# first and last.

emp1 = Employee('Corey', 'Schafer')
emp1.fullname = 'Se Long'

# from changing the first, the email doesnt change because the email attribute is only for when the email is being first
# initialized. So how can we automatically get the email to update and print using the new first? The property decorator
# allows us to define a method but access it like an attribute. So by placing @property above the method you can access
# it as an attribute. For the email attribute, it doesnt change with a change of first, so I removed it from the init
# attributes and created a seperate method for it. Last I added @property on top of this new method to make it accesible
# as if it was a attribute. emp1.email instead of emp1.email().

print(emp1.first)
# print(emp1.email)
print(emp1.fullname)

del emp1.fullname
print(emp1.fullname)
