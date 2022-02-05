# Object Oriented progamming involves you creating a
# bunch of classes and connect them together.

# Classes are basically a model or blueprint of
# anything. Objects are in a class. There are many classes out there.
# for creating anything. A class is just a template. ex. A tree class,
# might have oak tree, cedar tree, walnut tree, cherry tree as objects.

class Phone:
	def __init__(self, brand, price):
		self.brand = brand
		self.price = price
	
	def call(self, phone_number):
		print(f"{self.brand} is calling {phone_number}")
	
	def __str__(self) -> str:
		return f"Brand: {self.brand}\nPrice: {self.price}"


Iphone = Phone("Iphone 12", 1000)

print(Iphone.price)
print(Iphone.brand)
print(Iphone)

Iphone.call(9172320753)

Samsung = Phone("Note 20", 900)


