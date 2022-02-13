#Similar to List Comprehension but instead of [] sqaure brackets, you use () parentheses

#for example this generator expression will generate the sqaures of all the positive integers.

import itertools
import sys

#Generator Expression
squares = (x**2 for x in itertools.count(1))

for x in squares:
    print(x)
    #close if the square generator expession exceeds a certain value.
    if x > 500:
        squares.close()
        #break

#get the size of the generator expression
print(sys.getsizeof(squares))