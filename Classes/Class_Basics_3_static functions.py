class Employee:
    num_of_emps = 0
    raise_amount = 1.25

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    def fullname(self):  # 4, 5 method
        return '{} {}'.format(self.first, self.last)

    # methods automatically take in the instance, we call self.

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod  # To turn a regular instance method into a class method, all you need is the classmethod decorator.
    def set_raise_amount(cls, amount):  # gotta use cls for the class variable because class and cls are different.
        cls.raise_amount = amount

        # now instead of using Empolyee.raise_amount, we can use Empolyee.set_raise_amount(1.25)


emp1 = Employee('Corey', 'Schafer', 60000)
emp2 = Employee('Nathaniel', 'Walthrust', 70000)


# Example of static method, Using this method which does not require cls or self to create the constuctor,
# to find out if the day was a weekend or week day. weekday = True, weekend =  False
@staticmethod
def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    return True


import datetime

my_date = datetime.date(2022, 6, 12)

print(is_workday(my_date))

# differ from class and instance methods because the class or self(instance) has to be there.
# static functions behave just like regular functions.


print(Employee.num_of_emps)

# reference = https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
