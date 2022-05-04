import types
import builtins
from accessify import protected


class Serializer:

    # Function Serialization
    @staticmethod
    def serialize_func(obj):
        obj_dict = {}

        attrs = {
            "__name__": obj.__qualname__,
            "__defaults__": obj.__defaults__,
            "__closure__": obj.__closure__,
            "__code__": obj.__code__}

        global_ns = {}
        Serializer.__get_closure_globs(obj, global_ns)
        obj_dict["__globals__"] = global_ns
        obj_dict["attributes"] = attrs
        return obj_dict

    @staticmethod
    def __get_closure_globs(obj, globs):
        if hasattr(obj, '__code__'):
            code_obj = obj.__code__
            for var in code_obj.co_consts:  # return const values
                Serializer.__get_closure_globs(var, globs)
            for name in code_obj.co_names:  # tuple of names of local variables
                if name in obj.__globals__.keys() and name != obj.__name__:
                    globs[name] = obj.__globals__[name]
                elif name in dir(builtins):
                    globs[name] = getattr(builtins, name)

    # Function Deserialization
    @staticmethod
    def deserialize_function(obj_dict):
        attrs = obj_dict["attributes"]
        obj = types.FunctionType(
            code=attrs["__code__"],
            globals=obj_dict["__globals__"],
            name=attrs["__name__"],
            argdefs=attrs["__defaults__"],
            closure=attrs["__closure__"],
        )
        return obj




