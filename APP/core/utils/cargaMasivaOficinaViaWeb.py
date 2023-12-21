import pandas as pd
import requests

# Leer el archivo Excel
data = pd.read_excel('oficinas.xlsx')

# Iterar sobre las filas del archivo Excel
for index, row in data.iterrows():
    payload = {
        "id": str(row['id']),
        "capacidad": int(row['capacidad']),
        "idResponsable": int(row['idResponsable']),
        "status": str(row['status']),
        "precio": float(row['precio']),
        "sede": str(row['sede']),
        "fechaInicio": str(row['fechaInicio']),
        "fechaFin": str(row['fechaFin']),
        "deposito": float(row['deposito']),
        "fechaPago": str(row['fechaPago'])
    }

    # Realizar la solicitud POST
    response = requests.post('http://10.10.3.166:8010/MUNAY/oficinas/registroOficina', json=payload)

    # Imprimir la respuesta
    print(response.json())
