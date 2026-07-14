# Write a program to count the number of digits in a number.
# 987654

count = 0
num = 987654

while num>0:
    num = num//10
    count+=1

print(f"number of digits {count}")    


# using for loop

count = 0 
num = "987654"

for digit in num:
    count+=1

print(int(count))    




    