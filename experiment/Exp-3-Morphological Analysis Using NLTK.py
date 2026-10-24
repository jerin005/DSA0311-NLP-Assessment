from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "running",
         "studies", "cats", "connected"]

print("Morphological Analysis")

for word in words:
    stem = stemmer.stem(word)
    print(word, "->", stem)
