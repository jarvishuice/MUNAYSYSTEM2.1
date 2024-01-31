
/**
 * Description placeholder
 * @date 31/1/2024 - 2:13:37 p. m.
 *
 * @export
 * @interface DeudaClientesEntity
 * @typedef {DeudaClientesEntity}
 */
export interface DeudaClientesEntity {
    idCliente:       number;
    ci:              string;
    nombre:          string;
    cantidadOrdenes: number;
    deuda:           number;
    abono:           number;
}
/**
 * Description placeholder
 * @date 31/1/2024 - 2:16:21 p. m.
 *
 * @export
 * @interface DetalleDeudaCliente
 * @typedef {DetalleDeudaCliente}
 */
export interface DetalleDeudaCliente {
    fechaPedido: string;
    producto:    string;
    cantidad:    number;
    precio:      number;
    total:       string;
    sede:        string;
    idOrden:     string;
}

