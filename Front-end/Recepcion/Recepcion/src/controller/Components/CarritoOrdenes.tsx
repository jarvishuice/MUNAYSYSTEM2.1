import { useEffect, useState } from "react";

import { WalletDAO } from "../../core/Implements/wallet/walletDAO";
import '../../App.css'

import { DetalleDeudaCliente } from "../../core/Entities/clients/dedudaClientes";

export function CarritoOrdenes(props:any){


//  const sede= localStorage.getItem('sede')??'por favor inicie seccio para poder crear a orden'
  
 //Estado para consultar el wallert
 const[wallet,setWallet] = useState<number>(0);
 useEffect (()=>{
   async function fecthWallet() {
       try {
           const controladorWallet = new WalletDAO();
           const data = await controladorWallet.consultasaldoWallet(props.deudor.idCliente);
           setWallet(data);
         } catch (error) {
           console.error(error);
         }
   }
   fecthWallet();
 },[props.deudor.idCliente]);

 //==============================================================================
 //Estado detalled deuda clientes


 
 //



 return (
        <div className="flex-row-reverse carrito rounded  mt-2" style={{backgroundColor:"#1f2937"}} >
    
        
        <h4 className="d-flex justify-content-between align-items-center mb-2 mt-2">
       <center> <span className="text-md p-2 text-white d-block">{'\t'+props.deudor.nombre}</span></center>
          </h4>
          <h4 className="d-flex justify-content-between align-items-center mb-2">
   
          
          <span className="badge  rounded-pill">CI:{props.deudor.ci}</span>
          <span className="badge  rounded-pill" >WALLET:{wallet.toFixed(2)}$</span>

        </h4>
         <center> <h4 className="d-flex  justify-content-between align-items-center mb-2">
          <span className="badge  align-items-center  rounded-pill">Total:{props.deudor.deuda - props.deudor.abono}$</span>
          </h4></center>
          <ul className="list-group mb-3 scrollCarrito">
       {props.detalles.map((items:DetalleDeudaCliente)=>(
            <li key={items.idOrden+items.producto}  className="list-group-item d-flex justify-content-between lh-sm">
            <div>
           
              <h6 className="my-2 nombreProductoCar">{items.producto}</h6>
          

            </div>
            <div>
            
           
              </div>
              <h6 className="m-3 ml-2 p-2">{"\t"} {items.cantidad}X</h6>
            <h6 className="text-success mt-3">{parseFloat(`${items.total}`).toFixed(2)}$</h6>
            <h6 className="">{items.fechaPedido.slice(0,11)}</h6>
          </li>
          ))}
       
          
         
        </ul>
        <center><div className="list-group-item bg-secondary d-flex justify-content-between">
        <button className="btn  w-100 btn-primary p-2 rounded " onClick ={()=>props.activarModal(true)} > Pagar Deuda</button>
        </div></center>

        
      </div>
    

    )


}