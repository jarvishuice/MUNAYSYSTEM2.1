from pydantic import BaseModel
from typing import Optional, List

class OrdenesAbiertas(BaseModel):
    idOrden: str
    cliente: str
    total: float
    fecha: str
    hora: str

class VentasPorClientes(BaseModel):
    total: float
    cliente: str

class DetallesPedidos(BaseModel):
    idOrden: str
    cliente: str
    producto: str
    cantidad: float
    total: float
    fecha: str
    hora: str

class DetallePagos(BaseModel):
    cliente: str
    monto: float
    cotizacion: float
    motivo: str
    referencia: str
    fecha: str
    hora: str
    banco: str
    metodo: str

class PuntoCount(BaseModel):
    cantidad: int
    monto: float

class WalletDisponibles(BaseModel):
    idCliente: int
    cliente: str
    total: float

class DeudaCliente(BaseModel):
    cliente: str
    deuda: float

class VentasPorProducto(BaseModel):
    producto: str
    cantidad: float
    total: float

class ReporteCoffeshopEntity(BaseModel):
    ordenesAbiertas: Optional[List[OrdenesAbiertas]]
    puntoCount: Optional[List[PuntoCount]]
    ventasPorCliente:Optional [List[VentasPorClientes]]
    detallePedidos: Optional[List[DetallesPedidos]]
    detallePagos: Optional[List[DetallePagos]]
    walletDisponibles: Optional[List[WalletDisponibles]]
    ordenesAbiertasHistoricas: Optional[List[OrdenesAbiertas]]
    deudaCliente: Optional[List[DeudaCliente]]
    ventasPorProductos: Optional[List[VentasPorProducto]]
