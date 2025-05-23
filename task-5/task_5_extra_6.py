words = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
uniq = []

for w in words:
    if w not in uniq:
        uniq.append(w)

print(uniq)



# Очікуваний результат:
# ["apple", "banana", "orange", "kiwi"]
