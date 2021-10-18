from dataclasses import dataclass
from dataclasses_json import dataclass_json
from bookmakers.generale import eventi, evento

jsonFile = open('risultati.json', 'r')
lines = jsonFile.readline()
jsonFile.close()

eventi = eventi.from_json(lines)
print(eventi)
print(eventi.events[0].casa)