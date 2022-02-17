#Lists comphensions help when filtering though list.

# A list comprehension has square brackets like a list, but uses an expression with for loops and statements.

#List: [1, 2, "a", 3.14]


#List Comprehensions:
    #[expr for val in list 1 (collecton 1)]
    #[expr for val in list 1 (collecton 1) if <statement>]
    #[expr for val in list 1 (collecton 1) if <statement1> and if <statement2>]
    #[expr for val1 in list 1 (collecton 1) and val2 in list 2 (collecton 2)]

squares = []
for i in range(1,101):
    squares.append(i**2)

print(squares)

#Same thing using List Comprehension
squares2 = [i**2 for i in range(1,101)]
print(squares2)