from serializer_utility.SerializerFactory.Serializers.serializerJson import SerializerJson
from serializer_utility.SerializerFactory.serializerСreatorFormat import SerializerCreatorFormat


class SerializerJSON(SerializerCreatorFormat):

    def create_serializer(self) -> SerializerJson:
        return SerializerJson()
