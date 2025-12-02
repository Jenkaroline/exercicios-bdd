friends = {"John": 22, "Bella": 23, "Mike": 21}
print(friends["John"])

# i can modify values
friends["John"] = 23
print(friends["John"])

for name in friends:
    print(name)

# or do a list of dicts
friends_list = [
    {"name": "John", "age": 22},
    {"name": "Bella", "age": 23},
    {"name": "Mike", "age": 21},
]
print(friends_list[0]["name"])

# for, if and accessing values
for friend in friends_list:
    if friend["age"] > 21:
        print(friend["name"])

# adding new key-value pairs
friends["Alice"] = 24
print(friends)