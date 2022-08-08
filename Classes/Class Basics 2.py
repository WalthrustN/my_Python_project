class Employee:
    num_of_emps = 0
    raise_amount = 1.25

    # This is a Class Variable. You can access through the class or the instance. ex.(Employee.raise_amount or
    # emp.raise amount. When you try to access an attribute on an instance, program first checks if the instance
    # contains that attribute, if not then checks to see if the class or any class it inherits from has the attribute.
    ## __dict__ is a double underscore (dunder) variable that shows all that attribute contained by either an
    ## instance or class.

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):  # 4, 5 method
        return '{} {}'.format(self.first, self.last)

    # methods automatically take in the instance we call self.

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp1 = Employee('Corey', 'Schafer', 60000)
emp2 = Employee('Nathaniel', 'Walthrust', 70000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print(Employee.__dict__)  ##__dict__ variable shows raise_amount is a class variable.
print(emp1.__dict__)

Employee.raise_amount = 1.05
emp1.raise_amount = 1.33
Employee.raise_amount = 1.05  # ? why can't I change emp1.raise back to 1.05 with this line ?

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.num_of_emps)
