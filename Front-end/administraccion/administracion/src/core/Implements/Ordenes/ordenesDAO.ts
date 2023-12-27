import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { ConsumoDetalladoEntity, OrdenesDetalladasEntity, OrdenesEntity } from "../../Entities/ordenes/ordenesEntity";
import { PedidosEntity } from "../../Entities/pedidos/pedidosEntity";
import { IOrdenes } from "../../Interfaces/ordenes/Iordenes";

export class OrdenesDAO implements IOrdenes {
    private paths = new PATHMUNAYSYSY();
    private API = this.paths.PathAPI();
    private prefijo = 'ordenes';
    private headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
    };

    constructor() {
        console.log("nueva instancia de clientes ");
        this.paths = new PATHMUNAYSYSY();
    }

    async crearOrden(encabezado: OrdenesEntity, items: PedidosEntity[]): Promise<OrdenesEntity | null> {
        const data = {
            ordenData:encabezado,
            pedido:items
        };
        console.log(data);
        try {
            const response = await fetch(`${this.API}${this.prefijo}/`, {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify(data)
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as OrdenesEntity;
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
    async ordenesToday(sede: string): Promise<OrdenesDetalladasEntity[] | null> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/today/${sede}`, {
                method: 'POST',
                headers: this.headers,
              
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as OrdenesDetalladasEntity[];
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
    async consumoDetallado(idorden: string): Promise<ConsumoDetalladoEntity[] | null> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/DETALLE/${idorden}`, {
                method: 'POST',
                headers: this.headers,
              
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as ConsumoDetalladoEntity[];
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
     async getOrdenesBySede(sede: string): Promise<OrdenesDetalladasEntity[] | null> {
        try {
            const response = await fetch(`${this.API}${this.prefijo}/filter/${sede}`, {
                method: 'POST',
                headers: this.headers,
              
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data);
                
                return data as OrdenesDetalladasEntity[];
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
}
