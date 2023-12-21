import { DetalleDeudaCliente, DeudaClientesEntity } from "../../Entities/clients/dedudaClientes";
import { PagosEntity } from "../../Entities/pagos/pagosEntity";



export abstract class IDeudasCLientes {
    abstract DeudasClientesBysede(sede: string): Promise<DeudaClientesEntity[]>;
    abstract DetalleDeudaClientes(sede:string,idCliente:number):Promise<DetalleDeudaCliente[]>;
    /** 
     * Este metodo se encarga de paragar todas la deuda de un cliente ddo 
     * La i informacion del client y la sede viene dado por el parametro  @param pagos el cual es un pago entity definido en entities en nuestro core 
     *  
     *  @param Rwallet=Es el monto a recargar en el wallet 
     * @param Dwallet=Monto  a decontarb del wallet
     */
    abstract SaldarDeudaClientes(Rwallet:number,Dwallet:number,pago:PagosEntity):Promise<PagosEntity|null>;
  }