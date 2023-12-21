from typing_extensions import override
from core.Interface.config.DataBase.conectionsInterface import ConectionDbInterface
import psycopg2
from core.config.ResponseInternal import ResponseInternal
from config.Logs.LogsActivity import Logs
from config.Db.datosconfig import CredentialDb
class ConectionsPsqlInterface(ConectionDbInterface):
    
    OPERATIONAL_ERROR=psycopg2.OperationalError
    DATABASE_ERROR=psycopg2.DatabaseError
    INTEGRIDAD_ERROR=psycopg2.IntegrityError
    INTERFACE_ERROR=psycopg2.InternalError
    @override   
    def connect(self):
        try:
            self.conn = psycopg2.connect(CredentialDb().getDatos())
    
            return ResponseInternal.responseInternal(status=True,mesagge="Conexión exitosa a la base de datos",response='conecion exitosa')
        except psycopg2.OperationalError as err:
            return ResponseInternal.responseInternal(status=False,mesagge=f"{self.ERROR} Error en la conexion a la base de datos {err}",response=None)
        except psycopg2.InterfaceError as err:
            return ResponseInternal.responseInternal(status=False,mesagge=f"{self.ERROR} Error en la conexion a la base de datos {err}",response=None)
        except psycopg2.DatabaseError as err:
            return ResponseInternal.responseInternal(status=False,mesagge=f"Error de data bas e al intentar conectar as {err} ",response=None)
    @override 
    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            Logs.WirterTask("Desconexión exitosa de la base de datos")
            self.conn = None
        else:Logs.WirterTask(f"{self.NOTE}no tiene conexion aperturada en estos monetos ")
    