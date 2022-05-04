from SerializerFactory.factory import Factory
from SerializerFactory.Serializers.serializer import Serializer
import math
import inspect
import types

class A:
    def t(self):
        print("Hello")

class B:
    def __init__(self):
        self.prt = A()

class C:
    def __init__(self):
        self.Name = "name"
        self.Age = 15


def user_code():
    b = A().__dict__

    print(b)


if __name__ == '__main__':
    user_code()

