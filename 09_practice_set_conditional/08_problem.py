# 🔥 Next Question (Very Common Interview Question)
# Question 7: Voting Eligibility

# Write a program to check whether a person can vote.

# Rules
# Age 18 or above → "Eligible to Vote"
# Age below 18 → "Not Eligible to Vote"
# If age is less than 0 or greater than 120, print "Invalid Age"
age = 19
if age<0 or age>120:
    print("Invalid Age")
elif age>=18:
    print("Eligible to vote")
else:
    print("not eligible to vote")   
