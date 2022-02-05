print("Tuples: ordered, immutable, allows for duplicate elements")

mytuple = (0, 1, (5, 10), 12, 7, 9, 10, 15, 7, 2, 12, 3, 7, 9, 10, 15, 12)
mylist = list(mytuple)

print(mytuple)
print(mylist)

mylist[3] = 10
print(mylist)

print(mytuple[::2])
print(mytuple[1::2])

# b = [i * i for i in mytuple]
# print(b)

number = 5, 10

if number in mytuple:
	print(f"yes {number} is in there.")

else:
	print(f" The {number} is not in here.")
	

print(mytuple.count(7))

print (mytuple.index(2))

i1, *uni, i3 = mytuple
print(i1)
print(uni)
print(i3)

# With a tuple data structure you can create i1, *i2, i3 =the tuple and
# because tuples are immutable and cant be changed, the syntax turns
# i1 and i3 into the first and last numbers of the tuple and i2 becomes
# a list.

