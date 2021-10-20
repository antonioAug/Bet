from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json
from generale import evento, eventi, confronta

class Sisal:
    def __init__(self):
        self.url = ""
        self.bookMaker = "Sisal"
        self.eventi = list()

        self.__carica()

        self.dizionario = eventi(self.eventi)
        confronta(self.dizionario)

    def __carica(self):
        driver = webdriver.Firefox(executable_path='../geckodriver')
        driver.get("view-source:https://www.sisal.it/api-betting/lettura-palinsesto-sport/palinsesto/prematch/alberaturaPrematch")
        testo = driver.find_element(By.TAG_NAME, 'pre')
        testo = testo.text.strip()
        diz = json.loads(testo)

        manifestazioni = [man for man in diz['manifestazioneListByDisciplinaOggiEDomani']['3']]
        # print(manifestazioni)


        for manifestazione in manifestazioni:
            driver.get("view-source:https://www.sisal.it/api-betting/lettura-palinsesto-sport/palinsesto/prematch/schedaManifestazione/0/" + manifestazione)
            sleep(0.5)

            testo = driver.find_element(By.TAG_NAME, 'pre')
            testo = testo.text.strip()
            diz = json.loads(testo)

            chiavi = [incontro['key'] for incontro in  diz['avvenimentoFeList']]
            descrizioni = [incontro['descrizione'] for incontro in diz['avvenimentoFeList']]
            date = [incontro['data'] for incontro in diz['avvenimentoFeList']]
            # chiaviScom = [incontro + "2-0" for incontro in chiavi]


            for idx, chiave in enumerate(chiavi):
                # print(type(chiave))
                chiaveScom = chiave + "-2-0"
                if chiaveScom in diz['infoAggiuntivaMap']:
                    casa, trasferta = self.__trasformaNomi(descrizioni[idx])
                    data = self.__trasformaData(date[idx])
                    vittoria = {'value': diz['infoAggiuntivaMap'][chiaveScom]['esitoList'][0]['quota'] / 100, 'bookMaker': self.bookMaker}
                    sconfitta = {'value' :diz['infoAggiuntivaMap'][chiaveScom]['esitoList'][1]['quota'] / 100, 'bookMaker': self.bookMaker}

                    self.eventi.append(evento(casa, trasferta, data, vittoria, sconfitta))

        driver.close()

    def __trasformaNomi(self, descr):
        if len(descr.split('-')) == 2:
            n1, n2 = descr.split(" - ")
        else:
            n1, n2 = descr[:descr.find(' - ')], descr[descr.find(' - ') + 3:]

        return n1, n2


    def __trasformaData(self, data):
        data = data.replace('Z', ' ')
        data = data.replace('T', ' ')
        return data


if __name__ == "__main__":
    sisal = Sisal()
    # print(sisal.dizionario.events[0:5])



