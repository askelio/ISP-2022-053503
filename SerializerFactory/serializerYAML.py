from SerializerFactory.serializerСreatorFormat import SerializerCreatorFormat
from SerializerFactory.Serializers.serializerYaml import SerializerYaml


class SerializerYAML(SerializerCreatorFormat):

    def create_serializer(self) -> SerializerYaml:
        return SerializerYaml()
