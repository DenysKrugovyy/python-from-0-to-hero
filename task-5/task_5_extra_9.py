words = ["hi", "hello", "hey", "world", "python"]
res = {}

for w in words:
    if (len(w)) in res:
        res[(len(w))].append(w)
    else:
        res[(len(w))] = [w]

print(res)




# Очікуваний результат:
# {
#   2: ["hi"],
#   3: ["hey"],
#   5: ["hello", "world"],
#   6: ["python"]
# }
