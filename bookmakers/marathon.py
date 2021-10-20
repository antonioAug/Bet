from generale import evento, eventi
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from dataclasses_json import dataclass_json

MONTHS = {'Gen': '01',
'Feb': '02',
'Mar': '03',
'Apr': '04',
'Mag': '05',
'Giu': '06',
'Lug': '07',
'Ago': '08',
'Set': '09',
'Ott': '10',
'Nov': '11',
'Dic': '12'
}

class Marathon:
    def __init__(self):
        self.url = ""
        self.bookMaker = "MarathonBet"
        self.eventi = list()

        self.__carica()

        self.dizionario = eventi(self.eventi)
        self.dizionario.scriviPrimo(self.dizionario.to_json())


    def __carica(self):
        driver = webdriver.Firefox(executable_path='../geckodriver')
        driver.get("https://www.marathonbet.it/it/betting/Tennis+-+2398?interval=ALL_TIME")

        primiNomi = driver.find_elements(By.XPATH, '//tr[@class=\'sub-row\']/td[1]/table/tbody/tr[1]/td[1]/div/div/a')
        secondiNomi = driver.find_elements(By.XPATH, "//tr[@class='sub-row']/td[1]/table/tbody/tr[2]/td/div/div/a")

        dateLista = driver.find_elements(By.XPATH, "//td[@class='date date-short']")

        quoteVittoria = driver.find_elements(By.XPATH, "//tr[@class='sub-row']/td[3]")
        quoteSconfitta = driver.find_elements(By.XPATH, "//tr[@class='sub-row']/td[4]")

        for i in range(len(primiNomi)):
            nomeCasa = primiNomi[i].text
            nomeTrasferta = secondiNomi[i].text
            data = self.__trasformaData(dateLista[i].text)
            vittoria = {'value': float(quoteVittoria[i].text), 'bookMaker': self.bookMaker}
            sconfitta = {'value': float(quoteSconfitta[i].text), 'bookMaker': self.bookMaker}

            self.eventi.append(evento(nomeCasa, nomeTrasferta, data, vittoria, sconfitta))

        driver.close()

    def __trasformaData(self, data):
        today = date.today()
        if len(data.split()) == 1:
            return today.strftime("%Y-%m-%d") + " " + data + ":00"
        else:
            day, month, ora = data.split()
            return today.strftime("%Y") + "-" + MONTHS[month] + "-" + day + " " + ora + ":00"


if __name__ == '__main__':
    marathon = Marathon()
    # print(marathon.dizionario.events[0].casa)