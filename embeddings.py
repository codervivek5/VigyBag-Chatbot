import os

from langchain_huggingface import HuggingFaceEmbeddings

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"


# Load embedding model
def get_embedding_model():
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return model


if __name__ == "__main__":
    model = get_embedding_model()

    embedding = model.embed_query("What is VigyBag?")

    print(f"Embedding dimension: {len(embedding)}")
    print(embedding[:5])