# loader.py
import json
from pathlib import Path


FAQ_FILE = Path(__file__).resolve().parent / "data" / "faq.json"

# Load FAQ data from faq.json
def load_documents():
    with FAQ_FILE.open("r", encoding="utf-8") as file:
        records = json.load(file)

    documents = []

    for record in records:
        documents.append(
            {
                "question": record["Question"],
                "answer": record["Answer"],
                "category": record["Category"],
                "text": f"Question: {record['Question']}\nAnswer: {record['Answer']}"
            }
        )

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print(f"Loaded {len(docs)} FAQs")
    print("\nFirst FAQ:")
    print(docs[0])
