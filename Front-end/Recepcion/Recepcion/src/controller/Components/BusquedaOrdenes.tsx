import { useEffect, useState } from "react";
import { ProductosEntity } from "../../core/Entities/productos/productos";
import { ProductosDAO } from "../../core/Implements/productos/productosDAO";
export function BusquedaOrdenes(props:any){
const [inputValue,setInputValue] =useState<String|any>("")
const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

    const [nombre, setNombre] = useState("cafe");
const buscarProducto = (valor: string | any) => {
    setNombre(valor);
  };
 const [productos,setProductos] =useState<ProductosEntity[]|undefined>([]);
 useEffect (()=>{
    async function fecthProducto() {
        try {
            const controladorProducto = new ProductosDAO();
            const data = await controladorProducto.BuscarProductos(nombre);
            setProductos(data);
          } catch (error) {
            console.error(error);
          }
    }
    fecthProducto();
 },[nombre]);



    return (
        <div className=" offset-md-1   mt-2 ">
            <input className=" w-50 me-1" onChange={handleInputChange} key='1' type="search" placeholder="Search" aria-label="Search"/>
        <button className="btn btn-outline-primary " key='2' onClick={()=>{props.productos(productos),buscarProducto(inputValue)}} type="submit">Search</button>


        </div>

    )


}
export default BusquedaOrdenes;