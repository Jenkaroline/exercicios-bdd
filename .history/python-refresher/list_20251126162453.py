l = ["Je", "Jen", "Jennifer"] #i can change values
t = ("Je", "Jen", "Jennifer") #i can't change values
s = {"Je", "Jen", "Jennifer"} # it doesn't keep order / i can't have duplicates

l.append("Jenny")
l.remove("Je")
print(l)

s.append("Jenny")
l.remove("Je")
print(l)


