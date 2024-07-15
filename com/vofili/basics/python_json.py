import json
from json import JSONDecodeError,JSONEncoder,JSONDecoder

ss = {"c":0,"b":23,"a":1}
print(type(ss))

#Encoding a Python Dictionary to JSON String

json_str = json.dumps(ss)
print(json_str)
print(type(json_str))

#Decoding a JSON String to a Python Dictionary

ss_dict = json.loads(json_str)
print()
print(ss_dict)
print(type(ss_dict))


class Animal:
    def __init__(self, name):
        self.name=name

animals = {"a":Animal("Antelope"),"b":Animal("buffalo"),"c":Animal("Chimpanzee")}
print(animals)

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        else:
            super().default(o)
json_animals = json.dumps(animals,cls=AnimalEncoder)
print(json_animals)
print(type(json_animals))

