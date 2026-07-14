# Write a program that prints the first n Fibonacci numbers.

# Example 1

# Input

# 5

# Output

# 0
# 1
# 1
# 2
# 3

n = int(input("enter your num"))
a = 0
b = 1
count = 0

while count<n:
    print(a)
    c = a+b
    a = b
    b = c
    count+=1
