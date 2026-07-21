# Next Challenge (Slightly Harder)

# Given:

# 

# Using list comprehension, create a new list that contains only the names whose length is greater than 4.

# Expected Output:

# ["rahul", "priya", "rohit"]

names = ["rahul", "amit", "priya", "neha", "rohit"]

new_names =[name for name in names if len(name)>4] 
print(new_names)