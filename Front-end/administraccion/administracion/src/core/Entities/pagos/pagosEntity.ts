/**
 * @typedef {Object} PagosEntity
 * @property {string} id - Identificador único del pago
 * @property {string} fecha - Fecha del pago
 * @property {number} monto - Monto del pago
 * @property {string} motivo - Motivo del pago
 * @property {number} idcliente - Identificador único del cliente
 * @property {number} idformadepago - Identificador único de la forma de pago
 * @property {string} referencia - Referencia del pago
 * @property {string} idtaza - Identificador único de la taza
 * @property {string} sede - Sede del pago
 */
export interface PagosEntity {
    id:            string;
    fecha:         string;
    monto:         number;
    motivo:        string;
    idcliente:     number;
    idformadepago: number;
    referencia:    string;
    idtaza:        string;
    sede:          string;
}

/**
 * @typedef {Object} PagosDetailEntity
 * @property {string} id - Identificador único del detalle del pago
 * @property {string} fecha - Fecha del detalle del pago
 * @property {number} monto - Monto del detalle del pago
 * @property {string} motivo - Motivo del detalle del pago
 * @property {string} cliente - Cliente del detalle del pago
 * @property {string} formaDepago - Forma de pago del detalle del pago
 * @property {string} referencia - Referencia del detalle del pago
 * @property {number} tasa - Tasa del detalle del pago
 * @property {string} sede - Sede del detalle del pago
 * @property {number} idcliente - Identificador único del cliente del detalle del pago
 * @property {number} idformadepago - Identificador único de la forma de pago del detalle del pago
 */
export interface PagosDetailEntity {
    id:            string;
    fecha:         string;
    monto:         number;
    motivo:        string;
    cliente:       string;
    formaDepago:   string;
    referencia:    string;
    tasa:          number;
    sede:          string;
    idcliente:     number;
    idformadepago: number;
}
