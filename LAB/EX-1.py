#EX-1 Split the word,scentence
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

text = "Python is easy to learn. Python is powerful and useful. I love learning Python."

print("Sentences:", sent_tokenize(text))

words = word_tokenize(text)
print("Words:", words)

words = [w.lower() for w in words if w.isalpha()]

print("Word Count:", len(words))

print("Most Frequent:", Counter(words).most_common(1))

print("Top 3 Most Frequent:", Counter(words).most_common(3))
