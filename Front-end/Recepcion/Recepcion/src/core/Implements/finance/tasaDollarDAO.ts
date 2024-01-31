import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { ItasaDollar } from "../../Interfaces/finance/ItasaDollar";

/**
 * gestioon de tasas del BCV
 * @date 31/1/2024 - 4:20:18 p. m.
 *
 * @export
 * @class TasaDollarDAO
 * @typedef {TasaDollarDAO}
 * @implements {ItasaDollar}
 */
export class TasaDollarDAO implements ItasaDollar{
    private paths =  new PATHMUNAYSYSY()
    private API=  this.paths.PathAPI()
    private prefijo='finance/tasaDollarLast'
    private headers={  
         'accept': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('token')}`

    }

    /**
     * obtine la tas actual del BCV  proporcionada por el api 
     * @date 31/1/2024 - 4:19:49 p. m.
     *
     * @async
     * @returns {Promise<number>}
     */
    async ObtenerTazaActual(): Promise<number> {
        try{ 
            const response =await fetch(`${this.API}${this.prefijo}/`,{headers:this.headers,});
            if (response.ok) {
                const data = await response.json();
                console.log(data)
                return data
              } if(response.status== 404){
                alert("No se ha podido conectar con el servidor ")
                return 0;
              }
              if(response.status== 400){
                alert(response.statusText)
                return 0;
              }if(response.status == 401){
                localStorage.clear()
                window.location.href="/index.html"
                return 0
              }
               else {
                throw new Error('Error en la solicitud');
              }
            } catch (error) {
              console.error(error);
              return 0;
            }
       
   }



}