import { OrdenesEntity,OrdenesDetalladasEntity, ConsumoDetalladoEntity } from "../../Entities/ordenes/ordenesEntity";
import { PedidosEntity } from "../../Entities/pedidos/pedidosEntity";

export abstract class IOrdenes {
    abstract crearOrden(encabezado:OrdenesEntity,pedido:PedidosEntity[]):Promise<OrdenesEntity|null>;
    abstract ordenesToday(sede:string):Promise<OrdenesDetalladasEntity[]|null>;
    abstract consumoDetallado(idorden:string):Promise<ConsumoDetalladoEntity[]|null>;
    abstract getOrdenesBySede(sede:string):Promise<OrdenesDetalladasEntity[]|null>;
  }