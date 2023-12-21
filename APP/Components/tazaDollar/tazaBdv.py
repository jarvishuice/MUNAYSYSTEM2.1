import requests

def obtener_cotizacion_dolar():
    url = 'https://s3.amazonaws.com/dolartoday/data.json'
    response = requests.get(url)
    data = response.json()
    cotizacion = data['USD']['bcv']
    return cotizacion

cotizacion_dolar = obtener_cotizacion_dolar()
print(cotizacion_dolar)
