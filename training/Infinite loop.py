#x = 0
#while True:
#	print(x)
#	x += 1

person = {
	"name": "Naitini",
	"age" : 21,
	"address" : "UK"
}

for key in person:
	 print(f"key:{key} value:{person[key]}")
	
for key, valu in person.items():
	print(f"key:{key} value:{valu}")
	