import re
from SerializerFactory.Serializers.serializerFormat import SerializerFormat

FLOAT_REGEX = "-?[\d]+\.[\d]+"
INT_REGEX = "^-?[\d]+$"


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
                if type(key) == float or type(key) == int:
                    result += "\""
                    result += SerializerJson.dumps(key)
                    result += "\""
                else:
                    result += SerializerJson.dumps(key)
                result += ": "
                result += SerializerJson.dumps(value)
                result += ", "

            return result[0:-2] + "}"

        elif obj_type is list or obj_type is tuple:
            if len(obj) == 0:
                return "[]"

            result += "["

            for value in obj:
                result += SerializerJson.dumps(value)
                result += ", "

            return result[0:-2] + "]"

        elif obj_type is str:
            if len(obj) == 0:
                return ""
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
    def loads(lc_obj):
        if len(lc_obj) == 0:
            return ""
        if (": " and "{" and "[" and "]" and "}") not in lc_obj:
            if lc_obj[0] == "\"" and lc_obj[-1] == "\"":
                return lc_obj[1:-1]
            elif lc_obj == "true":
                return True
            elif lc_obj == "false":
                return False
            elif lc_obj == "null":
                return None


        def loads_obj(str_obj):
            obj = dict()
            if str_obj[0] == "{" or str_obj[0] == "[":
                str_obj = str_obj[1:len(str_obj) - 1]
            brackets = 0
            braces = 0
            quotes = 0
            is_key = True
            definition = ""
            key = ""
            i = 0

            while i < len(str_obj):
                if str_obj[i] == ':' and is_key:
                    is_key = False
                elif str_obj[i] == '[':
                    brackets += 1
                    temp_i = i + 1
                    while brackets:
                        if str_obj[temp_i] == '[':
                            brackets += 1
                        elif str_obj[temp_i] == ']':
                            brackets -= 1
                        temp_i += 1
                        if temp_i > len(str_obj):
                            raise ValueError()
                    obj[key] = load_arr(str_obj[i:temp_i])
                    key = ""
                    i = temp_i + 1
                    is_key = True
                elif str_obj[i] == '{':
                    braces += 1
                    temp_i = i + 1
                    while braces:
                        if str_obj[temp_i] == '{':
                            braces += 1
                        elif str_obj[temp_i] == '}':
                            braces -= 1
                        temp_i += 1
                        if temp_i > len(str_obj):
                            raise ValueError()
                    obj[key] = loads_obj(str_obj[i:temp_i])
                    key = ""
                    i = temp_i + 1
                    is_key = True
                elif str_obj[i] == '\"':
                    temp_i = i + 1
                    quotes += 1
                    while quotes:
                        if str_obj[temp_i] == '\"':
                            quotes = 0
                        temp_i += 1
                        if temp_i > len(str_obj):
                            raise ValueError()
                    if is_key:
                        key = str_obj[(i + 1):(temp_i - 1)]
                    else:
                        obj[key] = str_obj[(i + 1):(temp_i - 1)]
                        key = ""
                        is_key = True
                        temp_i += 2
                    i = temp_i - 1
                elif str_obj[i] == ' ' and not is_key:
                    i += 1
                    continue
                elif str_obj[i] == ',' and not is_key:
                    if definition == 'true':
                        obj[key] = True
                    elif definition == 'false':
                        obj[key] = False
                    elif definition == 'null':
                        obj[key] = None
                    elif re.fullmatch(FLOAT_REGEX, definition):
                        obj[key] = float(definition)
                    elif re.fullmatch(INT_REGEX, definition):
                        obj[key] = int(definition)
                    else:
                        raise ValueError()
                    definition = ""
                    key = ""
                    is_key = True
                    i += 1
                else:
                    if is_key:
                        raise KeyError()
                    else:
                        definition += str_obj[i]
                i += 1
            if key != "":
                if definition == 'true':
                    obj[key] = True
                elif definition == 'false':
                    obj[key] = False
                elif definition == 'null':
                    obj[key] = None
                elif re.fullmatch(FLOAT_REGEX, definition):
                    obj[key] = float(definition)
                elif re.fullmatch(INT_REGEX, definition):
                    obj[key] = int(definition)
            return obj

        def load_arr(str_obj):
            obj = list()
            str_obj = str_obj[1:len(str_obj) - 1]
            brackets = 0
            braces = 0
            quotes = 0
            definition = ""
            i = 0
            temp_i = 0
            while i < len(str_obj):
                if str_obj[i] != ' ':
                    if str_obj[i] == '[':
                        brackets += 1
                        temp_i = i + 1
                        while brackets:
                            if str_obj[temp_i] == '[':
                                brackets += 1
                            elif str_obj[temp_i] == ']':
                                brackets -= 1
                            temp_i += 1
                            if temp_i > len(str_obj):
                                raise ValueError()
                        obj.append(load_arr(str_obj[i:temp_i]))
                        i = temp_i
                    elif str_obj[i] == '{':
                        braces += 1
                        temp_i = i + 1
                        while braces:
                            if str_obj[temp_i] == '{':
                                braces += 1
                            elif str_obj[temp_i] == '}':
                                braces -= 1
                            temp_i += 1
                            if temp_i > len(str_obj):
                                raise ValueError()
                        obj.append(loads_obj(str_obj[i:temp_i]))
                        i = temp_i
                    elif str_obj[i] == '\"':
                        temp_i = i + 1
                        quotes += 1
                        while quotes:
                            if str_obj[temp_i] == '\"':
                                quotes = 0
                            temp_i += 1
                            if temp_i > len(str_obj):
                                raise ValueError()
                        obj.append(str_obj[i + 1:temp_i - 1])
                        i = temp_i
                    elif str_obj[i] == ',':
                        if re.fullmatch(FLOAT_REGEX, definition):
                            obj.append(float(definition))
                        elif definition == 'true':
                            obj.append(True)
                        elif definition == 'false':
                            obj.append(False)
                        elif definition == 'null':
                            obj.append(None)
                        elif re.fullmatch(INT_REGEX, definition):
                            obj.append(int(definition))
                        else:
                            raise ValueError()
                        definition = ""
                    else:
                        definition += str_obj[i]
                i += 1
            if definition != "":
                if re.fullmatch(FLOAT_REGEX, definition):
                    obj.append(float(definition))
                elif definition == 'true':
                    obj.append(True)
                elif definition == 'false':
                    obj.append(False)
                elif definition == 'null':
                    obj.append(None)
                elif re.fullmatch(INT_REGEX, definition):
                    obj.append(int(definition))
                else:
                    raise ValueError()
            return obj

        return loads_obj(lc_obj)

    @staticmethod
    def load(file):
        with open(file, 'r') as f:
            result = f.read()
            return SerializerJson.loads(result)
