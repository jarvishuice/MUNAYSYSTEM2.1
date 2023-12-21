import datetime
from config.router.pahtsMunay import PathMunay
class Logs:
    def __inti__(self):
        print('Call  Logs')
        
        
    @staticmethod
    def  WirterTask(mensaje):
        try: 
             with open(f'{PathMunay().getLogs()}ActivityMunay.log','a') as archivo:
                archivo.write(f' \033[0;36m[{datetime.datetime.now()}]:\033[0;32m{mensaje}\n')
                archivo.close()
        except TypeError as error:
            print('error al iniciar los logs de actividasdes')
            print(error)
    def __del__(self):
        print('cerrando los logs')