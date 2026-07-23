import importlib

from ai.config import LLM_PRIORITY


# Generate response using available providers
def get_llm_response(prompt):

    for provider in LLM_PRIORITY:

        try:
            module = importlib.import_module(
                f"providers.{provider.strip()}"
            )

            llm = module.get_llm()

            print(f"Using {provider.capitalize()}")

            response = llm.invoke(prompt)

            return response.content

        except Exception as error:
            print(f"{provider.capitalize()} failed : {error}")

    raise Exception("No LLM provider is available.")


if __name__ == "__main__":

    response = get_llm_response("What is 2 + 2?")

    print(response)