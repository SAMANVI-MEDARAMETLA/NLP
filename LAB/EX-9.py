#Experiment 9: Finite-State Machine for Plural Forms

def plural(word):
    state = "q0"

    if word.endswith(("s", "x", "ch", "sh")):
        state = "q1"
        result = word + "es"
    else:
        state = "q2"
        result = word + "s"

    print(word, ":", state, "->", result)


words = ["cat", "book", "bus", "box", "watch", "dish"]

for word in words:
    plural(word)
