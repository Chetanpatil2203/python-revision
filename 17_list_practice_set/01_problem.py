# # Create a list of the squares of only the even numbers from 1 to 20.

# Expected Output:

# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# Challenge: Try to solve it in one line using list comprehension. No hints this time! 🚀

square = [x*x for x in range(1,21) if x%2 ==0]
print(square)