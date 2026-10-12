
# Experiment 13: Porter Stemming Algorithm

from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "playing", "played", "plays",
    "walking", "walked", "walks",
    "studies", "studying", "happiness",
    "connected", "connection"
]

print("Porter Stemming Results")
print("-" * 35)

for word in words:
    stem = ps.stem(word)
    print(word, "->", stem)
