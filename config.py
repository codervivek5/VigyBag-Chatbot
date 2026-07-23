# config.py

import os
from dotenv import load_dotenv

load_dotenv()


# Providers in priority order
LLM_PRIORITY = os.getenv(
    "LLM_PRIORITY",
    "gemini"
).split(",")


# Models
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)


# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    print("Priority :", LLM_PRIORITY)
    print("Gemini   :", GEMINI_MODEL)
    print("Groq     :", GROQ_MODEL)
    print("OpenAI   :", OPENAI_MODEL)