# Problem:

# Write a program to find the sum of all digits in a number.

num = 12345
sum = 0

while num>0:
    digit = num%10
    sum = sum+digit
    num = num//10

print(sum)    