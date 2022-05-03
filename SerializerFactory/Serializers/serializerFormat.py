from abc import ABC, abstractmethod


class SerializerFormat(ABC):

    @staticmethod
    @abstractmethod
    def dump(obj, file):
        pass

    @staticmethod
    @abstractmethod
    def dumps(obj) -> str:
        pass

    @staticmethod
    @abstractmethod
    def load(obj: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def loads(file: str) -> str:
        pass
