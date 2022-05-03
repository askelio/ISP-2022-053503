from SerializerFactory.factory import Factory
import json
import re



def user_code():
    ser = Factory.create_serializer("json")

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

    with open(fp, "w") as f:
        f.write(json.dumps(x))



    a = json.dumps(x)
    b = ser.dumps(x)
    print(b)
    print(json.loads(b))
    print(ser.loads(b))

    # c = ser.loads("Hello")
    # print(c)






if __name__ == '__main__':
    user_code()

