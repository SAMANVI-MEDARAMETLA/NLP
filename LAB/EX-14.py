# Experiment 2.1: Bigram Counting and Next Word Prediction

from nltk.util import bigrams
from collections import Counter

text = "I want to eat. I want to sleep. I want to eat food."

words = text.lower().replace(".", "").split()
bg = list(bigrams(words))

print("Bigrams:", bg)
print("Bigram Count:", Counter(bg))

word = input("Enter a word: ").lower()
next_words = [b[1] for b in bg if b[0] == word]

if next_words:
    print("Next word prediction:", Counter(next_words).most_common(1)[0][0])
else:
    print("No next word found")
