from langchain_google_genai import ChatGoogleGenerativeAI

from ai.config import GEMINI_API_KEY, GEMINI_MODEL


# Create Gemini LLM
def get_llm():
    llm = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=GEMINI_API_KEY,
        temperature=0.2,
        max_output_tokens=150
    )

    return llm


if __name__ == "__main__":
    llm = get_llm()

    response = llm.invoke("What is 2 + 2?")

    print(response.content)