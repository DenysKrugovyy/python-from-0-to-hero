fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}

for f in fruits:
    if f in counts:
        counts[f] += 1
    else:
        counts[f] = 1

print(counts)
