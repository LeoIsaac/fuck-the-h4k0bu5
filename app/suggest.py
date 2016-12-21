from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Suggest:
    def getSuggest(self, ori:str, des:str) -> dict:
        if not ori and not des: return {}

        params = urlencode({'stopname_f': ori, 'stopname_t': des}, encoding='sjis')
        html = urlopen('http://www.hakobus.jp/search02.php?' + params)
        soup = BeautifulSoup(html, "html.parser")

        origin = []
        destination = []

        for stop in soup.find('select', id="in").find_all('option'):
            origin.append({"stop": stop.string})

        for stop in soup.find('select', id="out").find_all('option'):
            destination.append({"stop": stop.string})

        json = {}
        json["origin"] = origin
        json["destination"] = destination
        return json


    def getDecision(self, ori:str, des:str) -> dict:
        return "Hello"
