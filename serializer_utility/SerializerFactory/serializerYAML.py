from serializer_utility.SerializerFactory.serializerСreatorFormat import SerializerCreatorFormat
from serializer_utility.SerializerFactory.Serializers.serializerYaml import SerializerYaml


class SerializerYAML(SerializerCreatorFormat):

    def create_serializer(self) -> SerializerYaml:
        return SerializerYaml()
