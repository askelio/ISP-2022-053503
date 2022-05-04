import re
from SerializerFactory.Serializers.serializerFormat import SerializerFormat
import yaml


class SerializerYaml(SerializerFormat):

    @staticmethod
    def dumps(obj):
        return yaml.dump(obj)

    @staticmethod
    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(SerializerYaml.dumps(obj))

    @staticmethod
    def load(file):
        with open(file, 'r') as f:
            result = f.read()
            return SerializerYaml.loads(result)

    @staticmethod
    def loads(obj):
        return yaml.load(obj)
