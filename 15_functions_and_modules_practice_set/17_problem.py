# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2)+fib(n-1)



def fibonacci(n):
    for i in range(n):
        print(fib(i),end = " ")

print(fib(6))
fibonacci(6)

