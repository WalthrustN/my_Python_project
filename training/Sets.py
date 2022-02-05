"List Vs Set"
numberList = [1, 1, 2, 3, 4, 5, 1]
numberSet = {1, 1, 2, 3, 4, 5, 1}
print(numberList)
print(numberSet)

# In a set, this data type keeps only one occurrence of the value. +
# the syntax is different {} instead of () +
# the order is not guaranteed.

letterSet = {"A", "A", "B", "B", "C"}
print(letterSet)

print("Set Union (OR), Intersection(AND), Difference(Subtraction)")
lettersA = {"A", "B", "C", "D", "F" }
lettersB = {"E", "F" }
print(lettersA | lettersB)
print(lettersA & lettersB)
print(lettersA - lettersB)

