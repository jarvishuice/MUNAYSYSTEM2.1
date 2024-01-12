from pydantic import BaseModel
from typing import Optional

class PagosEntity(BaseModel):
    """
    Esta es la clase PagosEntity que hereda de BaseModel.
    Se utiliza para representar la entidad de pagos en la aplicación.

    Atributos:
    id (str): El identificador del pago.
    fecha (str, opcional): La fecha del pago.
    monto (float): El monto del pago.
    motivo (str): El motivo del pago.
    idcliente (int): El identificador del cliente que realizó el pago.
    idformadepago (int): El identificador de la forma de pago utilizada.
    referencia (str): La referencia del pago.
    idtaza (str, opcional): El identificador de la taza utilizada.
    sede (str, opcional): La sede donde se realizó el pago.
    """
    id:str
    fecha:Optional[str]
    monto:float
    motivo:str
    idcliente:int
    idformadepago:int
    referencia:str
    idtaza:Optional[str]
    sede:Optional[str]

    
class PagosDetailEntity(BaseModel):
    """
    Esta es la clase PagosDetailEntity que hereda de BaseModel.
    Se utiliza para representar los detalles de la entidad de pagos en la aplicación.

    Atributos:
    id (str): El identificador del detalle del pago.
    fecha (str): La fecha del detalle del pago.
    monto (float): El monto del detalle del pago.
    motivo (str): El motivo del detalle del pago.
    cliente (str): El cliente que realizó el detalle del pago.
    formaDepago (str): La forma de pago utilizada en el detalle del pago.
    referencia (str): La referencia del detalle del pago.
    tasa (float): La tasa utilizada en el detalle del pago.
    sede (str): La sede donde se realizó el detalle del pago.
    idcliente (int): El identificador del cliente que realizó el pago.
    idformadepago (int): El identificador de la forma de pago utilizada.
    """

    id:str
    fecha:str
    monto:float
    motivo:str
    cliente:str
    formaDepago:str
    referencia:str
    tasa:float
    sede:str
    idcliente:int
    idformadepago:int
