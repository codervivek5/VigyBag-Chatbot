from ai.llm import get_llm_response


def rewrite_query(query):

    prompt = f"""
You rewrite customer questions into short FAQ search queries.

Rules:
- Keep the meaning same.
- Do not answer the question.
- Return only the rewritten search query.
- Keep it under 10 words.

Customer Question:
{query}

Search Query:
"""

    rewritten = get_llm_response(prompt)

    return rewritten.strip()


if __name__ == "__main__":

    print(rewrite_query("How do I exchange my product?"))