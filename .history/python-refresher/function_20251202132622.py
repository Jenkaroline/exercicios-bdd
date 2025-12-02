def age_in_second():
    age = int(input("Enter your age: "))
    second = age * 24 * 365 * 60 * 60
    print(f"Your age in seconds is: {second}")

friends = ["John", "Bella", "Mike"]
def add_name():
    name = input("Enter a name: ")
    friends.append(name)
    print(f"Updated friends list: {friends}")

add_name()
age_in_second()