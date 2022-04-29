from SerializerFactory.serializerYAML import SerializerYAML
from SerializerFactory.serializerJSON import SerializerJSON
from SerializerFactory.serializerTOML import SerializerTOML


serializers = {
    "json": SerializerJSON().create_serializer(),
    "yaml": SerializerYAML().create_serializer(),
    "toml": SerializerTOML().create_serializer()
}


class Factory:
    @staticmethod
    def create_serializer(extension: str):
        if extension in serializers:
            return serializers[extension]

        print("Incorrect extension")
