# Print the following pattern using a for loop:

# *
# **
# ***
# ****

# for i in range(1,5):
#     print("*"*i)

for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()    


