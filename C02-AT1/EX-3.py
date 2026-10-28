# NLP Assessment - Question 3
# Stemming-Based Preprocessing for Search Engine

import re

words = ["played", "player", "playing"]

print("STEMMING-BASED PREPROCESSING")
print("-" * 75)

for word in words:

    stem = word
    suffix = ""
    transformation = "Root Word"

    if re.search(r"ed$", word):
        suffix = "-ed"
        stem = re.sub(r"ed$", "", word)
        transformation = "Inflectional"

    elif re.search(r"er$", word):
        suffix = "-er"
        stem = re.sub(r"er$", "", word)
        transformation = "Derivational"

    elif re.search(r"ing$", word):
        suffix = "-ing"
        stem = re.sub(r"ing$", "", word)
        transformation = "Inflectional"

    print("\nOriginal Word       :", word)
    print("Extracted Stem     :", stem)
    print("Removed Affix      :", suffix)
    print("Transformation Type:", transformation)
    print("Normalized Form    :", stem)
    print("-" * 40)
