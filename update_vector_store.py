"""Synchronize data/faq.json with the existing ChromaDB collection."""

from langchain_chroma import Chroma

from embeddings import get_embedding_model
from ingest import (
    COLLECTION_NAME,
    PERSIST_DIRECTORY,
    add_vector_records,
    prepare_vector_records,
)


def update_vector_store():
    texts, metadatas, ids = prepare_vector_records()

    vectorstore = Chroma(
        persist_directory=str(PERSIST_DIRECTORY),
        embedding_function=get_embedding_model(),
        collection_name=COLLECTION_NAME,
    )

    stored = vectorstore.get(include=["metadatas"])
    stored_hashes = {
        record_id: metadata.get("content_hash")
        for record_id, metadata in zip(
            stored.get("ids", []),
            stored.get("metadatas", []),
        )
    }

    records_to_update = [
        index
        for index, record_id in enumerate(ids)
        if stored_hashes.get(record_id) != metadatas[index]["content_hash"]
    ]

    if records_to_update:
        add_vector_records(
            vectorstore,
            texts=[texts[index] for index in records_to_update],
            metadatas=[metadatas[index] for index in records_to_update],
            ids=[ids[index] for index in records_to_update],
        )

    desired_ids = set(ids)
    stale_ids = [
        record_id for record_id in stored_hashes if record_id not in desired_ids
    ]
    if stale_ids:
        vectorstore.delete(ids=stale_ids)

    return vectorstore, len(records_to_update), len(stale_ids)


if __name__ == "__main__":
    store, updated_count, deleted_count = update_vector_store()

    print("Vector store updated successfully")
    print(f"Added/updated chunks: {updated_count}")
    print(f"Deleted stale chunks: {deleted_count}")
    print(f"Total documents: {store._collection.count()}")
