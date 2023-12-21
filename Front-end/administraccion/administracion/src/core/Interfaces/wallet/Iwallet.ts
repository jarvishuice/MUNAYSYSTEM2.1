export abstract class Iwallet {
    abstract consultasaldoWallet(idCliente:number):Promise<number>;
    
  }