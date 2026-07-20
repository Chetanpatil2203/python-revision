# # local variable and global variable

# x = 10
# def my_func():
#     x = 19
#     print(x)

# my_func()    
# print(x)


#using global keyword

# def my_func():
#     global x
#     x = 10
  

# my_func()    
# print(x)

#doctsring

def add (a,b):
    """
    return sum of a b
    parameters
    int(a): first parameters
    int(b): second parameter
    return sum of a b

    """
    return a+b
print(add(3,2))  
print(add.__doc__)  