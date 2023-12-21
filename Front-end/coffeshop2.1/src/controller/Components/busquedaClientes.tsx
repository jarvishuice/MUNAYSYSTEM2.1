import { useEffect, useState } from "react";
import { ClientesEntity } from "../../core/Entities/clients/clients";
import { ClientesDAO } from "../../core/Implements/clients/clientesDAO";
export function BusquedaClientes(){
const [inputValue,setInputValue] =useState("")
const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

    const [nombre, setNombre] = useState("contado");
const buscarCliente = (valor: string | any) => {
    setNombre(valor);
  };
 const [clientes,setClientes] =useState<ClientesEntity[]|undefined>(undefined);
 useEffect (()=>{
    async function fecthCliente() {
        try {
            const controladorClientes = new ClientesDAO();
            const data = await controladorClientes.BuscarClientes(nombre);
            setClientes(data);
          } catch (error) {
            console.error(error);
          }
    }
    fecthCliente();
 },[nombre]);
 const [mostrar,setMostrar] = useState<Boolean>(false);
  const trigger=(gatillo:Boolean)=>{
    setMostrar(gatillo);

  }

    return (
        <div>
             <input type="text" onChange={handleInputChange} value={inputValue} />
      <button  onClick={()=>{buscarCliente(inputValue);trigger(true)}}>Search</button>
        <div> 
        { mostrar ?(
      <center><div className="row w-100  align-content-center overflow-scroll  " >
      
      {clientes && clientes.map((x) => (
        <center><li key={x.id} onClick={()=>{trigger(false);}}><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="whithe" className="bi bi-person-fill-add mr-2" viewBox="0 0 16 16">
        <path d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm.5-5v1h1a.5.5 0 0 1 0 1h-1v1a.5.5 0 0 1-1 0v-1h-1a.5.5 0 0 1 0-1h1v-1a.5.5 0 0 1 1 0Zm-2-6a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
        <path d="M2 13c0 1 1 1 1 1h5.256A4.493 4.493 0 0 1 8 12.5a4.49 4.49 0 0 1 1.544-3.393C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4Z"/>
      </svg>
          {x.nombre}</li></center>

      ))}
      </div></center>):<div></div>}
        </div>
        

        </div>

    )


}
export default BusquedaClientes;