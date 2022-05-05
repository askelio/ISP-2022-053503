from abc import ABC, abstractmethod


class SerializerCreatorFormat(ABC):

    @abstractmethod
    def create_serializer(self):
        pass
