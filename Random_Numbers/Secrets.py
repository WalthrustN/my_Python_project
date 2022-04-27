import secrets

a = secrets.randbelow(15)  # Generates a number below (n).
# a = secrets.randbits(4) #Generates a number using (n) bits.
mylist = list('ABCDEFGHI')
b = secrets.choice(mylist)

print(a, b)
