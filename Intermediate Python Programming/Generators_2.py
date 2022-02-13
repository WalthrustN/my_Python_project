#A Function using Yield instead of Return is called a generator function or simply a generator.
import string

#Generate the lower case English Letters
def letters():
    for c in string.ascii_lowercase:
        yield c

for letter in letters():
    print(letter)

print(type(string.ascii_lowercase))