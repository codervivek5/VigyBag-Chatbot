from langchain_groq import ChatGroq

from config import GROQ_API_KEY, GROQ_MODEL


# Create Groq LLM
def get_llm():
    llm = ChatGroq(
        model=GROQ_MODEL,
        groq_api_key=GROQ_API_KEY,
        temperature=0.2,
        max_tokens=150
    )

    return llm


if __name__ == "__main__":
    print("Model :", GROQ_MODEL)
    print("Key Loaded :", bool(GROQ_API_KEY))

    if GROQ_API_KEY:
        llm = get_llm()

        response = llm.invoke("What is 2 + 2?")

        print(response.content)