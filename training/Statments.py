# If Statements
number = 0

if number > 0:
	print(f"{number} is positive")
elif number == 0:
	print("This number is 0")
elif number < 0:
	print(f"{number} is negative")

#Ternary If Statements
number = 1
message = "positive" if number > 0 else "0 or negative"
print(message)
