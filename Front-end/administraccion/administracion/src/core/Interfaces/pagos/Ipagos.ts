import { PagosEntity, PagosDetailEntity } from "../../Entities/pagos/pagosEntity";
/**
 * Clase abstracta IPagos.
 */
export abstract class IPagos{
    /**
     * Método abstracto para registrar múltiples pagos.
     * @param {PagosEntity} pago - La entidad de pago.
     * @returns {Promise<PagosEntity|null>} - Retorna una promesa con la entidad de pago o null.
     */
    abstract RegMultipago(pago:PagosEntity):Promise<PagosEntity|null>;

    /**
     * Método abstracto para obtener todos los detalles de pago.
     * @returns {Promise<PagosDetailEntity[]|null>} - Retorna una promesa con un array de los detalles de pago o null.
     */
    abstract getAllPayDetail():Promise<PagosDetailEntity[]|null>;
    /**
     * Método abstracto para editar un pago.
     * @param {PagosEntity} pago - La entidad de pago.
     * @returns {Promise<Boolean>} - Retorna una promesa con un valor booleano.
     */
    abstract editPay(pago:PagosEntity):Promise<Boolean>;
}