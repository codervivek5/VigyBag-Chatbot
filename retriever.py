# retriever.py
from langchain_chroma import Chroma

from embeddings import get_embedding_model
from ingest import COLLECTION_NAME, PERSIST_DIRECTORY


# Retrieve similar documents from ChromaDB
def retrieve_documents(query, top_k=3):
    vectorstore = Chroma(
        persist_directory=str(PERSIST_DIRECTORY),
        embedding_function=get_embedding_model(),
        collection_name=COLLECTION_NAME
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": top_k}
    )

    documents = retriever.invoke(query)

    return [document.page_content for document in documents]


if __name__ == "__main__":
    query = "How can I return my order?"

    documents = retrieve_documents(query)

    print("\nRetrieved Documents:\n")

    for document in documents:
        print(document)
        print("-" * 50)
