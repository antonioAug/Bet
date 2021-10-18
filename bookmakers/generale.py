from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List


@dataclass
class evento:
    casa: str
    trasferta: str
    data: str
    vittoria: dict = field(compare=False)
    sconfitta: dict = field(compare=False)

@dataclass_json
@dataclass()
class eventi:
    events: List[evento]

    def scriviFile(self, stringaJson: str):
        jsonFile = open('../risultati.json', 'w')
        jsonFile.write(stringaJson)
        jsonFile.close()


class Generale():
    pass