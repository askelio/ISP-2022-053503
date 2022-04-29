from abc import ABC, abstractmethod


class SerializerFormat(ABC):

    @staticmethod
    @abstractmethod
    def dump():
        pass

    @staticmethod
    @abstractmethod
    def dumps():
        pass

    @staticmethod
    @abstractmethod
    def load():
        pass

    @staticmethod
    @abstractmethod
    def loads():
        pass
