print("Dictionary: Key Value Pairs, Unordered, Mutable")

mydict = {"name":"Max" ,
          "age": 28 ,
          "city": "New York" }
print(mydict)

mydict2 = dict(name = "Mary", age = 27, city = "Boston")
print(mydict2)

# When you use dict() to make a dictionary your keys dont have to be in
# a ".

mydict2["email"] = "Maryd345@gmail.com"
print(mydict2)

del mydict2['name']
mydict2.pop("age")
mydict2.popitem()
print(mydict2)

if "city" in mydict2:
    mydict2["email"] = "Maryd345@gmail.com"
    print(mydict2)

for key, value in mydict2.items():
    print(key, value)

