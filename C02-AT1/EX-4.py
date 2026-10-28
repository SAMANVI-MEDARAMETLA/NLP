# NLP Assessment - Question 4
# Finite-State Morphological Parsing

import re

words = ["writes", "writing", "written"]

# Irregular verb dictionary
irregular_forms = {
    "written": "write"
}

# Finite-state transition model
transitions = {
    "Q0": {
        "s": "Q1",
        "ing": "Q2",
        "irregular": "Q3"
    }
}

print("FINITE-STATE MORPHOLOGICAL PARSING")
print("-" * 75)

for word in words:

    root = word
    suffix = ""
    inflection = "Regular"
    path = "Q0"

    if word in irregular_forms:

        root = irregular_forms[word]
        suffix = "irregular form"
        inflection = "Irregular"
        path = "Q0 -> Q3 -> QF"

    elif re.search(r"ing$", word):

        root = re.sub(r"ing$", "", word)
        root = root + "e"
        suffix = "-ing"
        path = "Q0 -> Q2 -> QF"

    elif re.search(r"s$", word):

        root = re.sub(r"s$", "", word)
        suffix = "-s"
        path = "Q0 -> Q1 -> QF"

    print("\nInput Word          :", word)
    print("State Transition   :", path)
    print("Morphological Form :", root + " + " + suffix)
    print("Root Word          :", root)
    print("Inflection Type    :", inflection)
    print("Normalized Output  :", root)
    print("-" * 40)
