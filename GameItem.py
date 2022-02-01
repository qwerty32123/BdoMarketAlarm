import requests
from bs4 import BeautifulSoup
import datetime
from datetime import datetime


class GameItem:

    def __init__(self,id,enchant,price,timestamp_sell,timestamp_posted) -> None:
        self.id = id
        self.enhancement = int(enchant)
        self.price = str(int(price) / 1000000000)
        self.TimeStamp_sell = int(timestamp_sell)
        self.TimeStamp_posted = timestamp_posted
        self.name = self.getName()
        self.EnchanmentString = self.setEnchanmentLevel()

        super().__init__()

    def __str__(self) -> str:
        return "Item with ID:"+ self.id +" "+self.name + " " + self.EnchanmentString +" is going to be sell for "+self.price +"B in "+ self.getMarketHitTime()

    def getName(self):

        r = requests.get('https://bdocodex.com/us/item/{}/'.format(self.id),proxies=proxies)
        soup = BeautifulSoup(r.text, "html.parser")
        item_name = soup.find('title').text.replace('- BDO Codex', '')
        return item_name

    def getMarketHitTime(self):
        s = datetime.fromtimestamp(self.TimeStamp_sell)
        now = datetime.now()
        result = s - now
        return str(result)

    def setEnchanmentLevel(self):
        if self.enhancement == 0:
            return "Base"
        elif self.enhancement == 1:
            return "PRI"
        elif self.enhancement == 2:
            return "DUO"
        elif self.enhancement == 3:
            return "TRI"
        elif self.enhancement == 4:
            return "TET"
        elif self.enhancement == 5:
            return "PEN"
        elif self.enhancement == 6:
            return "+6"
        elif self.enhancement == 7:
            return "+7"
        elif self.enhancement == 8:
            return "+8"
        elif self.enhancement == 9:
            return "+9"
        elif self.enhancement == 10:
            return "+10"
        elif self.enhancement == 11:
            return "+11"
        elif self.enhancement == 12:
            return "+12"
        elif self.enhancement == 13:
            return "+13"
        elif self.enhancement == 14:
            return "+14"
        elif self.enhancement == 15:
            return "+15"
        elif self.enhancement == 16:
            return "PRI"
        elif self.enhancement == 17:
            return "DUO"
        elif self.enhancement == 18:
            return "TRI"
        elif self.enhancement == 19:
            return "TET"
        elif self.enhancement == 20:
            return "PEN"


