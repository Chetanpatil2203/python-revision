# Create a dictionary of three friends and their phone numbers. Use:

# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

friends = {

    "vihaan": 83456865,
    "yuvi" : 383949202,
    "kshyap": 93839202
}

print(friends.keys())
print(friends.values())

for key,value in friends.items():
    print(f"{key} : {value}")