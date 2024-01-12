import datetime
from config.router.pahtsMunay import PathMunay

class Logs:
    """
    Esta es la clase Logs que se encarga de manejar los logs de la aplicación.
    """
    def __inti__(self):
        print('Call  Logs')
        
        
    @staticmethod
    def  WirterTask(mensaje):
        """
        Este es un método estático que escribe un mensaje en el archivo de log 'ActivityMunay.log'.
        El mensaje se escribe con un timestamp.

        Parámetros:
        mensaje (str): El mensaje que se va a escribir en el archivo de log.

        Excepciones:
        TypeError: Se lanza cuando hay un error al iniciar los logs de actividades.
        """
        try: 
             with open(f'{PathMunay().getLogs()}ActivityMunay.log','a') as archivo:
                archivo.write(f' \033[0;36m[{datetime.datetime.now()}]:\033[0;32m{mensaje}\n')
                archivo.close()
        except TypeError as error:
            print('error al iniciar los logs de actividasdes')
            print(error)
    def __del__(self):
        """
        Este es el destructor de la clase Logs. Se llama cuando el objeto de la clase Logs se destruye.
        Imprime 'cerrando los logs'.
        """
        print('cerrando los logs')