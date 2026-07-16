# 3. String Methods and Functions
# Take the string "  i love python programming  " and:

# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears
# Check if the string is alphanumeric.


text = "  i love python programming  " 

print(text.strip())
print(text.strip().title())
print(text.count("o"))
print(text.strip().isalnum())