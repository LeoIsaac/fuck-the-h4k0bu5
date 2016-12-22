from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Suggest:
    def __init__(self, ori:str, des:str):
        self.ori = ori
        self.des = des


    def getSuggest(self) -> dict:
        if not self.ori and not self.des: return {}

        params = urlencode({'stopname_f': self.ori, 'stopname_t': self.des}, encoding='sjis')
        html = urlopen('http://www.hakobus.jp/search02.php?' + params)
        soup = BeautifulSoup(html, "html.parser")

        origin = []
        destination = []

        for stop in soup.find('select', id="in").find_all('option'):
            origin.append({"stop": stop.string, "id": stop.get("value")})

        for stop in soup.find('select', id="out").find_all('option'):
            destination.append({"stop": stop.string, "id": stop.get("value")})

        json = {}
        json["origin"] = origin
        json["destination"] = destination
        return json


    def getDecision(self) -> dict:
        suggest = self.getSuggest()
        ori_id = suggest["origin"][0]["id"]
        des_id = suggest["destination"][0]["id"]

        params = urlencode({'in': ori_id, 'out': des_id})
        html = urlopen('http://www.hakobus.jp/result.php?' + params)
        soup = BeautifulSoup(html, "html.parser")

        json = []

        for tr in soup.find("div", id="result").find_all("tr"):
            railroad = {}
            for i, td in enumerate(tr.find_all("td")):
                if i == 1: railroad["time"] = td.string
                if i == 4: railroad["goal"] = td.string
                if i == 7: railroad["state"] = td.string

            if "time" in railroad:
                json.append(railroad)
    
        return json
