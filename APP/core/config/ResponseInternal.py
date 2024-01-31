from config.Logs.LogsActivity import Logs

class ResponseInternal():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def responseInternal(status:bool,mesagge:str,response):
        """
        Este método está diseñado para generar una respuesta interna.

        Params:
        status (bool): Un valor booleano que indica el estado de la operación.
        mesagge (str): Un mensaje que describe la operación o su resultado.
        response: La respuesta o el resultado de la operación.

        Retorna:
        dict: Un diccionario que contiene el estado, el mensaje y la respuesta de la operación.

        Uso:
        ClassName.responseInternal(True, "Operación exitosa", {"data": "valor"})
        """
            
        Logs.WirterTask(mesagge)
        
        return{"status":status,"mesagge":mesagge,"response":response}
    
