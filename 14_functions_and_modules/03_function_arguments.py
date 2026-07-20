#In function three types of arguments

#Positional Arguments
def add(a,b):
    return a+b

print(add(3,4))


#default arguments
def add(a,b, c=4):
    return a+b+c

print(add(3,2))


#keyword arguments
def bio(name,age):
    return f"name:{name}, age:{age}"

print(bio(name = "chetan", age = 24))