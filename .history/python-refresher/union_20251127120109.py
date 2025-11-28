local_friends = {"Marcolas", "João", "Jen"}
abroad = {"Marcolas", "João"}

total = abroad.union(local_friends)
print(total)

colleagues = {"Caio", "John", "Peter"}
names = {"John", "Peter"}

qa = names.difference(colleagues)
print(qa)