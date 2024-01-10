import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { DetalleDeudaCliente, DeudaClientesEntity } from "../../Entities/clients/dedudaClientes";
import { PagosEntity } from "../../Entities/pagos/pagosEntity";
import { IDeudasCLientes } from "../../Interfaces/Clients/IdeudaClientes";

export class DeudasClientesEspaciosDAO implements IDeudasCLientes{
    private paths =  new PATHMUNAYSYSY()
    private API=  this.paths.PathAPI()
    private prefijo='Espacios'
    private headers={  
         'accept': 'application/json',
         'Content-Type': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('token')}`
    
    }
    constructor(){
        
        console.log("nueva instancia de clientes ")
        this.paths= new PATHMUNAYSYSY()
        
    } 
    
   async  DeudasClientesBysede(sede: string|null): Promise<DeudaClientesEntity[]> {

        try{ 
            const response =await fetch(`${this.API}${this.prefijo}/deudas/Deudas/${sede}`,{headers:this.headers,});
            if (response.ok) {
                const data = await response.json();
                console.log(data)
                return data as DeudaClientesEntity[];
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
         
    };
    async DetalleDeudaClientes(sede: string, idCliente: number): Promise<DetalleDeudaCliente[]> {
      try{ 
        const response =await fetch(`${this.API}${this.prefijo}/deudas/Deudas/${sede}/${idCliente}`,{headers:this.headers,});
        if (response.ok) {
            const data = await response.json();
            console.log(data)
            return data as DetalleDeudaCliente[];
          } if(response.status== 404){
            alert("No se ha podido conectar con el servidor ")
            return [];
          }
          if(response.status== 400){
            alert(response.text)
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




  };
  async SaldarDeudaClientes(Rwallet: number, Dwallet: number, pago: PagosEntity): Promise<PagosEntity|null> {
    try{ 
      const response =await fetch(`${this.API}${this.prefijo}/deudas/Deudas/cerrarDeudas/${Rwallet}/${Dwallet}`,{  method: 'PUT',
      headers: this.headers,
      body: JSON.stringify(pago)});
      if (response.ok) {
          const data = await response.json();
          console.log(data)
          return data as PagosEntity;
        } if(response.status== 404){
          alert("No se ha podido conectar con el servidor ")
          return null;
        }
        if(response.status== 400){
          alert(response.text)
          return null;
        }
        if(response.status == 401){
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