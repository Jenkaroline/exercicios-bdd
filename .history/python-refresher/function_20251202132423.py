def age_in_second():
    age = int(input("Enter your age: "))
    second = age * 24 * 365 * 60 * 60
    print(f"Your age in seconds is: {second}")

def add_name():
    names = []
    while True:
        name = input("Enter a name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        names.append(name)
    print("Names entered:", names)