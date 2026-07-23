from langchain_chroma import Chroma
from ai.embeddings import get_embedding_model


embedding_model = get_embedding_model()

vectorstore = Chroma(
    persist_directory="vectorstore/chroma_db",
    embedding_function=embedding_model,
    collection_name="vigybag_faqs"
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


def retrieve_documents(query, top_k=3):
    documents = retriever.invoke(query)

    print("\n===== Retrieved Documents =====")
    for i, doc in enumerate(documents, 1):
        print(f"\nDocument {i}:")
        print(doc.page_content)
    print("===============================\n")

    return [doc.page_content for doc in documents]