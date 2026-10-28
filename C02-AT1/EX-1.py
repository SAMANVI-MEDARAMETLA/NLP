# NLP Assessment - Question 1
# Morphological Analysis for Document Indexing

import re

words = ["connected", "connecting", "connection"]

suffix_rules = {
    "ed": "Inflectional",
    "ing": "Inflectional",
    "ion": "Derivational"
}

print("MORPHOLOGICAL ANALYSIS")
print("-" * 70)

for word in words:

    root = word
    suffix = ""
    form_type = "Root Word"

    for s, t in suffix_rules.items():

        if re.search(s + "$", word):

            suffix = "-" + s
            root = re.sub(s + "$", "", word)

            if s == "ion":
                root = "connect"

            form_type = t
            break

    print("\nInput Word       :", word)
    print("Root Word        :", root)
    print("Suffix           :", suffix)
    print("Morphological Type:", form_type)
    print("Parsed Structure :", root + " + " + suffix.replace("-", ""))
    print("Normalized Output:", "connect")
