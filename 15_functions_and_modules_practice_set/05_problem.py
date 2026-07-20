# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)

def calculate_area(length,width=10):
    area = length*width
    return area

print(calculate_area(10))
print(calculate_area(10,10))
