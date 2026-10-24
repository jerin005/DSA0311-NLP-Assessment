def plural(word):
    if word.endswith("y") and word[-2] not in "aeiou":
        return word[:-1] + "ies"

    elif word.endswith(("s", "x", "ch", "sh")):
        return word + "es"

    else:
        return word + "s"


words = ["cat", "bus", "box", "watch", "baby"]

for word in words:
    print(word, "->", plural(word))
