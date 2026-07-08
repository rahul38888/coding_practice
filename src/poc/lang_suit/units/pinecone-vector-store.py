import os
import uuid

from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone

pc = Pinecone(api_key=os.getenv("pinecone_api_key"))

embedder = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=3072)

sentences = [
    {
        "text": "Anika is awesome",
        "metadata": {"entity": "person", "value": "Anika"}
    },
    {
        "text": "Anika is awesome",
        "metadata": {"entity": "person", "value": "Anika"}
    },
    {
        "text": "Anika has been nice to people",
        "metadata": {"entity": "person", "value": "Anika"}
    },
    {
        "text": "Rahul like to work on AI bots",
        "metadata": {"entity": "person", "value": "Rahul"}
    },
    {
        "text": "ISRO will launch the satellite",
        "metadata": {"entity": "org", "value": "ISRO"}
    }
]


index = pc.Index("tests-vector-index")


def update_data():
    sts = sentences.copy()
    for st in sts:
        st["id"] = str(uuid.uuid4())
        st["values"] = embedder.embed_documents([st["text"]])[0]
        del st["text"]

    index.upsert(vectors=sts, namespace="test-ns")


if __name__ == '__main__':
    # update_data()
    query = "How is Rahul?"
    q_vec = embedder.embed_query(query)
    response = index.query(namespace="test-ns", vector= q_vec, top_k=3,
                           include_values=True, include_metadata=True,
                           filter={"entity": {"$eq": "person"}})

    print(response)

