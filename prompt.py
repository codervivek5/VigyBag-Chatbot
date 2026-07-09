from langchain_core.prompts import PromptTemplate


# Create prompt from retrieved documents
def build_prompt():
    prompt = PromptTemplate.from_template(
        """
You are a customer support assistant for VigyBag.

Answer only using the provided context.

Keep the answer complete and concise.

If the answer is not present in the context, reply exactly:

"I could not find that information in the available data."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    return prompt


if __name__ == "__main__":

    prompt = build_prompt()

    formatted_prompt = prompt.format(
        context="Question: What is VigyBag?\nAnswer: VigyBag is an eco-friendly marketplace.",
        question="What is VigyBag?"
    )

    print(formatted_prompt)