import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { Iwallet } from "../../Interfaces/wallet/Iwallet";

/**
 * Clase WalletEspaciosDAO que extiende de Iwallet.
 * Esta clase se encarga de la gestión de la billetera de espacios.
 */
export class WalletEspaciosDAO extends(Iwallet){
    private paths =  new PATHMUNAYSYSY()
    private API=  this.paths.PathAPI()
    private prefijo='Espacios/Wallet'
    private headers={  
         'accept': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('token')}`

    }
    /**
     * Constructor de la clase.
     * Inicializa una nueva instancia de la clase PATHMUNAYSYSY.
     */
    constructor(){
        super();
        console.log("nueva instancia de clientes ")
        this.paths= new PATHMUNAYSYSY()
        
    }
    /**
     * Método para consultar el saldo de la billetera.
     * @param idCliente - El ID del cliente.
     * @returns Number - Promesa que resuelve al saldo de la billetera o un error.
     */
    async consultasaldoWallet(idCliente:number):Promise<number|any>{
        try{ 
            const response =await fetch(`${this.API}${this.prefijo}/consultaSaldo/${idCliente}`,{headers:this.headers,});
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