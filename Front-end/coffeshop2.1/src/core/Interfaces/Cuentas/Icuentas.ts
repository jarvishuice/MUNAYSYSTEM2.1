import { CuentasEntity } from "../../Entities/cuentas/cuentasEntity";


export abstract class ICuentas {
    abstract getCuentasBySede(sede: string|any): Promise<CuentasEntity[]>;
    
  }
  