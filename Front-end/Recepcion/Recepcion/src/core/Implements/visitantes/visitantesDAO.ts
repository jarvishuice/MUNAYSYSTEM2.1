import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { ClientesEntity } from "../../Entities/clients/clients";
import { IVisitantes } from "../../Interfaces/visitas/Ivisitantes";

export  class VisitantesDAO implements IVisitantes{
    private paths = new PATHMUNAYSYSY();
    private API = this.paths.PathAPI();
    private prefijo = 'Visitas';
    private headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
    };


   async crearVisitante(visitante: ClientesEntity): Promise<ClientesEntity | null> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/`, {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify(visitante)
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as ClientesEntity;
            } else if (response.status == 404) {
                alert("No se ha podido conectar con el servidor ");
                return null;
            } else if (response.status == 400) {
                alert(response.statusText);
                return null;
            } else if (response.status == 422) {
                alert("unprocesable entity");
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
  async   buscarVisitante(ci: string): Promise<[] | ClientesEntity[]> {
    try {
        const response = await fetch(`${this.API}${this.prefijo}/search/${ci}`, {
            method: 'GET',
            headers: this.headers,
          
        });
        if (response.ok) {
            const data = await response.json();
            console.log(data);
            
            return data as ClientesEntity[];
        } else if (response.status == 404) {
            alert("No se ha podido conectar con el servidor ");
            return [];
        } else if (response.status == 400) {
            alert(response.statusText);
            return [];
        } else if (response.status == 422) {
            alert("unprocesable entity");
            return [];
        }if(response.status == 401){
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
   async getAllVisitante(): Promise<[] | ClientesEntity[]> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/getAll/Visitantes`, {
                method: 'GET',
                headers: this.headers,
              
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as ClientesEntity[];
            } else if (response.status == 404) {
                alert("No se ha podido conectar con el servidor ");
                return [];
            } else if (response.status == 400) {
                alert(response.statusText);
                return [];
            } else if (response.status == 422) {
                alert("unprocesable entity");
                return [];
            }if(response.status == 401){
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