
# 6. Bonus Questions
# Write a program that counts how many vowels are in a given string.

name = "Chetan Patil"
count = 0
vowels = "aeiou" 

for ch in name.lower():
    if ch in vowels:
        count+=1

print("total vowels",count)        



         