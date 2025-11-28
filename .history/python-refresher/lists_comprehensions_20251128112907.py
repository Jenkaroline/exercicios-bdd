# doubling values in a list.

numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers]

# numbers.append(4)
# numbers.remove(4)
# for number in numbers:
#     doubled.append(number * 2)

print(f"Lista normal: {numbers}.")
print(f"Lista dobrada: {doubled}.")

# filtering names with S from a list
names = ["Sara", "Samanta", "Robert"]
s_names = [x.startswith("S") for x in names]
print(f"Nomes com S: {s_names}.")

