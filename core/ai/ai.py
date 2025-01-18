from os.path import join
from typing import Tuple

from langchain_community.llms.llamacpp import LlamaCpp
from time import time
from os import sep
from core.utilities.root import project_root
from configuration.environment import EnvironmentType, ENVIRONMENT

if ENVIRONMENT == EnvironmentType.PRODUCTION:
    MODEL_PATH_AND_FILENAME: str = join(project_root(), "core", "ai", "models", "granite-3.1-8b-instruct-Q4_K_M.gguf")
    N_CTX: int = 131072
else:
    MODEL_PATH_AND_FILENAME: str = join(project_root(), "core", "ai", "models", "qwen2-0_5b-instruct-q4_0.gguf")
    N_CTX: int = 32768


class LargeLanguageModel:
    _model_path_and_filename: str
    _instance: LlamaCpp

    def __init__(self, model_path_and_filename: str = MODEL_PATH_AND_FILENAME, *, n_ctx: int = N_CTX,
                 max_tokens: int = 2048):
        self._model_path_and_filename = model_path_and_filename
        print("LOADING LargeLanguageModel", self._model_path_and_filename.split(sep)[-1], end='')
        beginning_ = time()
        self._instance = LlamaCpp(
            model_path=self._model_path_and_filename,
            temperature=0.75,
            max_tokens=max_tokens,
            n_ctx=n_ctx,
            top_p=1,
            verbose=False,
            n_batch=32,
        )
        end_ = time()
        print(f" - DONE - {end_ - beginning_:.2f}s")

    def query(self, query_: str) -> Tuple[str, float]:
        beginning_: float = time()
        response_ = self._instance.invoke(query_)
        end_: float = time()

        return response_, end_ - beginning_


if __name__ == '__main__':
    pass
