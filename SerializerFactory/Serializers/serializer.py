import inspect
import re
from types import CodeType, FunctionType
from pydoc import locate

FUNC_ATTRS = [
    '__code__',
    '__name__',
    '__defaults__',
    '__closure__'
]


CODE_OBJECT_ARGS = [
        'co_cellvars',
        'co_code',
        'co_consts',
        'co_filename',
        'co_firstlineno',
        'co_flags',
        'co_freevars',
        'co_kwonlyargcount',
        #'co_linetable', #what the fuck?!??
        'co_lnotab',
        'co_name',
        'co_names',
        'co_nlocals',
        'co_posonlyargcount',
        'co_argcount',
        'co_stacksize',
        'co_varnames'
    ]


class Serializer:
    @staticmethod
    def serialize(obj):
        res = {}
        obj_type = type(obj)

        if obj_type == dict:
            res['type'] = 'dict'
            res['value'] = {}
            for i in obj:
                key = Serializer.serialize(i)
                value = Serializer.serialize(obj[i])
                res['value'][key] = value
            res['value'] = tuple((k, res['value'][k]) for k in res['value'])
        elif obj_type == list:
            res['type'] = 'list'
            res['value'] = tuple([Serializer.serialize(i) for i in obj])
        elif obj_type == tuple:
            res['type'] = 'tuple'
            res['value'] = tuple([Serializer.serialize(i) for i in obj])
        elif obj_type == bytes:
            res['type'] = 'bytes'
            res['value'] = tuple([Serializer.serialize(i) for i in obj])
        elif obj is None:
            res['type'] = 'NoneType'
            res['value'] = None
        elif inspect.isroutine(obj):#routine возвращает true, если объект имеет тип функции или метода.
            res['type'] = 'function'
            res['value'] = {}
            func_members = inspect.getmembers(obj)
            func_members = [i for i in func_members if i[0] in FUNC_ATTRS]
            for i in func_members:
                key = Serializer.serialize(i[0])
                if i[0] != '__closure__':
                    value = Serializer.serialize(i[1])
                else:
                    value = Serializer.serialize(None)
                res['value'][key] = value
                if i[0] == '__code__':
                    key = Serializer.serialize('__globals__')
                    res['value'][key] = {}
                    names = i[1].__getattribute__('co_names')
                    glob = obj.__getattribute__('__globals__')
                    globals_d = {}
                    for name in names:
                        if name == obj.__name__:
                            globals_d[name] = obj.__name__
                        elif name in glob and not inspect.ismodule(name) and name not in __builtins__:
                            globals_d[name] = glob[name]
                    res['value'][key] = Serializer.serialize(globals_d)
            res['value'] = tuple((k, res['value'][k]) for k in res['value'])

        elif isinstance(obj, (int, float, complex, bool, str)):
            typestr = re.search(r"\'(\w+)\'", str(obj_type)).group(1)
            res['type'] = typestr
            res['value'] = obj
        else:
            res['type'] = 'instance'
            res['value'] = {}
            class_members = inspect.getmembers(obj)
            class_members = [i for i in class_members if not callable(i[1])]
            for i in class_members:
                key = Serializer.serialize(i[0])
                value = Serializer.serialize(i[1])
                res['value'][key] = value
            res['value'] = tuple((k, res['value'][k]) for k in res['value'])

        res = tuple((k, res[k]) for k in res)
        return res

    @staticmethod
    def deserialize(obj):
        d = dict((a, b) for a, b in obj)
        obj_type = d['type']
        res = None
        if obj_type == 'list':
            res = [Serializer.deserialize(i) for i in d['value']]
        elif obj_type == 'tuple':
            res = tuple([Serializer.deserialize(i) for i in d['value']])
        elif obj_type == 'dict':
            res = {}
            for i in d['value']:
                value = Serializer.deserialize(i[1])
                res[Serializer.deserialize(i[0])] = value
        elif obj_type == 'function':
            func = [0] * 4
            code = [0] * 16
            glob = {'__builtins__': __builtins__}
            for i in d['value']:
                key = Serializer.deserialize(i[0])
                if key == '__globals__':
                    global_d = Serializer.deserialize(i[1])
                    for global_key in global_d:
                        glob[global_key] = global_d[global_key]
                elif key == '__code__':
                    value = i[1][1][1]   #list of lists
                    for arg in value:
                        code_arg_key = Serializer.deserialize(arg[0])
                        if code_arg_key != '__doc__':
                            code_arg_val = Serializer.deserialize(arg[1])
                            index = CODE_OBJECT_ARGS.index(code_arg_key)
                            code[index] = code_arg_val
                    code = CodeType(*code)
                else:
                    index = FUNC_ATTRS.index(key)
                    func[index] = (Serializer.deserialize(i[1]))

            func[0] = code
            func.insert(1, glob)

            res = FunctionType(*func)
            if res.__name__ in res.__getattribute__('__globals__'):
                res.__getattribute__('__globals__')[res.__name__] = res

        elif obj_type == 'NoneType':
            res = None
        elif obj_type == 'bytes':
            res = bytes([Serializer.deserialize(i) for i in d['value']])
        else:
            if obj_type == 'bool':
                res = d['value'] == 'True'
            else:
                res = locate(obj_type)(d['value'])
        return res



