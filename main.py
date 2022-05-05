from SerializerFactory.factory import Factory
import json
import toml
import yaml

a = {"hello": "world"}


js = Factory.create_serializer("json")

d= {
    "id": 101,
    "company": "GeeksForGeeks",
    # "topics": {"Data Structure": 1,
    #            "Algorithm": 2,
    #            "Gate Topics": 3},
    "speed": ["clock","ass"],
    "modules": ["numpy", "simpy", "math"]
}

a = {"hello": {"ff":1}}

print(toml.dumps(d))

print(toml.loads(toml.dumps(d)))



