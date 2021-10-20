import json
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List


@dataclass
class evento:
    casa: str
    trasferta: str = field(compare=False)
    data: str = field(compare=False)
    vittoria: dict = field(compare=False)
    sconfitta: dict = field(compare=False)

    #
    # def __eq__(self, other):
    #     return self.casa == other.casa and self.trasferta == other.trasferta

@dataclass_json
@dataclass()
class eventi:
    events: List[evento]

    def scriviPrimo(self, stringaJson: str):
        jsonFile = open('../risultati.json', 'w')
        jsonFile.write(stringaJson)
        jsonFile.close()

def confronta(eventiDaConfrontare):
    jsonFile = open('../risultati.json', 'r')
    lines = jsonFile.readline()
    # eventiJson = json.load(jsonFile)
    eventiFile = eventi.from_json(lines)
    jsonFile.close()

    nuoviEventi = []
    for ev1 in eventiFile.events:
        for ev2 in eventiDaConfrontare.events:
            vittoria = {}
            sconfitta = {}
            if ev1 == ev2:
                vittoria = ev2.vittoria if ev2.vittoria['value'] > ev1.vittoria['value'] else ev1.vittoria
                sconfitta = ev2.sconfitta if ev2.sconfitta['value'] > ev1.sconfitta['value'] else ev1.sconfitta

                break

        else:
            vittoria = ev1.vittoria
            sconfitta = ev1.sconfitta


        casa = ev1.casa
        trasferta = ev1.trasferta
        data = ev1.data

        nuoviEventi.append(evento(casa, trasferta, data, vittoria, sconfitta))


    newEvents = eventi(nuoviEventi)
    newEvents.scriviPrimo(newEvents.to_json())