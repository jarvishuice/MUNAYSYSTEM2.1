import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { CuentasEntity } from "../../Entities/cuentas/cuentasEntity";
import { ICuentas } from "../../Interfaces/Cuentas/Icuentas";

/**
 * gestro de las cuentas para realizar pagos 
 * @date 31/1/2024 - 4:19:09 p. m.
 *
 * @export
 * @class CuentasDAO
 * @typedef {CuentasDAO}
 * @implements {ICuentas}
 */
export class CuentasDAO implements ICuentas{
    private paths = new PATHMUNAYSYSY();
    private API = this.paths.PathAPI();
    private prefijo = 'Cuentas';
    private headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
    }; 
   /**
    * extracion de las cuentas segun la sede 
    * @date 31/1/2024 - 4:18:31 p. m.
    *
    * @async
    * @param {String} sede
    * @returns {Promise<CuentasEntity[]>}
    */
   async  getCuentasBySede(sede: any): Promise<CuentasEntity[]> {
     
    try{ 
        const response =await fetch(`${this.API}${this.prefijo}/${sede}`,{headers:this.headers,});
        if (response.ok) {
            const data = await response.json();
            console.log(data)
            return data as CuentasEntity[];
          } if(response.status== 404){
            alert("No se ha podido conectar con el servidor ")
            return [];
          }
          if(response.status== 400){
            alert(response.statusText)
            return [];
          }
          if(response.status == 401){
            localStorage.clear()
            window.location.href="/index.html"
            return []
          }
           else {
            throw new Error('Error en la solicitud');
          }
        } catch (error) {
          console.error(error);
          return [];
        }
     

        
    }
}