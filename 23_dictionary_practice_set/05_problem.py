# Write a program that merges two dictionaries into one.


student1 = {
    "name": "John",
    "age": 20
}

student2 = {
    "grade": "A",
    "city": "Delhi"
}

# for key,value in student2.items():
#     student1[key] = value


# print(student1)

student1.update(student2)

print(student1)
