# 4. Recursion in Python

# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def find_sum(num):
    
    if num == 0:
        return 0
    return num%10 + find_sum(num//10)

print(find_sum(1234))