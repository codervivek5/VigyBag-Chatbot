from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

from config import GEMINI_API_KEY, GEMINI_MODEL


# Create Gemini LLM
def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=GEMINI_API_KEY,
        temperature=0.2,
    )


# Create local Ollama LLM
def get_ollama_llm():
    return ChatOllama(
        model="qwen2.5-coder:7b",
        temperature=0.2,
        base_url="http://localhost:11434"
    )


# Gemini primary + Ollama fallback
def get_llm():
    gemini_llm = get_gemini_llm()
    ollama_llm = get_ollama_llm()

    # Gemini request fail hone par Ollama automatically use hoga
    llm = gemini_llm.with_fallbacks(
        [ollama_llm],
        exceptions_to_handle=(Exception,)
    )

    return llm


if __name__ == "__main__":
    llm = get_llm()

    try:
        response = llm.invoke("What is 2 + 2?")

        print("Response:")
        print(response.content)

    except Exception as error:
        print("Gemini aur Ollama dono se response nahi mila.")
        print(f"Error: {error}")