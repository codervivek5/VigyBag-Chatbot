import json
from pathlib import Path

from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

MEMORY_DIR = Path(__file__).resolve().parent / "data" / "chat_history"

MEMORY_DIR.mkdir(parents=True, exist_ok=True)


# Get or create chat history for a given session ID
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    file_path = MEMORY_DIR / f"{session_id}.json"

    if not file_path.exists() or not file_path.read_text(encoding="utf-8").strip():
        file_path.write_text("[]", encoding="utf-8")
    else:
        try:
            stored_messages = json.loads(file_path.read_text(encoding="utf-8"))
            if not isinstance(stored_messages, list):
                raise ValueError("Chat history must be a JSON list")
        except (json.JSONDecodeError, ValueError):
            file_path.write_text("[]", encoding="utf-8")

    return FileChatMessageHistory(str(file_path))


# Function to fetch recent chat context as a string
def get_chat_history_string(session_id: str, limit: int = 6) -> str:
    history = get_session_history(session_id)
    messages = history.messages[-limit:] if history.messages else []

    formatted_history = []
    for msg in messages:
        role = "User" if msg.type == "human" else "Vigy Help"
        formatted_history.append(f"{role}: {msg.content}")

    return "\n".join(formatted_history)


# IDE reference error fix: Add save_chat_message function
def save_chat_message(session_id: str, question: str, answer: str):
    history = get_session_history(session_id)
    history.add_user_message(question)
    history.add_ai_message(answer)
