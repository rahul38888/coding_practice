import json
import os
import math
import string

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone


embedder = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=3072)

pc = Pinecone(api_key=os.getenv("pinecone_api_key"))
index = pc.Index("me-n-myself")

embedd_batch_size = 1000
chunk_size = 600

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

custom_stop_words = {"a", "an", "and", "are", "as", "at", "be", "because",
                     "been", "but", "by", "for", "from", "has", "had", "have",
                     "he", "her", "hers", "him", "his", "if", "in", "is", "it",
                     "its", "itself", "me", "my", "myself", "no", "nor", "not",
                     "of", "on", "or", "our", "ours", "ourselves", "she", "so",
                     "such", "than", "that", "the", "their", "theirs", "them",
                     "themselves", "then", "there", "these", "they", "this",
                     "those", "to", "too", "very", "was", "we", "were", "what",
                     "when", "where", "which", "while", "who", "whom", "why",
                     "with", "you", "your", "yours", "yourself", "yourselves"
                     }

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()


preprocess_threshold = 601


def preprocess_text(text: str) -> str:
    if len(text) < preprocess_threshold:
        return text

    word_tokens = word_tokenize(text)
    filtered_tokens = [w for w in word_tokens
                       if w.lower() not in custom_stop_words and
                       w.lower() not in string.punctuation]
    filtered_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    return " ".join(filtered_tokens)


def text_to_vec(vec_json_list: list[dict], common_metadata: dict,
                get_concise_text=False) -> list[dict]:
    vec_json_list = vec_json_list.copy()
    n = len(vec_json_list)
    print(f"Generating embedding for texts, embedd_batch_size = "
          f"{embedd_batch_size} ...")
    for i in range(math.ceil(n / embedd_batch_size)):
        batch = vec_json_list[i*embedd_batch_size: (i + 1)*embedd_batch_size]
        texts = list(map(lambda x: x['values'], batch))
        concise_texts = list(map(preprocess_text, texts))
        vecs = embedder.embed_documents(texts, chunk_size=chunk_size)

        for j in range(len(vecs)):
            doc_i = j + i * embedd_batch_size
            vec_json_list[doc_i]['id'] = str(hash(texts[j]))
            vec_json_list[doc_i]['values'] = vecs[j]
            vec_json_list[doc_i]['metadata'] = (
                    vec_json_list[doc_i]['metadata'] | common_metadata)
            vec_json_list[doc_i]['metadata']['text'] = (
                concise_texts)[j] if get_concise_text else texts[j]

    return vec_json_list


def update_all_data(file_name, save_concise_text=False):
    with open(file_name, "r") as d:
        print(f"Loading json file {file_name}")
        data = json.load(d, strict=False)

    for namespace_data in data:
        namespace = namespace_data['namespace']
        common_metadata = namespace_data['common_metadata']
        print(f"Found data for namespace = {namespace}, common_metadata = "
              f"{common_metadata}, count = {len(namespace_data['data'])}")
        vec_json_list = text_to_vec(namespace_data['data'], common_metadata,
                                    get_concise_text=save_concise_text)

        print(f"Updating vector store for namespace = {namespace} "
              f"and save_concise_text = {save_concise_text}...")
        index.upsert(vectors=vec_json_list, namespace=namespace)


if __name__ == '__main__':
    update_all_data("D:/Desktop/me_in_text.json")

