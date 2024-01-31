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
             with open(f'{PathMunay().getLogs()}systemLog{str(datetime.date.today())}.log','a+') as archivo:
                archivo.write(f' \033[0;36m[{datetime.datetime.now()}]:\033[0;32m{mensaje}\n')
                archivo.close()
        except TypeError as error:
            print('error al iniciar los logs de actividasdes')
            print(error)
    def Warnings(mensaje:str):
        '''
        Este código es un método estático que se utiliza para registrar advertencias en un archivo de registro. Toma un mensaje como entrada y lo agrega al archivo de registro "systemLog.log" junto con la marca de tiempo actual.

        Ejemplo de uso:
        LogsActivity.Warnings("Este es un mensaje de advertencia")

        '''
        try:
            with open(f'{PathMunay().getLogs()}systemLog{str(datetime.date.today())}.log', 'a+') as archivo :
                archivo.write(f' \033[0;36m[{datetime.datetime.now()}]:\033[0;33m {mensaje}\n')
                archivo.close()
        except TypeError as error:
            print('error al iniciar los logs de actividades')
    @staticmethod
    def Error( mensaje:str):
        try:
            with open(f'{PathMunay().getLogs()}systemLog{datetime.date.today()}.log', 'a+') as archivo :
                archivo.write(f' \033[0;36m[{datetime.datetime.now()}]:\033[0;31m {mensaje}\n')
                archivo.close()
        except TypeError as error:
            print('error al iniciar los logs de actividades')
    def __del__(self) -> object:
        print('cerrando los logs')