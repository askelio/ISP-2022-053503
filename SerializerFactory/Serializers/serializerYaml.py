from SerializerFactory.Serializers.serializerFormat import SerializerFormat


class SerializerYaml(SerializerFormat):

    @staticmethod
    def dump(obj):

        def dumps_complex(complex_obj, tabs=''):
            if len(complex_obj) == 0:
                return '{}\n'
            ans = str()
            for key, item in complex_obj.items():
                ans += tabs + key + ': '
                obj_type = type(item)
                if obj_type is dict:
                    tabs += '\t'
                    if len(item) != 0:
                        ans += '\n'
                    ans += dumps_complex(item, tabs)
                    tabs = tabs[:len(tabs) - 1]
                elif obj_type is list or obj_type is tuple:
                    ans += dumps_simple(item, tabs) + '\n'
                elif obj_type is str:
                    if (' ' in item) or ('\t' in item) or ('\n' in item):
                        ans += '\'' + item + '\'' + '\n'
                    else:
                        ans += item + '\n'
                elif obj_type is bool:
                    if item:
                        ans += "true" + '\n'
                    else:
                        ans += "false" + '\n'
                elif item is None:
                    ans += "null" + '\n'
                else:
                    ans += str(item) + '\n'
            return ans

        def dumps_simple(simple_obj, tabs=''):
            if len(simple_obj) == 0:
                return "[]"
            ans = str()
            for item in simple_obj:
                obj_type = type(item)
                if obj_type == str:
                    ans += '\n' + tabs + '- '
                    if (' ' in item) or ('\t' in item) or ('\n' in item):
                        ans += '\'' + item + '\''
                    else:
                        ans += item
                elif obj_type == dict:
                    ans += '\n' + tabs + '-' + '\n'
                    tabs += '\t'
                    ans += tabs + dumps_complex(item)
                    tabs = tabs[:len(tabs) - 1]
                elif obj_type == list or type(item) == tuple:
                    ans += '\n' + tabs + '- ' + dumps_simple(item)
                elif obj_type == bool:
                    if item:
                        ans += '\n' + tabs + '- ' + 'true'
                    else:
                        ans += '\n' + tabs + '- ' + 'false'
                elif item is None:
                    ans += '\n' + tabs + '- ' + 'null'
                else:
                    ans += '\n' + tabs + '- ' + str(item)
            return ans

        return dumps_complex(obj)

    def dumps(self):
        pass

    def load(self):
        pass

    def loads(self):
        pass
