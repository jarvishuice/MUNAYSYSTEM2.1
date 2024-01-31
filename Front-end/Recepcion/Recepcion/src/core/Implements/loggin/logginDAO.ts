import { PATHMUNAYSYSY } from "../../../Config/routes/pathsMuanaysys";
import { UsersEntity } from "../../Entities/users/userEntity";
import { Iloggin } from "../../Interfaces/Loggin/Ilogin";

/**
 * Description placeholder
 * @date 31/1/2024 - 4:21:06 p. m.
 *
 * @export
 * @class logginDAO
 * @typedef {logginDAO}
 * @implements {Iloggin}
 */
export class logginDAO implements Iloggin{
    private paths = new PATHMUNAYSYSY();
    private API = this.paths.PathAPI();
    private prefijo = 'Loggin';
    private headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
    };
/**
 * Cierre de seccion
 * @date 31/1/2024 - 4:20:52 p. m.
 *
 * @async
 * @param {UsersEntity} user
 * @returns {Promise<boolean>}
 */
async logout(user: UsersEntity): Promise<boolean> {
   
    console.log(localStorage.getItem('user'));
    try {
        const response = await fetch(`${this.API}${this.prefijo}/logout`, {
            method: 'POST',
            headers: this.headers,
            body:JSON.stringify(user)
        });
        if (response.ok) {
            const data = await response.json();
            console.log(data);
            localStorage.clear();
        
            alert('ha cerrado seccion de manetra correcta !!!')
            window.location.href="http://191.97.17.26:8050/index.html"
            return data as boolean;
        } else if (response.status == 404) {
            alert("No se ha podido conectar con el servidor ");
            return false;
        } else if (response.status == 400) {
            alert(response.statusText);
            return false;
        } else if (response.status == 422) {
            alert("unprocesable entity");
            return false;
        } else {
            throw new Error('Error en la solicitud');
        }
    } catch (error) {
        console.error(error);
        return false;
    }
}



}