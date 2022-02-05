print("Creating Functions")
name = "tom"

def gret():
	print("happy to meet you")
	
# We created a function with no arguments

def greet(name):
	print(f"happy to meet you {name}")
	
# We created a function with one argument, name.

greet("James")
gret()

def greetings(name, age):
	print(f"hello,{name}, how's it going")
	if age > 10 :
		print(f" how does it feel to be {age}.")
		
greetings("Nathaniel", 28)


def isAdult(age):
	return age > 16

print(isAdult(28))

def genderConverter(Gender = "Unknown"):
	if Gender.upper() == "M":
		return "MALE"

	elif Gender. upper() == "F":
		return "FEMALE"
	
	else:
		return f"Gender {Gender} is Unknown"
	
print(genderConverter("m"))
print(genderConverter("M"))
print(genderConverter("f"))
print(genderConverter("F"))
print(genderConverter("Male"))

	
	
	