from types import FunctionType, CodeType
import inspect

st_types = ["int", "float", "bool", "str", "None"]
st_iter_types = ["list", "tuple", "set"]
types_to_classes = {"int": int, "float": float, "bool": bool, "str": str, "None": None, "list": list, "tuple": tuple, "set": set, "dict": dict}
CODE_OBJ_ATTR = (
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars'
)

def serialize(obj):
    response = {}
    if obj is None:
        return {"None": None}
    if type(obj) == FunctionType:
        return {"func": serialize(serialize_function(obj))}
    if type(obj).__name__ in st_types:
        response = {type(obj).__name__: obj}
    elif type(obj).__name__ in st_iter_types:
        res_list = []
        for item in obj:
            res_list.append(serialize(item))
        response = {type(obj).__name__: res_list}
    elif type(obj).__name__ == 'dict':
        res_dict = {}
        i = 0
        for key, value in obj.items():
            res_dict["item" + str(i)] = {"key": serialize(key), "value": serialize(value)}
            i += 1
        response = {type(obj).__name__: res_dict}
    return response


def deserialize(obj):
    response = None
    if type(obj).__name__ == 'dict':
        if len(obj) == 1 and 'dict' in obj:
            response = {}
            for key, item in obj['dict'].items():
                 response[deserialize(item['key'])] = deserialize(item['value'])
        elif len(obj) == 1 and 'func' in obj:
            return deserialize_function(deserialize(obj["func"]))
        else:
            for key, value in obj.items():
                response = create_standard_type(key, deserialize(value))
                return response
    if type(obj).__name__ in st_iter_types:
        response = []
        for item in obj:
             response.append(deserialize(item))

    if response is None:
        return str(obj)
    else:
        return response


def create_standard_type(typename, value):
    if typename == "None":
        return None
    else:
        return types_to_classes[typename](value)


def serialize_function(func):
    members = dict(inspect.getmembers(func))
    CODE_OBJ_ATTR = dict(inspect.getmembers(members['__code__']))
    special = []
    for attr_name in CODE_OBJ_ATTR:
        if attr_name == 'co_lnotab' or attr_name == 'co_code':
            if len(list(CODE_OBJ_ATTR[attr_name])) == 0:
                special.append(None)
            else:
                special.append(list(CODE_OBJ_ATTR[attr_name]))
        else:
            if CODE_OBJ_ATTR[attr_name] == ():
                special.append(None)
            else:
                special.append(CODE_OBJ_ATTR[attr_name])

    name = members['__name__']
    globals_res = {"__name__": name}
    for outer_obj_name in CODE_OBJ_ATTR['co_names']:
        if outer_obj_name == name:
            globals_res[outer_obj_name] = outer_obj_name
            continue
        if outer_obj_name in __builtins__:
            continue
        globals_res[outer_obj_name] = serialize(members['__globals__'][outer_obj_name])
    # print(special)
    return {"__code__": special, "__globals__": globals_res, "__name__": name,
            "__defaults__": members['__defaults__']}


def deserialize_function(obj):
    recursive_flag = False
    globals = obj['__globals__']
    for outer_obj_name, outer_obj in globals.items():
        if outer_obj_name == obj['__name__']:
            recursive_flag = True
        globals[outer_obj_name] = deserialize(outer_obj)
    globals['__builtins__'] = __builtins__

    code = obj['__code__']
    for i in range(len(code)):
        # co_lnotab
        if i == 13 and code[i] is None:
            code[i] = b''
        if code[i] is None:
            code[i] = ()
        elif isinstance(code[i], list):
            code[i] = bytes(code[i])
    func = FunctionType(CodeType(*code), globals,
                    obj['__name__'], obj['__defaults__'], None)
    if recursive_flag:
        func.__getattribute__('__globals__')[obj['__name__']] = func
    return func
