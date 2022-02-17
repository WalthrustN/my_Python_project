import pprint as pp

# lambda functions(one line functions)
add5 = lambda x: x + 5
print(add5(4))

square = lambda x: x * x
square6 = square(6)
print(square6)

gettens = lambda p: int(p / 10) % 10
print(gettens(794.67))

# sorting through a list of tuples with the key being a lambda function
list1 = [("eggs", 5.66), ('honey', 9.70), ('carots', 1.20), ('peaches', 2.45)]
list1.sort(key=lambda x: x[0])
print(list1)

list2 = list1.copy()
list2.sort(key=lambda x: x[1])
print(list2)

# sorting through a list of dictionaries with the key being a lambda function
list3 = [{"make": "Ford", "model": "focus", "year": 2010}, {"make": "BMW", "model": "530XI", "year": 2007},
         {"make": "Nissan", "Quest": "focus", "year": 2002}]
list3.sort(key=lambda x: x["year"])
pp.pprint(list3)

# using lambda functions to filter a list.
list4 = [1, 2, 3, 4, 5, 6]
list5 = list(filter(lambda x: x % 2 == 0, list4))
print(list5)

odds = lambda x: x % 2 == 1
list6 = list(filter(odds, list4))
print(list6)

# using a function called map to modify every value in a list by the lambda function. Map applies the same function to
# every item in this list.

list7 = list(map(lambda x: x * x * x, list4))
print(list7)

# Lambda Conditionals
starts_with_J = lambda x: True if x.upper().startswith("J") else False
print(starts_with_J("jade"))

wordb4 = lambda s, w: s.split()[s.split().index(w) - 1] if w in s else None
sentence = "The cat ate the big rat."
print(wordb4(sentence, "ate"))

# using datetime with lambda functions
import datetime

now = datetime.datetime.now()
print(now)
year = lambda x: x.year
print(year(now))


def do_something(f, val):
    return f(val)


func = lambda x: x ** 3
print(func(16))
print(do_something(func, 3))

# final example
# replaces "." with a " " one time. If theres 1 . , it will be replaced for an empty string. Then .isdigit() will be
# used to determine if isnum is a number.

isnum = lambda q: q.replace(".", "", 1).isdigit()
print(isnum('24379'))
print(isnum('3.1415'))
print(isnum('T53'))
print(isnum("-16"))

# .lstrip() takes out the whitespaces in front and .rstrip() for the ones in the back.
is_num = lambda r: isnum(r.lstrip()[1:]) if r.lstrip()[0] == "-" else isnum(r)
print(is_num("  -17"))

tonum = lambda s: float(s) if is_num(s) is True else -1
print(tonum("  -345")), print(type(tonum(" -93.54")))
