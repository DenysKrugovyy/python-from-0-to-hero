words = ["apple", "banana", "avocado", "grape", "ananas"]
check = "a"
nub = 0

for i in words:
    for x in i:
        if x == check:
            nub += 1

print(nub)
