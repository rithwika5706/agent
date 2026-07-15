from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


# Embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# Vector database
vectorstore = Chroma(
    collection_name="user_memory",
    embedding_function=embeddings,
    persist_directory="./memory_db"
)


def save_memory(text):
    """
    Store important information about user
    """

    vectorstore.add_texts(
        texts=[text]
    )


def search_memory(query):
    """
    Retrieve related memories
    """

    results = vectorstore.similarity_search(
        query,
        k=3
    )

    memories = []

    for r in results:
        memories.append(r.page_content)

    return memories