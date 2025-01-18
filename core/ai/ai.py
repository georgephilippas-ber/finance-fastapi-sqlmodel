from os.path import join
from typing import Tuple

from langchain_community.llms.llamacpp import LlamaCpp
from time import time

from core.utilities.root import project_root

MODEL_PATH_AND_FILENAME = join(project_root(), "core", "ai", "models", "granite-3.1-8b-instruct-Q4_K_M.gguf")


class LargeLanguageModel:
    _model_path_and_filename: str
    _instance: LlamaCpp

    def __init__(self, model_path_and_filename: str = MODEL_PATH_AND_FILENAME):
        self._model_path_and_filename = model_path_and_filename

        self._instance = LlamaCpp(
            model_path=self._model_path_and_filename,
            temperature=0.75,
            max_tokens=2000,
            n_ctx=2048,
            top_p=1,
            verbose=False,
        )

    def query(self, query_: str) -> Tuple[str, float]:
        beginning_: float = time()
        response_ = self._instance.invoke(query_)
        end_: float = time()

        return response_, end_ - beginning_


if __name__ == '__main__':
    llm = LargeLanguageModel()

    r, p = llm.query(
        "Just say hello in 9 ways of increasing politeness. Just a JSON array of strings as a response with no special characters or escape sequences.")

    print(r.replace("\n", ""))
