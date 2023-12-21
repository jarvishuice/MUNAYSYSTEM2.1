export interface OrdenesEntity {
    id: string;
    total: number;
    sede: string;
    fechaPedido: string;
    fechaPago: string;
    status: string;
    idCliente: number;
    tipoPago: string;
    idPago: string;
  };

export interface OrdenesDetalladasEntity{
  idOrden: string;
  cliente: string;
  total:   number;
  fecha:   Date;
  hora:    string;
  status:  string;

}
export interface ConsumoDetalladoEntity {
  nombre:   string;
  cantidad: number;
  precio:   number;
  total:    number;
}
