from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma


def load_file_persistent(file_name: str) -> Chroma:
    raw_doc = TextLoader(file_name).load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(raw_doc)

    return Chroma.from_documents(docs, OpenAIEmbeddings(), persist_directory="vector_store_data/")


def get_db_connection() -> Chroma:
    return Chroma(persist_directory="vector_store_data/")


db = load_file_persistent("quant_computing.txt")

if __name__ == '__main__':
    query = "What is Quantum computing?"
    print("String query")
    query_results = db.similarity_search(query, k=2)
    print(query_results[0].page_content)
    print("------------------------------------------")

    print("Vector query")
    embedded_query = OpenAIEmbeddings().embed_query(query)
    em_query_results = db.similarity_search_by_vector(embedded_query)
    print(em_query_results[0].page_content)
