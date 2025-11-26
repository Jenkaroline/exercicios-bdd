print("--------------------------------")
print(f"Math and String Operations")
print("--------------------------------")

#String operations
name = "Jen"
print(f"My name is {name}")
print("My name is {}".format(name))

#String concatenation
cm = input("Enter a value in centimeters: ")
cent = int(cm) / 100

print(f"{cm} cm is equal to {cent:.2f} meters.")
