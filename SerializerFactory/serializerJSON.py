from SerializerFactory.Serializers.serializerJson import SerializerJson
from SerializerFactory.serializerСreatorFormat import SerializerCreatorFormat


class SerializerJSON(SerializerCreatorFormat):

    def create_serializer(self) -> SerializerJson:
        return SerializerJson()
