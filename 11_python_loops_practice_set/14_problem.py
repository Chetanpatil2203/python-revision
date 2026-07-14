# Write a program to reverse a number.

# Example:

# Input:

# 12345

# Output:

# 54321


num = 12345
reverse = 0

while num>0:
    digit = num%10
    reverse = reverse*10+digit
    num = num//10

print(reverse)    