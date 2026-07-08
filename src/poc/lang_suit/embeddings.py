from langchain_openai import OpenAIEmbeddings
import numpy as np

embedder = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=3072)


def cosine_similarity(a_str, b_str):
    a = embedder.embed_documents([a_str])[0]
    r = embedder.embed_documents([b_str])[0]
    return np.dot(a, r)/(np.linalg.norm(a)*np.linalg.norm(r))


if __name__ == '__main__':
    print(cosine_similarity("Anika is awesome", "Anika is sweet"))
    print(cosine_similarity("I work alone", "ISRO will launch the satellite"))
