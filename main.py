from SerializerFactory.factory import Factory
from SerializerFactory.Serializers.serializer import Serializer
import math
import inspect
import types


c = 42
def fun(x):
    a = 123
    return math.sin(x * a * c)


def user_code():
    a = Serializer.serialize_func(fun)
    print(a)
    b = Serializer.deserialize_function(a)
    print(b(5))


if __name__ == '__main__':
    user_code()

