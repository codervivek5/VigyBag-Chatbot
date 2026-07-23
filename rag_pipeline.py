import time
import logging
from retriever import retrieve_documents
from prompt import build_prompt
from llm import get_llm_response
from memory import get_chat_history_string, save_chat_message

# Terminal logging config (Bina file write ke console log karega)
logging.basicConfig(
    level=logging.INFO,
    # format="%(asctime)s - [%(levelname)s] - %(message)s",
    # datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def generate_answer(question: str, session_id: str = "default_user") -> str:
    start_time = time.time()

    logger.info(f"Received question: '{question}'")

    # 1. Retrieve Context
    documents = retrieve_documents(question)
    retrieved_context = "\n\n".join(documents)
    logger.info(f"Retrieved {len(documents)} context chunks from ChromaDB")

    # 2. Get Memory & Prompt
    chat_history_text = get_chat_history_string(session_id)
    prompt = build_prompt()

    formatted_prompt = prompt.format(
        chat_history=chat_history_text if chat_history_text else "No previous conversation.",
        context=retrieved_context,
        question=question
    )

    # 3. LLM Response Generation
    logger.info("Sending request to LLM...")
    answer = get_llm_response(formatted_prompt)

    # 4. Save History
    save_chat_message(session_id, question, answer)

    elapsed_time = round(time.time() - start_time, 2)
    logger.info(f"Response generated in {elapsed_time}s")

    return answer