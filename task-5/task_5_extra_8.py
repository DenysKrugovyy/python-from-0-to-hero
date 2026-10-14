text = "Banana Apple"
res = {}

for l in text:
    if l in res:
        if l != " ":
            res[l] += 1
    else:
        res[l] = 1

print(res)

# Очікуваний результат (приклад):
# {'b': 1, 'a': 4, 'n': 2, 'p': 2, 'l': 1, 'e': 1}
