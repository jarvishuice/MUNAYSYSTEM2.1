import { PagosEntity } from "../../Entities/pagos/pagosEntity";

export abstract class IPagos{
    abstract RegMultipago(pago:PagosEntity):Promise<PagosEntity|null>;
}