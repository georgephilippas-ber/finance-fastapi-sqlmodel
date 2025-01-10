from abc import ABC


class Client(ABC):
    _base_url: str

    def __init__(self, base_url: str):
        self._base_url = base_url
