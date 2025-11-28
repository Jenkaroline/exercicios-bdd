numbers = [1, 2, 3]
doubled = []

numbers.append(4)
numbers.remove(2)

print(numbers)

for number in numbers:
    doubled.append(number * 2)

print(f"Lista normal: {numbers}.")
print(f"Lista dobrada: {doubled}.")