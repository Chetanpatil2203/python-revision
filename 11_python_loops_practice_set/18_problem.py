# ⭐ Final Challenge: Prime Number

# Write a program that:

# Takes a number as input.
# Checks whether it is Prime or Not Prime.
# Prints:
# "Prime Number" or
# "Not Prime Number"
# Example 1

# Input:

# 13

# Output:

# Prime Number

n = int(input("enter your num"))
is_prime = True
i = 2

while i<n:
    if n%i == 0:
        is_prime = False
        break
    i+=1

if n>1 and is_prime:
    print("Prime Number")   
else:
    print("Not Prime Number")     
