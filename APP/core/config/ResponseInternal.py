from config.Logs.LogsActivity import Logs

class ResponseInternal():
    def __init__(self) -> None:
        pass
    @staticmethod
    def responseInternal(status:bool,mesagge:str,response):
        
        Logs.WirterTask(mesagge)
        
        return{"status":status,"mesagge":mesagge,"response":response}
    
