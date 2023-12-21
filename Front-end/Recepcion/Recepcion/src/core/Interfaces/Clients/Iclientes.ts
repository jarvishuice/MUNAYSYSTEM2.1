import { ClientesEntity } from "../../Entities/clients/clients";


export abstract class IClientes {
    abstract BuscarClientes(nombre: string|any): Promise<ClientesEntity[]>;
    abstract CrearCliente(Cliente:ClientesEntity):Promise<ClientesEntity|null>;
    abstract getAllClientes():Promise<ClientesEntity[]|null>;
    abstract updateCliente(cliente:ClientesEntity):Promise<ClientesEntity|null>
  }
  
