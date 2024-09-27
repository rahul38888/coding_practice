import os

from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore, Pinecone

embedder = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=3072)

vector_store = PineconeVectorStore(index="tests-vector-index", embedding=embedder)


pc = Pinecone(api_key=os.getenv("pinecone_api_key"))

pc.simi