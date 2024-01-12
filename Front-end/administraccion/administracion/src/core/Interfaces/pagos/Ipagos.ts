import { PagosEntity, PagosDetailEntity } from "../../Entities/pagos/pagosEntity";

export abstract class IPagos{
    abstract RegMultipago(pago:PagosEntity):Promise<PagosEntity|null>;
    abstract getAllPayDetail(sede:String):Promise<PagosDetailEntity|null>;
}