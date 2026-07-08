import re

import gensim.models
import nltk
from nltk import word_tokenize, pos_tag, sent_tokenize
from nltk.corpus import stopwords, words

from gensim.models import Word2Vec

nltk.download('averaged_perceptron_tagger_eng')
nltk.download('words')
nltk.download('punkt_tab')
nltk.download('stopwords')

if __name__ == '__main__':
    with open("quant_ent.txt", "r") as f:
        text = f.read()

    # Lowercasing
    text = text.lower()

    # Remove punctuations
    # text = re.sub(r"[^\w\s]", " ", text)

    # Remove whitespaces
    text = text.strip()

    # Part of speech recognition
    # tagged = pos_tag(tokens)
    # print(f"Apart of speech: {tagged}")
    # print("--------------------------------")

    # Tokenize
    tokens = []
    st = sent_tokenize(text)
    print(f"Sentence token count >>> {len(st)}")
    for s in st:
        temp = []
        s = re.sub(r"[^\w\s]", " ", s)
        for w in word_tokenize(s):
            temp.append(w)
        tokens.append(temp)
    # tokens = word_tokenize(text)

    print(f"Sentence Tokens: {len(tokens)} - {tokens}")
    print("--------------------------------")

    # Remove stopwords
    # stop_words = stopwords.words("english")
    # # print(stop_words)
    # tokens = [[w for w in s if w not in stop_words] for s in tokens]
    # print(f"Tokens after stopword removal: {len(tokens)} - {tokens}")
    # print("--------------------------------")

    # Vocabulary
    vocab = list()
    for s in tokens:
        vocab += set(s)
    vocab = vocab
    vocab = set(vocab)
    print(f"Vocabulary: {len(vocab)} - {vocab}")
    print("--------------------------------")

    # Bag of words
    bag = dict()
    for s in tokens:
        for t in s:
            if not bag.__contains__(t):
                bag[t] = 0
            bag[t] += 1

    print(f"Bag of words: {bag}")
    print("--------------------------------")

    # Word to vector
    word1 = 'superposition'
    word2 = 'entanglement'
    print(f"Cosine similarity of \"{word1}\" and \"{word2}\"")
    model = Word2Vec(tokens, min_count=1, vector_size=100, window=20)
    print(f"CBOW : {model.wv.similarity(word1, word2)}")
    sg_model = Word2Vec(tokens, min_count=1, vector_size=100, window=20, sg=1)
    print(f"Skip gram: {sg_model.wv.similarity(word1, word2)}")

