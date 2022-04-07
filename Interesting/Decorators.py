# Property
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # 1 self.email = first + '.' + last + '@email.com'

    @property
    ### by using @property decorator we are defining the function as a method but accessing it like an attribute
    # meaning we don't have to use this () ate the end of the method call.
    def email(self):  ##2
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):  ##2
        return '{} {}'.format(self.first, self.last)

    @fullname.setter  # 4
    def fullname(self, name):  # 4
        first, last = name.split(' ')  # 4
        self.first = first  # 4 with this code we reset our first name
        self.last = last  # 4 with this code we reset our last name

    @fullname.deleter  # 5
    def fullname(self):  # 5
        print('Delete Name!')  # 5
        self.first = None  # 5 with this code we delete our first name
        self.last = None  # 5 with this code we delete our last name


emp1 = Employee("Nathaniel", "Walthrust")

emp1.fullname = 'Shomari Reynolds'  # 4

print(emp1.fullname)

print(emp1.first, end=" ")
print(emp1.last)

print(
    emp1.email)  # 1 we have a problem when we change the first name or last. The email remains the same. This is because the email is an
# attribute when in the __init__ clause.

# 2 print(emp1.fullname()) ##because fullname is a method, () has to presented.
# 2 print(emp1.email()) ##because email is a method, () has to presented.


del emp1.fullname
