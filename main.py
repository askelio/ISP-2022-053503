from SerializerFactory.factory import Factory
from SerializerFactory.Serializers.serializer import Serializer
from numpy import sin
import json
import yaml
import toml
import re

def fun(n):
    print("ddd")


def user_code():
    ser = Factory.create_serializer("toml")

    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann", "Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }

    fp = "/home/askelio/Desktop/BSUIR/ISP/LR_2/file"

    # fun(10)

    a = Serializer.serialize(fun)

    b = Serializer.deserialize(a)

    print(a)

    # print(b(5))


if __name__ == '__main__':
    user_code()

