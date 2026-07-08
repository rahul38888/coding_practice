# openai and cohere can be used

from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()


if __name__ == '__main__':
    embeddings = embedding_model.embed_documents(
        [
            "Hi there!",
            "Oh, hello!",
            "What's your name?",
            "My friends call me World",
            "Hello World!"
        ]
    )
    print(len(embeddings), len(embeddings[0]), embeddings[0][:5])

    embedded_query = embedding_model.embed_query("What was the name mentioned in the conversation?")
    print(embedded_query[:5])

