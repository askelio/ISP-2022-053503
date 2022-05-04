from SerializerFactory.Serializers.serializerFormat import SerializerFormat
import toml


class SerializerToml(SerializerFormat):

    @staticmethod
    def dumps(obj):
        return toml.dumps(obj)

    @staticmethod
    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(SerializerToml.dumps(obj))

    @staticmethod
    def loads(obj):
        return toml.loads(obj)

    @staticmethod
    def load(file):
        with open(file, 'r') as f:
            result = f.read()
            return SerializerToml.loads(result)

