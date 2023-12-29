import { useEffect, useState } from "react";
import { ProductosEntity } from "../../core/Entities/productos/productos";
import { ProductosEspaciosDAO } from "../../core/Implements/productos/productosEspaciosDAO";
export function BusquedaProducto(props:any){
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
            const controladorProducto = new ProductosEspaciosDAO();
            const data = await controladorProducto.BuscarProductos(nombre);
            setProductos(data);
          } catch (error) {
            console.error(error);
          }
    }
    fecthProducto();
 },[nombre]);

 const [mostrar,setMostrar] = useState<Boolean>(false);
 const trigger=(gatillo:Boolean)=>{
   setMostrar(gatillo);

 }

 if (productos){productos.map((j)=>(
  j.cantidad=1 //se inicializa la cantidad en uno para que me carge la cantidad en el carrito
 ))}
 else{
console.log("no se encontraron productos")
 }
 

    return (
        <div className=" offset-md-1   mt-2 ">
            <input className=" w-50 me-1" onChange={handleInputChange} key='1' type="search" placeholder="Search" aria-label="Search"/>
        <button className="btn btn-outline-primary " key='2' onClick={()=>{buscarProducto(inputValue),trigger(true)}} type="submit">Buscar</button>
        { mostrar ?(
     <div className="row w-50  bg-primary border-bottom text-white align-content-center overflow-scroll  " >
      
      {productos && productos.map((x) => (
        <center><li key={x.id} onClick={()=>{{props.insertProduct(x),trigger(false)}}}>
     
          {x.nombre}</li></center>

      ))}
      </div>):<div></div>}

        </div>

    )


}
export default BusquedaProducto;