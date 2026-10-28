# NLP Assessment - Question 5
# Porter Stemmer-Based Processing

import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer
ps = PorterStemmer()

# Input words
words = ["relational", "relation", "relate"]

print("PORTER STEMMER PROCESSING")
print("-" * 50)

for word in words:

    # Preprocessing
    word = word.lower()

    # Apply Porter Stemmer
    stem = ps.stem(word)

    print("\nInput Word :", word)
    print("Stem Word  :", stem)
    print("Normalized :", stem)

    print("-" * 30)
