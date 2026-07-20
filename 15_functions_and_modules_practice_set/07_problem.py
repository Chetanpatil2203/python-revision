# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

num = [1,2,3,4,5]

square = map(lambda x: x*x,num)
print(list(square))
