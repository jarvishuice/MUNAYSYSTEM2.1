import { ClientesEntity } from "../../Entities/clients/clients";
import { IClientes } from "../../Interfaces/Clients/Iclientes";
import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";

export class ClientesDAO extends(IClientes){
    private paths =  new PATHMUNAYSYSY()
    private API=  this.paths.PathAPI()
    private prefijo='Clientes'
    private headers={  
         'accept': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('token')}`

    }
    constructor(){
        super();
        console.log("nueva instancia de clientes ")
        this.paths= new PATHMUNAYSYSY()
        
    }
    async BuscarClientes(nombre: string|any): Promise<ClientesEntity[]> {
     try{ 
        const response =await fetch(`${this.API}${this.prefijo}/search/${nombre}`,{headers:this.headers,});
        if (response.ok) {
            const data = await response.json();
            console.log(data)
            return data as ClientesEntity[];
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