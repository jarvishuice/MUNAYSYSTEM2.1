import { OrdenesEntity,OrdenesDetalladasEntity, ConsumoDetalladoEntity } from "../../Entities/ordenes/ordenesEntity";
import { PedidosEntity } from "../../Entities/pedidos/pedidosEntity";

export abstract class IOrdenes {
  /**
       * Creates an order.
       * @param encabezado - The header information for the order.
       * @param pedido - An array of order items.
       * @returns A promise that resolves to an `OrdenesEntity` object representing the created order or `null` if the order creation fails.
       */
    abstract crearOrden(encabezado:OrdenesEntity,pedido:PedidosEntity[]):Promise<OrdenesEntity|null>;

    
   /**
       * Retrieves orders placed today at a specific location.
       * @param sede - The location to retrieve orders from.
       * @returns A promise that resolves to an array of `OrdenesDetalladasEntity` objects representing the orders placed today at the specified location or `null` if there are no orders.
       */
    abstract ordenesToday(sede:string):Promise<OrdenesDetalladasEntity[]|null>;
    /**
       * Retrieves detailed consumption information for a specific order.
       * @param idorden - The ID of the order to retrieve consumption information for.
       * @returns A promise that resolves to an array of `ConsumoDetalladoEntity` objects representing the detailed consumption information for the specified order or `null` if the order is not found.
       */
    abstract consumoDetallado(idorden:string):Promise<ConsumoDetalladoEntity[]|null>;
     /**
     * Abstract method to delete an order.
     * 
     * @param idOrden - The ID of the order to be deleted.
     * @returns A Promise that resolves to a boolean value indicating whether the deletion was successful or not.
     */
    abstract getOrdenesBySede(sede:string):Promise<OrdenesDetalladasEntity[]|null>;
     /**
     * Abstract method to delete an order.
     * 
     * @param idOrden - The ID of the order to be deleted.
     * @returns A Promise that resolves to a boolean value indicating whether the deletion was successful or not.
     */
    abstract deleteOrden(idOrden:string):Promise<boolean>;
  }