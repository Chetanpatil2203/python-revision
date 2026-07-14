# # Write a program to find the factorial of a number using a while loop.
# num = int(input("enter your num: "))
# fact = 1
# i = 1

# while i<=num:
#     fact*=i
#     i+=1

# print(f"factorial of {num} is {fact}") 



#solve using for loop

num1 = int(input("enter your num"))
fact1 = 1
for i in range(1,num1+1):
    fact1*=i

print(f"factorial of {num1} is {fact1}")     



