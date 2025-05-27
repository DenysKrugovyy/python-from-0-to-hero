words = ["apple", "banana", "apple", "orange", "banana", "kiwi", "apple"]
res = {}

for w in words:
    if w in res:
        res[w] += 1
    else:
        res[w] = 1

print(res)