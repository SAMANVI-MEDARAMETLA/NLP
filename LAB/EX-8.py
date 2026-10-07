#Experiment 8: Morphological Analysis using NLTK

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["playing", "played", "studies", "cars"]

for word in words:
    print(word, "-> Stem:", stemmer.stem(word))
