from rag_pipeline import generate_answer


# Run chatbot
def start_chat():

    print("VigyBag Chatbot Started")
    print("Type 'exit' to quit\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("Bot: Goodbye!")
            break

        answer = generate_answer(question)

        print(f"\nBot: {answer}\n")


if __name__ == "__main__":
    start_chat()