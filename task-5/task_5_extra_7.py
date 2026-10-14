words = ["cat", "elephant", "dog", "giraffe"]
long = ""

for word in words:
    if len(word) > len(long):
        long = word

print(long)

# Очікуваний результат:
# "elephant"
