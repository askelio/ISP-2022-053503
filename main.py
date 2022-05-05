from SerializerFactory.factory import Factory
import json
import toml
import yaml

a = {"hello": "world"}


js = Factory.create_serializer("json")

dict = {
    "id": 101,
    "company": "GeeksForGeeks",
    "topics": {"Data Structure": 1,
               "Algorithm": 2,
               "Gate Topics": 3},
    "speed": ["clock", "100"],
    "modules": ["numpy", "simpy", "math"]
}

js.dump(dict, "ConsoleUtility/Files/file.json")



