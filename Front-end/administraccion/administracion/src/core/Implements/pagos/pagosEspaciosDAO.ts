import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { PagosEntity,PagosDetailEntity } from "../../Entities/pagos/pagosEntity";
import { IPagos } from "../../Interfaces/pagos/Ipagos";

export class PagosEspaciosDAO implements IPagos{
    private paths = new PATHMUNAYSYSY();
    private API = this.paths.PathAPI();
    private prefijo = 'Espacios/Pagos';
    private sede = "ddd ";
    private headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
    };
    constructor() {
        console.log("nueva instancia de clientes ");
        this.paths = new PATHMUNAYSYSY();
        this.sede = localStorage.getItem("sede") ?? "ingresa tu sede"
    }

 
    async RegMultipago(pago: PagosEntity): Promise<PagosEntity|null> {
        
        console.log(pago);
        try {
            const response = await fetch(`${this.API}${this.prefijo}/MultiPago`, {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify(pago)
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as PagosEntity;
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


    /**
     * Método para obtener todos los detalles de pago.
     * @returns {Promise<PagosDetailEntity[]|null>} - Retorna una promesa con un array de los detalles de pago o null.
     * 
     */
    async getAllPayDetail(): Promise<PagosDetailEntity[] | null> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/details/sede/${this.sede}`, {
                method: 'GET',
                headers: this.headers,

            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);

                return data as PagosDetailEntity[];
            } else if (response.status == 404) {
                alert("No se ha podido conectar con el servidor ");
                return null;
            } else if (response.status == 400) {
                alert(response.statusText);
                return null;
            } else if (response.status == 422) {
                alert("unprocesable entity");
                return null;
            } if (response.status == 401) {
                localStorage.clear()
                window.location.href = "/index.html"
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

    async editPay(pago: PagosEntity): Promise<Boolean> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/edit/`, {
                method: 'PUT',
                headers: this.headers,
                body:JSON.stringify(pago),

            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);

                return data as Boolean;
            } else if (response.status == 404) {
                alert("No se ha podido conectar con el servidor ");
                return false;
            } else if (response.status == 400) {
                alert(response.statusText);
                return false;
            } else if (response.status == 422) {
                alert("unprocesable entity");
                return false;
            } if (response.status == 401) {
                localStorage.clear()
                window.location.href = "/index.html"
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
        
    
}