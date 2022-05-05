import unittest
from SerializerFactory.factory import Factory
from SerializerFactory.Serializers.serializer import Serializer
import test_suite as ts


class TestMethods(unittest.TestCase):
    def __init__(self, method):
        super().__init__(method)
        self.json = Factory.create_serializer("json")
        self.yaml = Factory.create_serializer("yaml")
        self.toml = Factory.create_serializer("toml")
        self.fnc_ser = Serializer()

    # test simple objects serialization
    def test_int(self):

        json_test = self.json.loads(self.json.dumps(ts.int_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(ts.int_test))
        toml_test = self.toml.loads(self.toml.dumps(ts.int_test))

        self.assertEqual(json_test, ts.int_test)
        self.assertEqual(yaml_test, ts.int_test)
        self.assertEqual(toml_test, ts.int_test)

    def test_float(self):

        json_test = self.json.loads(self.json.dumps(ts.float_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(ts.float_test))
        toml_test = self.toml.loads(self.toml.dumps(ts.float_test))

        self.assertEqual(json_test, ts.float_test)
        self.assertEqual(yaml_test, ts.float_test)
        self.assertEqual(toml_test, ts.float_test)

    def test_str(self):

        json_test = self.json.loads(self.json.dumps(ts.str_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(ts.str_test))
        toml_test = self.toml.loads(self.toml.dumps(ts.str_test))

        self.assertEqual(json_test, ts.str_test)
        self.assertEqual(yaml_test, ts.str_test)
        self.assertEqual(toml_test, ts.str_test)

    def test_bool(self):
        json_test = self.json.loads(self.json.dumps(ts.bool_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(ts.bool_test))
        toml_test = self.toml.loads(self.toml.dumps(ts.bool_test))

        self.assertEqual(json_test, ts.bool_test)
        self.assertEqual(yaml_test, ts.bool_test)
        self.assertEqual(toml_test, ts.bool_test)

    # test list and tuple serialization
    def test_tuple(self):
        json_test = self.json.loads(self.json.dumps(ts.tuple_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(ts.tuple_test))
        toml_test = self.toml.loads(self.toml.dumps(ts.tuple_test))

        self.assertEqual(tuple(json_test), ts.tuple_test)
        self.assertEqual(yaml_test, ts.tuple_test)
        self.assertEqual(tuple(toml_test), ts.tuple_test)

    def test_list(self):
        json_test = self.json.loads(self.json.dumps(ts.list_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(ts.list_test))
        toml_test = self.toml.loads(self.toml.dumps(ts.list_test))

        self.assertEqual(json_test, ts.list_test)
        self.assertEqual(yaml_test, ts.list_test)
        self.assertEqual(toml_test, ts.list_test)

    # test complex dict serialization
    def test_cdict(self):
        json_test = self.json.loads(self.json.dumps(ts.dict_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(ts.dict_test))
        toml_test = self.toml.loads(self.toml.dumps(ts.dict_test))

        self.assertEqual(json_test, ts.dict_test)
        self.assertEqual(yaml_test, ts.dict_test)
        self.assertEqual(toml_test, ts.dict_test)

    # test class serialization
    def test_class(self):
        cl_test = ts.TestClass().__dict__

        json_test = self.json.loads(self.json.dumps(cl_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(cl_test))
        toml_test = self.toml.loads(self.toml.dumps(cl_test))

        self.assertEqual(json_test, cl_test)
        self.assertEqual(yaml_test, cl_test)
        self.assertEqual(toml_test, cl_test)

    # test function serialization
    def test_func_global_params(self):
        self.assertEqual(self.fnc_ser.deserialize_function(self.fnc_ser.serialize_func(ts.question))(), ts.question())

    def test_func_local_params(self):
        self.assertEqual(self.fnc_ser.deserialize_function(self.fnc_ser.serialize_func(ts.mul_params))(5, 4),
                         ts.mul_params(5, 4))

    def test_func_bytoma_func(self):
        self.assertEqual(self.fnc_ser.deserialize_function(self.fnc_ser.serialize_func(ts.f))(5), ts.f(5))



