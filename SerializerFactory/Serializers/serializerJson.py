from SerializerFactory.Serializers.serializerFormat import SerializerFormat


class SerializerJson(SerializerFormat):

    @staticmethod
    def dumps(obj):
        # defining the returning result of object serialization to json
        result = str()

        obj_type = type(obj)

        if obj_type is dict:
            if len(obj) == 0:
                return "{}"

            result += "{"

            for key, value in obj.items():

                result += SerializerJson.dumps(key)
                result += ": "
                result += SerializerJson.dumps(value)
                result += ", "

            return result[0:-2]+ "}"

        elif obj_type is list or obj_type is tuple:
            if len(obj) == 0:
                return "[]"

            result += "["

            for value in obj:
                result += SerializerJson.dumps(value)
                result += ", "

            return result[0:-2] + "]"

        elif obj_type is str:
            return f"\"{obj}\""

        elif obj_type is int or obj_type is float:
            return str(obj)

        elif obj_type is bool:
            if obj:
                return "true"
            return "false"

        elif obj is None:
            return "null"
        else:
            return result


    @staticmethod
    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(SerializerJson.dumps(obj))


    @staticmethod
    def loads():
        pass

    @staticmethod
    def load(file):
        with open(file, 'r') as f:
            result = f.read()
            return SerializerJson.loads(result)
