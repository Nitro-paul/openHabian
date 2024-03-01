# Module

import ErrorHandler
import SettingHandler


class Action():
    url: str
    header: dict
    stagedValue: int

    def __init__(self) -> None:
        try:
            import requests
        except Exception:
            ErrorHandler.fatal("unable to import requests")

    def setUrl(self, url: str) -> None:
        self.url = url

    def getUrl(self) -> str:
        return self.url

    def makeUrl(self, itemName: str) -> None:
        openHabAdress = SettingHandler.get(["openHab", "serverAdress"])
        openHabAdress += f'/rest/items/'
        openHabAdress += itemName
        self.url = openHabAdress

    def makeHeader(self) -> None:
        self.header = SettingHandler.get(["openHab", "AccesHeader"])

    def sendRequest(self, data: str) -> None:
        try:
            requests.post(url=self.url, headers=self.header, data=data)
        except Exception:
            ErrorHandler.fatal("unable to act on openhab server")

    def requestValue(self) -> str:
        pass

    def SendRequestAutomatic(self, itemName: str, data: str):
        self.makeUrl(itemName=itemName)
        self.makeHeader()
        if self.shallowTest():
            self.sendRequest(data=data)
        else:
            ErrorHandler.message("shallow test resulted in possible failure, deep test started(at request sending)")
            result = self.deepTest()
            if result[0]:
                ErrorHandler.message("deep test did find nothing(at request sending)")
            else:
                ErrorHandler.error(f'{result[1]}, trying annyways')
                self.sendRequest(data)

    def shallowTest(self) -> bool:  # returns true if set requests seem to be working
        return True

    def deeptest(self) -> dict:
        return True
