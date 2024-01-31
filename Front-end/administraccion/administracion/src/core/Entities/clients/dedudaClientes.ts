/**
 * @interface DeudasClientesEntity
 * @description esta contine todos los datos de las deudas de un cliente 
 */
export interface DeudaClientesEntity {
    idCliente:       number;
    ci:              string;
    nombre:          string;
    cantidadOrdenes: number;
    deuda:           number;
    abono:           number;
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

