from retriever import retrieve_documents
from prompt import build_prompt
from llm import get_llm_response


# Generate answer using RAG pipeline
def generate_answer(question):

    documents = retrieve_documents(question)

    context = "\n\n".join(documents)

    prompt = build_prompt()

    formatted_prompt = prompt.format(
        context=context,
        question=question
    )

    answer = get_llm_response(formatted_prompt)

    return answer


if __name__ == "__main__":

    question = "What is VigyBag?"

    answer = generate_answer(question)

    print("\nAnswer:\n")
    print(answer)