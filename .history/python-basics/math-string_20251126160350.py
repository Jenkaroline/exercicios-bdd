print("--------------------------------")
print(f"Math and String Operations")
print("--------------------------------")

name = "Jen"
print(f"My name is {name}")

#letter f, in this case, means formatted string literal. 
#it means that I will put an operation inside my String  
# also it could be:

print(f"2 + 2 = {2 + 2}")


print("--------------------------------")
print(f"Converting cm to meters")
print("--------------------------------")

#math operations
cm = input("Enter a value in centimeters: ")
cent = (int(cm)) / 100

print(f"{cm} cm is equal to {cent:.2f} meters.")
