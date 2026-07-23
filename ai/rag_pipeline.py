from ai.retriever import retrieve_documents
from ai.prompt import build_prompt
from ai.llm import get_llm_response
from ai.query_rewriter import rewrite_query


# Generate answer using RAG pipeline
def generate_answer(question):

    # Rewrite user query for better retrieval
    search_query = rewrite_query(question)

    print(f"\nSearch Query: {search_query}")

    # Retrieve documents using rewritten query
    documents = retrieve_documents(search_query)

    context = "\n\n".join(documents)

    prompt = build_prompt()

    formatted_prompt = prompt.format(
        context=context,
        question=question
    )
    print("\n========== FINAL PROMPT ==========\n")
    print(formatted_prompt)
    print("\n==================================\n")

    answer = get_llm_response(formatted_prompt)

    return answer


if __name__ == "__main__":

    question = "What is VigyBag?"

    answer = generate_answer(question)

    print("\nAnswer:\n")
    print(answer)