import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { IAbonos } from "../../Interfaces/abonos/IAbonos"

/**
 * gestiona las operaciones de abomnos entre e l usuario y el api 
 * @date 31/1/2024 - 3:32:26 p. m.
 *
 * @export
 * @class AbonosDAO
 * @typedef {AbonosDAO}
 * @extends {(IAbonos)}
 */
export class AbonosDAO extends(IAbonos){
    private sede = localStorage.getItem("sede")?? "inicia seccion"
    private paths =  new PATHMUNAYSYSY()
    private API=  this.paths.PathAPI()
    private prefijo='Abonos'
    private headers={  
         'accept': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('token')}`

    }
    constructor(){
        super();
        console.log("nueva instancia de clientes ")
        this.paths= new PATHMUNAYSYSY()
        
    }
    async consultasaldoAbono(idCliente:number):Promise<number|any>{
        try{ 
            const response =await fetch(`${this.API}${this.prefijo}/${idCliente}/${this.sede}`,{headers:this.headers,});
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
              }
              if(response.status == 401){
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