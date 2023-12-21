
import { useEffect, useState } from 'react';
import producto from '../../assets/producto.png'
import { ProductosEntity } from '../../core/Entities/productos/productos'
import { ProductosDAO } from '../../core/Implements/productos/productosDAO';
const sede = localStorage.getItem('sede')??'inicie seccio por favor '
export function Productos(props:any){








//estado de productos  by categoria
const[productos,setProductos]= useState<ProductosEntity[]>([])
useEffect (()=>{
  async function fecthProducto(categoria:string) {
      try {

          const controladorProducto = new ProductosDAO();
          const data = await controladorProducto.ProductosByCategoriaandSede(categoria,sede);
          //insertarItems(data);
          setProductos(data)

        } catch (error) {
          console.error(error);
        }
  }
  fecthProducto(props.categoria);
},[props.categoria]);




///









return (

  <div className="container-fluid  vh-10 col-sm-4 col-md-7 col-sx-8 col-lg-7 m-0 mt-1 vh-100 ">
    <div className="row p-3 scrollable" >
  {productos.map((items:ProductosEntity|any)=>{
     {items.cantidad=1}{/** cantida se seta a 1 para que no altere el resto de la vista porque se trae el inventario completo */}
     return <div className="col-md-4"  key={items.id}>
     
        <div className="card"  onClick={()=>props.insertarPedido(items)}>
       <center>   <img src={items.urlimagen??producto} className="card-img-top rounded "  alt="Imagen"/></center>
          <div className="card-body">
            <h5 className="card-title">{items.precio}$</h5>
            <p className="nombreProducto">{items.nombre}.</p>
          </div>
        </div>
      </div>})??<h2></h2>}
     
    </div>
  </div>

    );
}