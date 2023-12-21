
import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { DetailVisitasEntity, VisitasEntity } from "../../Entities/visistas/visitasEntity";
import { Ivisitas } from "../../Interfaces/visitas/Ivisitas";



/**
 *La clase VisitasDAO es responsable de manejar las solicitudes de la API relacionadas con las visitas. 
 *Incluye métodos para obtener detalles de las visitas, crear nuevas visitas, actualizar el estado de las visitas y filtrar las visitas 
 *según varios criterios.
  *@author jarvis huice 2023-12-11
 
 */
export class VisitasDAO implements  Ivisitas {
    /**
     * 
     * 
     */
    private paths = new PATHMUNAYSYSY();
    private API = this.paths.PathAPI();
    private prefijo = 'Visitas';
    private headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
    };

    constructor() {
        console.log("nueva instancia de clientes ");
        this.paths = new PATHMUNAYSYSY();
    }
    async getVisitasDetailToday(sede: string): Promise<[] | DetailVisitasEntity[]> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/visitas/detail/today/${sede}`, {
                method: 'GET',
                headers: this.headers,
            
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as DetailVisitasEntity[];
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
   async crearVisita(visita: VisitasEntity): Promise<VisitasEntity|null> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/Reg/Visita`, {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify(visita)
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as VisitasEntity;
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
     async salidaVisita(idVisita: string): Promise<boolean> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/salida/${idVisita}`, {
                method: 'PUT',
                headers: this.headers,
              
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                //alert("debug salida visita  "+ data)
                window.location.reload();
                return data as boolean;
            } else if (response.status == 404) {
                alert("No se ha podido conectar con el servidor ");
                return false;
            } else if (response.status == 400) {
                alert(response.text);
                return false;
            } else if (response.status == 422) {
                alert("unprocesable entity");
                return false;
            }if(response.status == 401){
                localStorage.clear()
                window.location.href="/index.html"
                return false
              }
             else {
                throw new Error('Error en la solicitud');
            }
        } catch (error) {
            console.error(error);
            return false;
        }
    }
 async   getAllVisitasDay(sede: string): Promise<[] | VisitasEntity[]> {
    try {
        const response = await fetch(`${this.API}${this.prefijo}/visitasToday/${sede}`, {
            method: 'GET',
            headers: this.headers,
          
        });
        if (response.ok) {
            const data = await response.json();
            console.log(data);
            
            return data as VisitasEntity[];
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

   async  getFilterByMotivoAndSede(motivo: string, sede: string): Promise<[] | VisitasEntity[]> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/visitasByMotivo/${sede}/${motivo}`, {
                method: 'GET',
                headers: this.headers,
              
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as VisitasEntity[];
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
   async getVisitasByStatus(sede: string, status: string): Promise<[] | VisitasEntity[]> {
    try {
        const response = await fetch(`${this.API}${this.prefijo}/visitasBystatus/${sede}/${status}`, {
            method: 'GET',
            headers: this.headers,
          
        });
        if (response.ok) {
            const data = await response.json();
            console.log(data);
            
            return data as VisitasEntity[];
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
    async VisitasActivasToday(sede: string): Promise<[] | DetailVisitasEntity[]> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/visitas/detail/today/${sede}`, {
                method: 'GET',
                headers: this.headers,
            
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                const filtrado= data.filter((e:DetailVisitasEntity) => e.status === 'activa' );
                return filtrado as DetailVisitasEntity[]
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
