# NLP Assessment - Question 2
# Stemming for Text Normalization

import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt', quiet=True)

# Create Porter Stemmer
ps = PorterStemmer()

# Input words
words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying",
    "connected",
    "connecting",
    "connection"
]

print("STEMMING USING PORTER STEMMER")
print("-" * 50)

for word in words:

    stem = ps.stem(word)

    print("Input Word :", word)
    print("Stem Word  :", stem)
    print("-" * 30)
