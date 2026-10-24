from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "connected",
         "connection", "fairness", "easily"]

print("Porter Stemmer Results")

for word in words:
    print(word, "->", ps.stem(word))
