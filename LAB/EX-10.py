
# Experiment 10: Generate Word Forms

words = ["walk", "play", "happy", "fast", "box"]

for word in words:
    print("\nWord:", word)

    # Plural form
    if word.endswith(("s", "x", "ch", "sh")):
        print("Plural:", word + "es")
    elif word.endswith("y") and word[-2] not in "aeiou":
        print("Plural:", word[:-1] + "ies")
    else:
        print("Plural:", word + "s")

    # Past tense
    if word.endswith("e"):
        print("Past tense:", word + "d")
    elif word.endswith("y") and word[-2] not in "aeiou":
        print("Past tense:", word[:-1] + "ied")
    else:
        print("Past tense:", word + "ed")

    # Comparative and superlative
    if word.endswith("y") and word[-2] not in "aeiou":
        print("Comparative:", word[:-1] + "ier")
        print("Superlative:", word[:-1] + "iest")
    else:
        print("Comparative:", word + "er")
        print("Superlative:", word + "est")
