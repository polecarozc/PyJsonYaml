import json
import yaml
from yaml import SafeLoader

def json_to_yaml():
    name = str(input("enter file name (no extension): ")).lower()
    file = open(name + '.json', "r")
    loader = json.load(file)
    file_conversion = open(name + '1.yaml', 'w')
    yaml.dump(loader,file_conversion)
    file_conversion.close()
    print('saved!')

def yaml_to_json():
    name = str(input("enter file name (no extension): ")).lower()
    file = open(name + '.yaml', 'r')
    loader = yaml.load(file, Loader=SafeLoader)
    file_conversion = open(name + '1.json', 'w')
    json.dump(loader,file_conversion)
    file_conversion.close()
    print('saved!')


if __name__ == '__main__':
    choice = input("pick a conversion: ").lower()
    if choice == "json":
        json_to_yaml()
    else:
        yaml_to_json()