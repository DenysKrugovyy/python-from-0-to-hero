def capitalize_words(s):
    l = s.split(" ")
    cap = []
    for w in l:
        cap.append(w.capitalize())
    return(" ".join(cap))

print(capitalize_words("hello world"))