# chunking.py
from langchain_text_splitters import RecursiveCharacterTextSplitter



# Split documents into smaller chunks
def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []

    for document in documents:
        split_text = splitter.split_text(document["text"])

        for text in split_text:
            chunks.append(
                {
                    "question": document["question"],
                    "answer": document["answer"],
                    "category": document["category"],
                    "text": text
                }
            )

    return chunks


if __name__ == "__main__":
    sample_documents = [
        {
            "question": "What is VigyBag?",
            "answer": "VigyBag is an eco-friendly marketplace.",
            "category": "General Information",
            "text": "Question: What is VigyBag?\nAnswer: VigyBag is an eco-friendly marketplace."
        }
    ]

    chunks = chunk_documents(sample_documents)

    print(f"Created {len(chunks)} chunks")
    print(chunks[0])