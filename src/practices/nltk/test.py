import re

import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords, words

nltk.download('averaged_perceptron_tagger_eng')
nltk.download('words')
nltk.download('punkt_tab')
nltk.download('stopwords')

if __name__ == '__main__':
    with open("2b0rnot2b.txt", "r") as f:
        text = f.read()

    # Lowercasing
    text = text.lower()

    # Remove punctuations
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove whitespaces
    text = text.strip()

    # Part of speech recognition
    # tagged = pos_tag(tokens)
    # print(f"Apart of speech: {tagged}")
    # print("--------------------------------")

    # Tokenize
    tokens = word_tokenize(text)
    print(f"Tokens: {len(tokens)} - {tokens}")
    print("--------------------------------")

    # Remove stopwords
    stop_words = stopwords.words("english")
    # print(stop_words)
    tokens = [w for w in tokens if w not in stop_words]
    print(f"Tokens after stopword removal: {len(tokens)} - {tokens}")
    print("--------------------------------")

