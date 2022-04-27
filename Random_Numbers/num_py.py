import numpy as np

# I had to install this package from the Interpreter Section of the settings.
# numpy stands for numerical python and is an excellent way to deal with arrays and just large amounts of data.

# Reference:
# https://www.youtube.com/watch?v=z99Pgl1UklM
# https://www.youtube.com/watch?v=HGOBQPFzWKo&t=7243s
# date:04/26/2022

new_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(new_matrix)
np.random.shuffle(new_matrix)
print(new_matrix)

# a = np.random.rand(3)
a = np.random.rand(3, 3)
# b = np.random.randint(0, 10, 3)
b = np.random.randint(0, 10, (3, 3))
print(a, end='\n\n')
print(b, end='\n\n')
