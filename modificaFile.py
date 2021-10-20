from dataclasses import dataclass
from dataclasses_json import dataclass_json
from bookmakers.generale import eventi, evento

def scriviPrimo(events):
    jsonFile = open('risultati.json', 'r')
    lines = jsonFile.readline()
    jsonFile.close()

def confronta(events):
    jsonFile = open('risultati.json', 'r')
    lines = jsonFile.readline()
    jsonFile.close()

    eventiFile = eventi.from_json(lines)

