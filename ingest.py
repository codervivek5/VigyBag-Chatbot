from langchain_chroma import Chroma

from loader import load_documents
from chunking import chunk_documents
from embeddings import get_embedding_model


# Create and store embeddings in ChromaDB
def create_vector_store():
    documents = load_documents()
    chunks = chunk_documents(documents)

    texts = []
    metadatas = []

    for chunk in chunks:
        texts.append(chunk["text"])

        metadatas.append(
            {
                "question": chunk["question"],
                "category": chunk["category"]
            }
        )

    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=get_embedding_model(),
        metadatas=metadatas,
        persist_directory="vectorstore/chroma_db",
        collection_name="vigybag_faqs"
    )

    return vectorstore


if __name__ == "__main__":
    vectorstore = create_vector_store()

    print("Vector store created successfully")
    print(f"Total documents: {vectorstore._collection.count()}")