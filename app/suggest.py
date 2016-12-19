from bs4 import BeautifulSoup

class Suggest:
    def getSuggest(self, ori:str, des:str) -> dict:
        if not ori or not des: return {}

        json = {}
        origin = []
        destination = []
        origin.append({"stop": ori})
        destination.append({"stop": des})
        json["origin"] = origin
        json["destination"] = destination
        return json
