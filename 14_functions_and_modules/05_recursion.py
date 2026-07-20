# print factorial of 5 using recursion

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(5))


#print fibonacci series

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2)+fib(n-1)

print(fib(6))
