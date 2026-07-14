# Print the multiplication table of a number (entered by user).

num = int(input("enter a num : "))
for i in range(1,11):
    print(f"{num}*{i}={i*num}")