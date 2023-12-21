from pydantic import BaseModel
from typing import Optional


class VisitasEntity(BaseModel):
    """
    Represents a visit entity.

    Args:
        id (Optional[str]): The ID of the visit.
        idVisitante (int): The ID of the visitor.
        idCliente (int): The ID of the client.
        fIngreso (Optional[str]): The date and time of entry.
        fSalida (Optional[str]): The date and time of exit.
        status (str): The status of the visit.
        sede (str): The location of the visit.
        motivo (str): The reason for the visit.
    """
    id: Optional[str]
    idVisitante: int
    idCliente: int
    fIngreso: Optional[str]
    fSalida: Optional[str]
    status: str
    sede: str
    motivo: str


class DetailVisitasEntity(BaseModel):
    """
    Represents a detailed visit entity.

    Args:
        id (Optional[str]): The ID of the visit.
        visitante (str): The visitor's name.
        correo (str): The visitor's email.
        ci (str): The visitor's identification number.
        cliente (str): The client's name.
        fIngreso (Optional[str]): The date and time of entry.
        fSalida (Optional[str]): The date and time of exit.
        status (str): The status of the visit.
        sede (str): The location of the visit.
        motivo (str): The reason for the visit.
    """
    id: Optional[str]
    visitante: str
    correo: str
    ci: str
    cliente: str
    fIngreso: Optional[str]
    fSalida: Optional[str]
    status: str
    sede: str
    motivo: str