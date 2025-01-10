import os
import string

from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

embedder = OpenAIEmbeddings(model="text-embedding-3-large")

pc = Pinecone(api_key=os.getenv("pinecone_api_key"))
index = pc.Index("me-n-myself")
vector_store = PineconeVectorStore(index=index, embedding=embedder,
                                   namespace='career', )

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


def preprocess_text(text: str) -> str:
    word_tokens = word_tokenize(text)
    filtered_tokens = [w for w in word_tokens
                       if w.lower() not in custom_stop_words and
                       w.lower() not in string.punctuation]
    filtered_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]

    return " ".join(filtered_tokens)


if __name__ == '__main__':
    text = "List all the projects I have worked on?"
    processed_text = preprocess_text(text)
    print(f"Query: {text}\nProcessed text: {processed_text}")
    res = vector_store.similarity_search_with_score(text, k=5)
    print("\n")

    print("Responses\n============")
    for r, s in res:
        print(f"SIM: {s:3f}\n{r.page_content}\n{r.metadata}")
        print("------------")
