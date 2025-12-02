print((lambda x, y: x + y)(2, 3))  # Output: 5

def double(i):
    return i * 2

sequence = [1, 2, 3, 4, 5]
# first way using map and a named function
doubled = list(map(double, sequence))
print(doubled)  # Output: [2, 4, 6, 8, 10]

doubled = [x * 2 for x in sequence]
print(doubled)