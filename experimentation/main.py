# %pip install --upgrade --quiet  llama-cpp-python

from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    model_path=r"C:\Users\George\PycharmProjects\llama-3.2-3b-instruct-q8_0.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    # callback_manager=callback_manager,
    # verbose=True,  # Verbose is required to pass to the callback manager
    verbose=False,
)

if __name__ == '__main__':
    question = "Question: Give me a JSON array with 3 popular female names."
    print(llm.invoke(question))
