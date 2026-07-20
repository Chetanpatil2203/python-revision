# Write a recursive function factorial(n) that returns the factorial of a number.

def find_fact(n):
    if n == 1:
        return 1
    return n*find_fact(n-1)

print(find_fact(5))