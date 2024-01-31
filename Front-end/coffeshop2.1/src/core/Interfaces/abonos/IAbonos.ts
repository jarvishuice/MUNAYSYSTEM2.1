export abstract class IAbonos {
    abstract consultasaldoAbono(idCliente:number,sede:string):Promise<number>;
    
  }