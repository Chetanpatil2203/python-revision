# Given:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using one list comprehension, create this output:

# ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

# 💡 This introduces a new feature of list comprehensions: if ... else inside the expression.

# Try it on your own first. This is one of the most common list comprehension interview questions.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["even" if num%2==0 else "odd" for num in numbers]
print(result)