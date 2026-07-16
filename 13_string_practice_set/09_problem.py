# Take a user input string and check if it is a palindrome (same forwards and backwards).

text = input("enter your text")
rev = text[::-1]

if text == rev:
    print("Is Palindrome")
else:
    print("not Palindrome")