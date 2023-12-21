"""Interface The Conections dataBase
posgresql tha operating system 

    Returns:
method tha operations the systems
erential connect and disconect
the methods this override 

    """
#@author
#jarvisHuice
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
class ConectionDbInterface(ABC):
    ERROR="\033[0;31m" 
    NOTE="\033[0;33m"
    DATABASE_ERROR=None
    INTEGRIDAD_ERROR=None
    INTERFACE_ERROR=None
    OPERATIONAL_ERROR=None   
    #conect DataBase
    @abstractmethod
    def connect(self):
        pass 
    #disconect dataBase
    def disconnect(self):
        pass 
    #create register
    def wirter(self,data)-> dict:
        pass
    #read all register table
    def readAll(self) ->dict:
        pass 
    #read one register  filter by  id
    def readOneById(self,id)-> dict:
        pass 
    # searh registers filter by param 
    def search(self,param)->dict:
        pass    
    # read one register by param
    def readOneByParam(self,param) ->dict:
        pass
    #read all by status
    def readOneByStatus(self,status)-> dict:
        pass
    def readAllTwoParm(self,param,param2)-> dict:
        pass
    #lectura de todos los detalles de la entidad vinculada en distintas tablas   
    def readDetailEntity(self,id)-> dict:
        pass
    #actualizar la cantidad de un campo por un id 
    def  updateCantidadById(self,id,catidad,sede)-> dict :
        pass