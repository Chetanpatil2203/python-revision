# 🟡 Question 2: Palindrome Number

# Problem:

# Check whether a number is a palindrome.

# A palindrome number reads the same forwards and backwards.



num = 121
rev = 0
copy = num

while copy>0:
    digit = copy%10
    rev = digit+rev*10
    copy = copy//10

print(rev)  
if num == rev:
    print("number is palindrome")
else:
    print("number is not palindrome")    