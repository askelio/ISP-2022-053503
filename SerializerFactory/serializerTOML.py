from SerializerFactory.Serializers.serializerToml import SerializerToml
from SerializerFactory.serializerСreatorFormat import SerializerCreatorFormat


class SerializerTOML(SerializerCreatorFormat):

    def create_serializer(self) -> SerializerToml:
        return SerializerToml()
