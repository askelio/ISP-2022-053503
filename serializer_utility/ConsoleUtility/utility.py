import argparse
import pathlib
from SerializerFactory.factory import Factory


"""
    Utility to convert serialized data from one format to another
    
    Available arguments:     
        --src - source path    
        --dst - destination path
        --ext - extension(json/yaml/toml)
"""


def utility_code():

    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, required=True)
    parser.add_argument('--dst', type=str, required=True)
    parser.add_argument('--ext', type=str, required=True)

    print("This utility allows to convert serialized data from one format to another")

    args = parser.parse_args()

    source = args.src
    destin = args.dst
    extens = args.ext

    print("Source: " + source)
    print("Destination: " + destin)
    print("Convert extension " + extens)

    serializer = Factory.create_serializer(extens)
    deserializer = Factory.create_serializer(pathlib.Path(source).suffix[1:])

    src_temp = deserializer.load(source)

    serializer.dump(src_temp, destin)


if __name__ == "__main__":
    utility_code()
