# Inheriting allows us to create a subclass with a the attributes and methods of the parent.

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    num_of_emps = 0
    raise_amount = 1.25

    def fullname(self):  # 4, 5 method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Creating a Developer class
class Developer(Employee):
    raise_amount = 1.5

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)  # 1
        # Employee.__init__(first, last, pay) #2
        self.prog_language = prog_language


# for our developer class we want to pass in another argument for our init method. But our Employee class where the
# init method is inherited only has first, last and pay as arguments. You can use #1 or #2 to pass through the init
# arguments from the parent class

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # 1
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


# we passed employees= None, instead of [] initially because you never want to pass mutuable data types like a list
# or dictionary. Also for some reason we cant say if employees=None: #?


# We created a subclass by using (XXXXX) after creating a class.

dev1 = Employee('Nathaniel', 'Walthrust', 80000)
dev2 = Developer('Aziah', 'Walthrust', 100000, 'Python')
mgr1 = Manager('Naitini', 'Walthrust', 120000, employees=None)

print(dev2.email)
print(dev1.email)

mgr1.print_emps()
mgr1.add_emp(dev1)
mgr1.print_emps()

print(isinstance(mgr1, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))

# print(help(Developer)) #to show inheritances

# print(dev2.pay)
# dev2.apply_raise()
# print(dev2.pay)
# print(dev2.prog_language)

# using a apply raise function from the parent Employee class with the raise_amount attribute from the Developer class.
