# embeddings.py
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GEMINI_API_KEY
from dotenv import load_dotenv

load_dotenv()


# Load embedding model
def get_embedding_model():
    model = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=GEMINI_API_KEY
    )

    return model


if __name__ == "__main__":
    model = get_embedding_model()

    embedding = model.embed_query("What is VigyBag?")

    print(f"Embedding dimension: {len(embedding)}")
    print(embedding[:5])