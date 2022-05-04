import unittest
from SerializerFactory.factory import Factory
import test_suite as ts
import SerializerFactory.factory


class TestMethods(unittest.TestCase):
    def __init__(self):
        self.json = Factory.create_serializer("json")
        self.yaml = Factory.create_serializer("yaml")
        self.toml = Factory.create_serializer("toml")

    # test simple objects serialization

    def test_int(self):

        json_test = self.json.loads(self.json.dumps(ts.int_test))
        yaml_test = self.yaml.loads(self.yaml.dumps(ts.int_test))
        toml_test = self.toml.loads(self.toml.dumps(ts.int_test))

        self.assertEqual(json_test, ts.int_test)
        self.assertEqual(yaml_test, ts.int_test)
        self.assertEqual(toml_test, ts.int_test)


    # def test_float(self):
    #     pass
    # def test_str(self):
    #     pass
    # def test_bool(self):
    #     pass
    #
    #
    # # test list and tuple serialization
    #
    # def test_tuple(self):
    #     pass
    # def test_list(self):
    #     pass
    #
    #
    # # test complex dict serialization
    #
    # def test_cdict(self):
    #     pass
    #
    #
    # # test class serialization
    #
    # def test_class(self):
    #     pass
    #
    #
    # #test function serialization
    #
    # def test_func_global_params(self):
    #     pass
    #
    # def test_func_local_params(self):
    #     pass
    #
    # def test_func_bytoma_func(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
