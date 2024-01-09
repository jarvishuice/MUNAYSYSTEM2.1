import { useEffect, useState } from "react";
import { WalletDAO } from "../../core/Implements/wallet/walletDAO";
import { DetalleDeudaCliente } from "../../core/Entities/clients/dedudaClientes";
import { DeudasClientesEspaciosDAO } from "../../core/Implements/clients/deudasClientesEspaciosDAO";

export function DetallesDeudasEspacios(props:any){
const sede:string = localStorage.getItem('sede')??"inicie seccion" ;
/**
 * Consulta del wallet 
 */
    const [wallet,setWallet] = useState<number>(0)
useEffect (()=>{
    async function fecthWallet() {
        try {
            const controladorWallet = new WalletDAO();
            const data = await controladorWallet.consultasaldoWallet((props.deudor.idCliente).replace(/['"]+/g, ''));
            setWallet(data);
          } catch (error) {
            console.error(error);
          }
    }
    fecthWallet();
  },[]);


/**
 * dettallesDeudas
 */
const [detalles,setDetalles]=useState<DetalleDeudaCliente[]>([{fechaPedido:" ",producto:" ",cantidad:0,precio:0,total:'1',sede:sede,idOrden:"3333"},])

async function DETALLESDEUDAS(idCliente:number) {
  try {
    const controladorDeudas = new DeudasClientesEspaciosDAO();
    const data = await controladorDeudas.DetalleDeudaClientes(sede, idCliente);
    setDetalles(data);
    alert( "id cliente DEtalles"+ idCliente)

    console.log(data);
  } catch (error) {
    console.error(error);
  }
  
}
useEffect(()=>{
    DETALLESDEUDAS(props.deudor.idCliente);
    alert(typeof(props.deudor.idCliente))
},[])

return( <div className="flex-row-reverse carrito rounded  mt-2" style={{backgroundColor:"#1f2937"}} >
    
        
<h4 className="d-flex justify-content-between align-items-center mb-2 mt-2">
<center> <span className="text-md p-2 text-white d-block">{'\t'+props.deudor.nombre}</span></center>
  </h4>
  <h4 className="d-flex justify-content-between align-items-center mb-2">

  
  <span className="badge  rounded-pill">CI:{props.deudor.ci}</span>
  <span className="badge  rounded-pill" >WALLET:{wallet.toFixed(2)}$</span>

</h4>
 <center> <h4 className="d-flex  justify-content-between align-items-center mb-2">
  <span className="badge  align-items-center  rounded-pill">Total:{props.deudor.deuda}$</span>
  </h4></center>
  <ul className="list-group mb-3 scrollCarrito">
{detalles.map((items:DetalleDeudaCliente)=>(
    <li key={items.idOrden+items.producto}  className="list-group-item d-flex justify-content-between lh-sm">
    <div>
   
      <h6 className="my-2 nombreProductoCar">{items.producto}</h6>
  
      </div>
      <h6 className="m-3 ml-2 p-2">{"\t"} {items.cantidad}X</h6>
    <h6 className="text-success mt-3">{parseFloat(`${items.total}`).toFixed(2)}$</h6>
    <h6 className="">{items.fechaPedido.slice(0,11)}</h6>
  </li>
  ))}

  
 
</ul>



</div>


)

}