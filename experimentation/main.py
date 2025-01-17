# %pip install --upgrade --quiet  llama-cpp-python

from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from sqlmodel import SQLModel

from abstract.manager.manager import SQLModelBound
from database.database import Database

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
    import model.comprehensive
    from sqlalchemy.schema import CreateTable

    db = Database()
    sql_statements = []
    tables = SQLModel.metadata.tables.values()
    for table in tables:
        sql = str(CreateTable(table).compile(db.get_engine())).replace("\n", "").replace("\t", "")
        sql_statements.append(sql)
    statement = ';\n'.join(sql_statements)
    print(statement)

    # question = "Question: Give me a JSON array with 3 popular female names."
    # print(llm.invoke(question))
