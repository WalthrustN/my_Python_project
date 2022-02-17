movies = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("Its a Wonderful Life", 1946), ("Gattaca", 1997),
          ("No Country for Old Men", 2007), ("Rear Window", 1954), ("The Lord of the Rings: The Fellowship of the Ring",2001),
          ("Groundhog Day", 1993), ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001),
          ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

#Filter though the movies to find movies made before 2000

pre2000s = [title for (title, year) in movies if year < 2000]
print(pre2000s)

#Using LC to do vector multiplication
v = [2, 3, 1]
print(4*v)

x = [4*y for y in v]
print(x)

t = [2, 4, 6] + [1, 3]
print(t)

#Cartesian Product

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)

