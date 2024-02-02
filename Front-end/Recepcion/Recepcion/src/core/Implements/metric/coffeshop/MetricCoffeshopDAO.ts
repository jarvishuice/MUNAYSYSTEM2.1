import { MetricCoffeshopEntity } from "../../../Entities/metric/coffeshop/MetricCoffeshopEntity";

import { PATHMUNAYSYSY } from "../../../../Config/routes/pathsMuanaysys";

import { IMetricCoffeshop } from "../../../Interfaces/metric/coffeshop/IMetricCoffeshop";


/**
 * Description placeholder
 * @date 31/1/2024 - 4:33:07 p. m.
 *
 * @export
 * @class MetricCoffeshopDAO
 * @typedef {MetricCoffeshopDAO}
 * @implements {IMetricCoffeshop}
 */
export class MetricCoffeshopDAO implemMnts IMetricCoffeshop{
    private paths =  new PATHMUNAYSYSY()
    private API=  this.paths.PathAPI()
    private prefijo='metric/coffeshop'
    private headers={  
         'accept': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('token')}`

    }
    constructor(){
      console.log("nueva instancia de clientes ");
      this.paths = new PATHMUNAYSYSY();
    }
    /**
     * metricas por sede
     * @date 31/1/2024 - 4:22:04 p. m.
     *
     * @async
     * @param {string} sede
     * @returns {Promise<MetricCoffeshopEntity|null>}
     */
    async ExtraerMetricasBySede(sede:string): Promise<MetricCoffeshopEntity|null> {
        try{ 
            const response =await fetch(`${this.API}${this.prefijo}/${sede}`,{headers:this.headers,});
            if (response.ok) {
                const data = await response.json();
                console.log(data)
                return data as MetricCoffeshopEntity
              } if(response.status== 404){
                alert("No se ha podido conectar con el servidor ")
                return null;
              }
              if(response.status== 400){
                alert(response.statusText)
                return null;
              }if(response.status == 401){
                localStorage.clear()
                window.location.href="/index.html"
                return null
              }
               else {
                throw new Error('Error en la solicitud');
              }
            } catch (error) {
              console.error(error);
              return null;
            }
       
   }

   /**
    * Metricas en general 
    * @date 31/1/2024 - 4:22:25 p. m.
    *
    * @async
    * @returns {Promise<MetricCoffeshopEntity|null>}
    */
   async ExtraerMetricasGlobales(): Promise<MetricCoffeshopEntity|null> {
    try{ 
        const response =await fetch(`${this.API}${this.prefijo}/global`,{headers:this.headers,});
        if (response.ok) {
            const data = await response.json();
            console.log(data)
            return data as MetricCoffeshopEntity
          } if(response.status== 404){
            alert("No se ha podido conectar con el servidor ")
            return null;
          }
          if(response.status== 400){
            alert(response.statusText)
            return null;
          }if(response.status == 401){
            localStorage.clear()
            window.location.href="/index.html"
            return null
          }
           else {
            throw new Error('Error en la solicitud');
          }
        } catch (error) {
          console.error(error);
          return null;
        }
   
}



}