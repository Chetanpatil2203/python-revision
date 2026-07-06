# ⭐ Question 6: Grade Calculator

# Write a program that prints the grade based on the marks.


# 90–100	A
# 80–89	B
# 70–79	C
# 60–69	D
# Below 60	F

marks = 80
if marks>100:
    print("check your marks")
elif marks>=90:
    print("A")
elif marks>=80:
    print("B") 
elif marks>=70:
    print("C")   
elif marks>=60:
    print("D")    
else:
    print("F")        