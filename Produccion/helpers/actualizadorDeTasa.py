import requests
import time
import os

url = "http://191.97.17.26:8010/MUNAY/nest/finance/"

# Asegúrate de reemplazar esto con los datos que deseas enviar
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""************************************************************""")
    print("""* actualizador de cotizacion del  dolar bcv de munaysystem *""")
    print("""************************************************************""")
    

    print("Sincronizando con el BCV......")
    response = requests.post(url)
    print("Sincronizacion Finalizada .......")    

    # Imprime el estado de la respuesta
    print("Estado de la respuesta:", response.status_code)
    if response.status_code == 200:
        print(f"tasa actualizada de manera correcta \nnueva tasa :[{response.json()}]")
    
    
    # Espera una hora (3600 segundos)
    time.sleep(3600)
