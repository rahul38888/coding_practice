import os
from uuid import uuid4

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from pymongo.server_api import ServerApi

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1536)

uri = os.getenv("MONGO_CLUSTER_URI")
client = MongoClient(uri, server_api=ServerApi('1'))

collection = client["vector_db"]["vector_collection"]


vector_store = MongoDBAtlasVectorSearch(
    collection=collection, embedding=embedding,
    index_name="vector_search_index", relevance_score_fn="cosine")


def put_vector_data():
    document_1 = Document(
        page_content="I had chocalate chip pancakes and scrambled eggs for "
                     "breakfast this morning.",
        metadata={"source": "tweet"},
    )

    document_2 = Document(
        page_content="The weather forecast for tomorrow is cloudy and "
                     "overcast, with a high of 62 degrees.",
        metadata={"source": "news"},
    )

    document_3 = Document(
        page_content="Building an exciting new project with LangChain - come "
                     "check it out!",
        metadata={"source": "tweet"},
    )

    document_4 = Document(
        page_content="Robbers broke into the city bank and stole $1 million "
                     "in cash.",
        metadata={"source": "news"},
    )

    document_5 = Document(
        page_content="Wow! That was an amazing movie. I can't wait to see "
                     "it again.",
        metadata={"source": "tweet"},
    )

    document_6 = Document(
        page_content="Is the new iPhone worth the price? Read this review "
                     "to find out.",
        metadata={"source": "website"},
    )

    document_7 = Document(
        page_content="The top 10 soccer players in the world right now.",
        metadata={"source": "website"},
    )

    document_8 = Document(
        page_content="LangGraph is the best framework for building stateful, "
                     "agentic applications!",
        metadata={"source": "tweet"},
    )

    document_9 = Document(
        page_content="The stock market is down 500 points today due to "
                     "fears of a recession.",
        metadata={"source": "news"},
    )

    document_10 = Document(
        page_content="I have a bad feeling I am going to get deleted :(",
        metadata={"source": "tweet"},
    )

    documents = [
        document_1,
        document_2,
        document_3,
        document_4,
        document_5,
        document_6,
        document_7,
        document_8,
        document_9,
        document_10,
    ]
    uuids = [str(uuid4()) for _ in range(len(documents))]

    vector_store.add_documents(documents=documents, ids=uuids)


def search(query: str, k: int = 4):
    return vector_store.similarity_search(query, k=k)


if __name__ == '__main__':
    # put_vector_data()

    results = search("LangChain provides abstractions to make working with LLMs easy")
    for r in results:
        print(r.page_content, r.metadata)
