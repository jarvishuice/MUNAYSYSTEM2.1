import { ClientesEntity } from "../../Entities/clients/clients";


export abstract class IClientes {
    abstract BuscarClientes(nombre: string|any): Promise<ClientesEntity[]>;
    
  }
  