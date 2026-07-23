from rag_pipeline import generate_answer


# Run chatbot
def start_chat():
    print("VigyBag Chatbot Started")
    print("Type 'exit' to quit\n")

    # Session ID (Multiple users/chats can have unique IDs)
    session_id = "user_session_1"

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            print("Bot: Goodbye!")
            break

        answer = generate_answer(question, session_id=session_id)

        print(f"\nBot: {answer}\n")


if __name__ == "__main__":
    start_chat()