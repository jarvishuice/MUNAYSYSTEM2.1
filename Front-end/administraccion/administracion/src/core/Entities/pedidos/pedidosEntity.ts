export interface PedidosEntity {
  idOrden: string;
  idProducto: number;
  cantidad: number;
  total: number;
}
  
export   interface PedidoEspacioEntity {
    idOrden: string;
    idProducto: string;
    cantidad: number;
    total: number;
  }
  