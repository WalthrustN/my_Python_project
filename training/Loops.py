print(" loops ")

names = ["Jamilia", "Jacob", "Jackie", "Jerome"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

for name in names:
	print(name)

print("Loop Example 2")

nums = [1, 2, 3, 4, 5, 6]

for num in nums:
	if num == 3:
		print("found")
		break
	print(num)

# in this code we are changing num into a variable
# just by line 16 the corresponds to num's index.
# so if you print nums with for num in nums, you
# will start with the first num which is index 0 of
# nums.  +  Break stops the for loop.

for num in nums:
	if num == 3:
		print("found")
		continue
	print(num)
	
#continue goes to the next num.

for num in nums:
	for eye in "eyes":
		print(num,eye)

print("for a certain number of iterations")
for i in range(10):
	print(i)

print("")
print("For Loop with Range")
print("")

for i in range(4, 11, 2):
	print(i)

for byte in b'[Binary, ten]{}':
	print(byte)

for letter in "Word":
	print(letter)

c = 2997582
digits = [int(d) for d in str(c)]

for digit in digits:
	print(digit)

