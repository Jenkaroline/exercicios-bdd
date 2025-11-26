print("--------------------------------")
print(f"Math and String Operations")
print("--------------------------------")

print(f"2 + 2 = {2 + 2}")

name = "Jen"
print(f"My name is {name}")
print("My name is {}".format(name))



#letter f, in this case, means formatted string literal. 
#it means that I will put an operation inside my String  
# also it could be:

#math operations
cm = input("Enter a value in centimeters: ")
cent = (int(cm)) / 100

print(f"{cm} cm is equal to {cent:.2f} meters.")
