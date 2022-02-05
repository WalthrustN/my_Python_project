usernames = ("kaner45", "rickster25", "nicenippy")
print(type(usernames))
looper1 = usernames.__iter__()
print(type(looper1))

print(looper1.__next__())
print(looper1.__next__())
print(looper1.__next__())

print("Iterable method 2")

usernames2 = ('nickels555', 'vombraider9', 'mickeykeys')
looper2 = iter(usernames2)

print(next(looper2))
print(next(looper2))
print(next(looper2))

print("""Iterable method 3\n next line""")

users = [ 'rattyana95', 'curlyswirls', 'fnbossybrat']

# for user in users:
#     print(users)

looper3 = iter(users)
while True:
    try:
        user = next(looper3)
        print(user)
    except StopIteration:
        break
