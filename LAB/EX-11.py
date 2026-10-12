
# Experiment 11: Morphological Analysis Using NLTK

!pip install nltk

import nltk
from nltk.stem import PorterStemmer
from collections import Counter

stemmer = PorterStemmer()

text = "The boys are playing and the girls are running."
words = nltk.wordpunct_tokenize(text)

print("Original Words:", words)

print("\nMorphological Analysis:")
for word in words:
    if word.isalpha():
        print(word, "-> Root:", stemmer.stem(word))

print("\nWord Frequency:")
print(Counter(w.lower() for w in words if w.isalpha()))
