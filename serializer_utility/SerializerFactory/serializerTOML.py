from serializer_utility.SerializerFactory.Serializers.serializerToml import SerializerToml
from serializer_utility.SerializerFactory.serializerСreatorFormat import SerializerCreatorFormat


class SerializerTOML(SerializerCreatorFormat):

    def create_serializer(self) -> SerializerToml:
        return SerializerToml()
