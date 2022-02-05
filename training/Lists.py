# Lists
number_zero = 0
number_one = 1
number_two = 2

numbers = [1, 2, 3, 4, -1, -6, ["A", "B", "C"]]
print(numbers[0])
print(numbers[6][1])

# to call a number in the list, you have indexes starting with 0, in
# order to call the first number which is index 0 variable[index?]

# List Methods
print("Sort Method 1")
numbers = [1, 2, 3, 4, -1, -6, ]
print(sorted(numbers))

print("Sort Method 2")
numbers = [1, 2, 3, 4, -1, -6, ]
(numbers.sort())
print(numbers)

print("Reverse")
numbers.reverse()
print(numbers)

print("Append and length")
numbers.append(13)
print(numbers)
print(len(numbers))

# clear numbers
# numbers.clear()
# Find out if numbers in lists
print(5 in numbers)

print("Remove Method")
# Remove an index from the list
# remove - only removes the first instances of the list
numbers.remove(-6)
print(numbers)

print("Remove Method 2")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.pop()
numbers.pop()
print(numbers)
# pop removes the last index in the list

print("Remove Method 3")
del numbers[1:4]
print(numbers)
# removes numbers in the list by indexing

mylist2 = ["banana", "cherry", "apple", ["A", "B", "C"]]
print(mylist2[1:])

if "C" in mylist2:
	print("yes")

else:
	print("no")

print(mylist2[1:-2])

listcpy = mylist2.copy()

listcpy.append("lemon")

print(listcpy)
print(mylist2)

#if i didnt use.copy both would get the appended lemon, instead of just
# one.
