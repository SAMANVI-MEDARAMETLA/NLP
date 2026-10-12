
# Experiment 12: Derivational Suffix Analysis

words = ["careless", "helpful", "happiness",
         "quickly", "teacher"]

suffixes = {
    "less": ("adjective", "without"),
    "ful": ("adjective", "full of"),
    "ness": ("noun", "state or quality"),
    "ly": ("adverb", "in a manner"),
    "er": ("noun", "a person who performs an action")
}

for word in words:
    print("\nWord:", word)

    found = False
    for suffix, (pos, meaning) in suffixes.items():
        if word.endswith(suffix):
            base = word[:-len(suffix)]

            # Handle a common spelling change
            if suffix == "ness" and base.endswith("i"):
                base = base[:-1] + "y"

            print("Base word:", base)
            print("Suffix:", suffix)
            print("Word class:", pos)
            print("Meaning:", meaning)
            found = True
            break

    if not found:
        print("No known suffix found")
