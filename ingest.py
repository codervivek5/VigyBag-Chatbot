# ingest.py
import hashlib
import time
from pathlib import Path

from langchain_chroma import Chroma

from loader import load_documents
from chunking import chunk_documents
from embeddings import get_embedding_model


PROJECT_ROOT = Path(__file__).resolve().parent
PERSIST_DIRECTORY = PROJECT_ROOT / "vectorstore" / "chroma_db"
COLLECTION_NAME = "vigybag_faqs"
EMBEDDING_BATCH_SIZE = 90
EMBEDDING_BATCH_DELAY_SECONDS = 60


def prepare_vector_records():
    documents = load_documents()
    chunks = chunk_documents(documents)

    texts = []
    metadatas = []
    ids = []

    question_chunk_numbers = {}

    for chunk in chunks:
        question = chunk["question"].strip()
        question_key = question.casefold()
        chunk_number = question_chunk_numbers.get(question_key, 0)
        question_chunk_numbers[question_key] = chunk_number + 1

        record_id = hashlib.sha256(
            f"{question_key}:{chunk_number}".encode("utf-8")
        ).hexdigest()
        content_hash = hashlib.sha256(
            chunk["text"].encode("utf-8")
        ).hexdigest()

        texts.append(chunk["text"])
        ids.append(record_id)
        metadatas.append(
            {
                "question": question,
                "category": chunk["category"],
                "content_hash": content_hash,
            }
        )

    return texts, metadatas, ids


def add_vector_records(vectorstore, texts, metadatas, ids):
    for batch_start in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        if batch_start:
            print(
                "Waiting 60 seconds for the Gemini embedding quota "
                "before the next batch..."
            )
            time.sleep(EMBEDDING_BATCH_DELAY_SECONDS)

        batch_end = batch_start + EMBEDDING_BATCH_SIZE
        vectorstore.add_texts(
            texts=texts[batch_start:batch_end],
            metadatas=metadatas[batch_start:batch_end],
            ids=ids[batch_start:batch_end],
        )


# Create and store embeddings in ChromaDB
def create_vector_store(reset=True):
    texts, metadatas, ids = prepare_vector_records()
    embedding_model = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=str(PERSIST_DIRECTORY),
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )

    if reset:
        vectorstore.delete_collection()
        vectorstore = Chroma(
            persist_directory=str(PERSIST_DIRECTORY),
            embedding_function=embedding_model,
            collection_name=COLLECTION_NAME,
        )

    if texts:
        add_vector_records(vectorstore, texts, metadatas, ids)

    return vectorstore


if __name__ == "__main__":
    vectorstore = create_vector_store()

    print("Vector store created successfully")
    print(f"Total documents: {vectorstore._collection.count()}")
