import requests
class Finance:
    __urlBCV = 'https://pydolarvenezuela-api.vercel.app/api/v1/dollar/page?page=bcv'
    def __init__(self):
        pass
    def getTasaBcv(self):
        response = requests.get(self.__urlBCV)
        if response.status_code == 200:
            data =  response.json()
            dataConvert = dict(data)
            return float(dataConvert['monitors']['usd']['price'])
        else:
            return False