#EX-2 Spell check
from spellchecker import SpellChecker
spell = SpellChecker()
text = "I am lerning machne learnng"
words = text.split()
for word in words:
    correction = spell.correction(word)
    if correction != word:
        print(word, "->", correction)
