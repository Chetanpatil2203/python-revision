# Create a program that checks if a person is eligible to vote (age >= 18). 

age = int(input("enter your age"))

if age<0 or age>=120:
    print("You enter invalid age")
elif age>= 18:
    print("Person is eligible to vote")    
else:
    print("Person is not eligible to vote")    
