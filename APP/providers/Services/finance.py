import requests
class Finance:
    __urlBCV = 'https://pydolarvenezuela-api.vercel.app/api/v1/dollar/page?page=bcv'
    def __init__(self):
        pass
    def getTasaBcv(self):
       
        """
    
    Este método realiza una solicitud GET a la URL almacenada en self.__urlBCV.

    :returns: Si la solicitud es exitosa (código de estado 200), devuelve el precio del USD 
              obtenido de la respuesta JSON. Si la solicitud no es exitosa, devuelve False.
    :rtype: float o bool
    """
        response = requests.get(self.__urlBCV)
        if response.status_code == 200:
            data =  response.json()
            dataConvert = dict(data)
            return float(dataConvert['monitors']['usd']['price'])
        else:
            return False