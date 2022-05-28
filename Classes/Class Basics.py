# Python Object Oriented Programming

# Classes is not just specific to python. It is used in most programming languages as a way to logically group our data,
# and function in a way that is  easy to reuse and build upon.

# Example
# We have an  app for our company and we want to represent our employees in our python code. This is a great use for a
# class cause each individual employee will have specific attributes and methods. Each employee might have a name, an
# email, a pay and actions the employee can take.

# We will use a class as a blueprint for creating an employee. A Class is a blueprint for creating instances.
# Each unique employee will be an instance of the class Employee. An Instance is an object that belongs to a class.
class Employee:
    def __init__(self, first, last, pay):  ### __init__ method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # 4, 5 method
        return '{} {}'.format(self.first, self.last)


## this is a special method called __init__ in python we can think about it as
## a function that we use to initialize the instance. instead of emp1.first = 'Corey' we can use this function to create
## a template for what attributes a class Employee object can have. In other langauges this might be called a
## constructor.
#    pass    # we can use pass as a placeholder

# emp1 = Employee()
# emp2 = Employee()

emp1 = Employee('Corey', 'Schafer', 60000)
emp2 = Employee('Nathaniel', 'Walthrust', 70000)
### You can  use this instead of making instance variables one by one, because of the __init__ method

# print(emp1)
# print(emp2)

# Emp1 and Emp2 are 2 instances of the class Employee. When you print the instances,
# the result will be the location of the object. They both have different locations in memory.

### emp1.first = 'Corey'
# emp1.last = 'Schafer'
# emp1.email = 'Corey.Schafer@company.com'
# emp1.pay = 60000
#
# emp2.first = 'Nathaniel'
# emp2.last = 'Walthrust'
# emp2.email = 'Nathaniel.Walthrust@company.com'
### emp2.pay = 70000

print(emp1.email)
print(emp2.email)

# We created instance variables (emp1.first, emp1.last, emp1.email and emp1.pay) and the same for emp2.
# But theres an easier way. Go to ##

# 4 to perform some form of actions, we have to add some methods to our class.

print(emp1.fullname())  # we have to put the () after the method name because it is a method not an attribute  #5 If we
# remove the self from where we define the method fullname, it wont work. fullname takes 0 positional arguments but 1
# was given. It can be confusing because it doesnt look like we are passing any arguments into the fullname method. But
# the instance is getting passed automatically. We can also run this method using
print(
    Employee.fullname(emp1))  # 5 This is whats going on in the background. print(emp1.fullname()) gets transformed into
# this.
