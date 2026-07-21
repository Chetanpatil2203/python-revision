# 3. Tuples and Operations on Tuples
# Create a tuple coordinates = (10, 20) and print both elements.
# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.


coordinates = (10, 20)
print(coordinates)

# #try to modify 
# coordinates[0] = 50
# print(coordinates)

new_tuple = list(coordinates)
new_tuple[0] = 50
print(new_tuple)

new = tuple(new_tuple)
print(new)