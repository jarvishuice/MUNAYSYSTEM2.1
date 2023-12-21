export interface DeudaClientesEntity {
    idCliente:       number;
    ci:              string;
    nombre:          string;
    cantidadOrdenes: number;
    deuda:           number;
}
export interface DetalleDeudaCliente {
    fechaPedido: string;
    producto:    string;
    cantidad:    number;
    precio:      number;
    total:       string;
    sede:        string;
    idOrden:     string;
}

