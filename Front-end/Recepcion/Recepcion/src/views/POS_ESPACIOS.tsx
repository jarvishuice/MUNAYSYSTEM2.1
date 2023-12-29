import { useState } from "react";
import { ProductosEntity } from "../core/Entities/productos/productos";
import { Carrito } from "../controller/Components/carrito";
import BusquedaProductoEspacios from "../controller/Components/busquedaProductosEspacios";
import { BotoneraCategoriaEspacios } from "../controller/Components/botoneraCategoriaEspacios";
import { ProductosEspacios } from "../controller/Components/productosEspacios";


export function POSESPACIOS(){
  

  //estado para la gestipon de cattegorias
  const [categoria,setCategoria]=useState<string>("cafe")



  let selecionarCaytegoria=(cate:string) =>{
setCategoria(cate)

  }

  //====================================
    



    //estado para insertar prductos  al carrito 
    const [pedidos,setPedidos]=useState<ProductosEntity[]>([])
    const insertarPedidos=(pedidoNew:ProductosEntity)=>{
     const pedidoExiste = pedidos.find(items => items.id === pedidoNew.id);
     if (pedidoExiste){
       const pedidoNuevo = pedidos.map(item=>{
         if(item.id ===pedidoNew.id){
           return {
             ...item,cantidad:item.cantidad + 1
           };
         }
         return item
       });
       setPedidos(pedidoNuevo)
     } else{
       setPedidos([...pedidos,pedidoNew])
     }
   
    };
   
  const incrementoProducto=(item:ProductosEntity)=>{
  
    insertarPedidos(item)


  }



  const descremento = (pedidoNew: ProductosEntity) => {
    const pedidoExiste = pedidos.find(items => items.id === pedidoNew.id);
    if (pedidoExiste) {
      const pedidoNuevo = pedidos.map(item => {
        if (item.id === pedidoNew.id) {
           item.cantidad - 1;
          return {
            ...item,cantidad:item.cantidad -1
          };
        }
        return item;
      }).filter(item => item.cantidad > 0); // Utiliza filter() para eliminar los elementos null
  
      setPedidos(pedidoNuevo);
    } else {
      setPedidos([...pedidos, pedidoNew]);
    }
  };
  
  



//==============================================

return(<>
     
        <main className="main ">
                       <div className="row g-5">
          
            <center><div className="col-md-7 col-lg-8  ">
            <div className=" ">
                <BusquedaProductoEspacios insertProduct={incrementoProducto}  ></BusquedaProductoEspacios></div>
                
            
            <BotoneraCategoriaEspacios  Categoria={selecionarCaytegoria} ></BotoneraCategoriaEspacios></div>
             

            </center>
            <ProductosEspacios categoria={categoria} insertarPedido={insertarPedidos}></ProductosEspacios>
            <div className=" mt-4 col-sm-2 col-md-4 col-lg-4 order-md-reverse"><Carrito pedido={pedidos} aumento={incrementoProducto} descremento={descremento}></Carrito> </div>
        
            </div>
          
        </main>
        </>
    )
    }