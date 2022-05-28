class Employee:
    raise_amount = 1.03

    # This is a Class Variable. You can access through the class or the instance. ex.(Employee.raise_amount or
    # emp.raise amount. When you are using this attribute though the instance the program first checks to see

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # 4, 5 method
        return '{} {}'.format(self.first, self.last)

    # methods automatically take in the instance we call self.

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp1 = Employee('Corey', 'Schafer', 60000)
emp2 = Employee('Nathaniel', 'Walthrust', 70000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
