import { useEffect, useState } from "react";
import { ClientesEntity } from "../../core/Entities/clients/clients";
import { ClientesDAO } from "../../core/Implements/clients/clientesDAO";
import { ProductosEntity } from "../../core/Entities/productos/productos";
import { PedidosEntity } from "../../core/Entities/pedidos/pedidosEntity";
import { WalletDAO } from "../../core/Implements/wallet/walletDAO";
import '../../App.css';
import { OrdenesEntity } from "../../core/Entities/ordenes/ordenesEntity";
import { OrdenesEspaciosDAO } from "../../core/Implements/Ordenes/OrdenesEspaciosDAO";
export function CarritoEspacios(props:any){


  const sede= localStorage.getItem('sede')??'por favor inicie seccio para poder crear a orden'
 //Estado para buscar clientes 
  const [inputValue,setInputValue] =useState("")
  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      setInputValue(event.target.value);
    };
  
      const [nombre, setNombre] = useState("contado");
  const buscarCliente = (valor: string | any) => {
      setNombre(valor);
    };
   const [clientes,setClientes] =useState<ClientesEntity[]>([]);
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
 //====================================================================================   
 //estado seleccion cliente
 const [cliente,setCliente]=useState<ClientesEntity>({
  "id": 8,
  "nombre": "seleccione un cliente",
  "apellido": "",
  "correo": "clientecontado@gmail.com",
  "tlf": "",
  "fechaingreso": "2022-10-25 14:39:01",
  "fechacambio": null,
  "codigo": null,
  "credito": null,
  "ci": "10000002",
  "identificacion": "",
  "direccion": "Caracas null",
  "deuda": null
}
  )
  const seleccionarCliente=(client:ClientesEntity)=>{
    setCliente(client)
    alert(`ha selecciondao al cliente ${client.nombre}`)
  }
 //====================================================================================
   
 //calculo del total 
let total =0
 props.pedido.map((items:ProductosEntity)=>(
  total +=items.precio *  items.cantidad
 ))
 //===================================================================================
 //consulta salod wallet 
const[wallet,setWallet] = useState<number>(0);
useEffect (()=>{
  async function fecthWallet() {
      try {
          const controladorWallet = new WalletDAO();
          const data = await controladorWallet.consultasaldoWallet(cliente.id);
          setWallet(data);
        } catch (error) {
          console.error(error);
        }
  }
  fecthWallet();
},[cliente.id]);



 //=======================================================================================


 // estado para registrar Ordenes
async function crearOrden (ordenData:OrdenesEntity,pedido:PedidosEntity[]){
  try {
    const controladorOrdenes = new OrdenesEspaciosDAO();
    const data = await controladorOrdenes.crearOrden(ordenData,pedido);
    if (data != null ){
      if(data.status ==='pagado'){
      alert( `Orden creada y pagada con el wallet  bajo el # ${data.id} `);
        window.location.reload()
      }
      else{
        alert(`Orden creada con exito bajo el #${data.id}`)
        window.location.reload()
      }
    }
    
  } catch (error) {
    console.error(error);
  }



}


 //==============================
//convertir productos a pedidos

/**
 * Esta funcion lo que hace es extraer todo los elementos de  la lsita 
 * @props.pedidos.prodctos y lo convieeter en @pedidosEntity
 */
function llenarLista(){
const ListaPedidos:PedidosEntity[]=[]
props.pedido.map((items:ProductosEntity)=>(
  ListaPedidos.push({
  
    idOrden: "ss",
    idProducto: items.id,
    cantidad: items.cantidad,
    total: items.cantidad * items.precio,
  })
 ))
return ListaPedidos}


//==============================================
/*/encabezadpoOrdenes
 let encabezado:OrdenesEntity={
  "id":"x",
  "total":Number(total),
  "sede":String(sede),
  "fechaPedido":"n",
  "fechaPago":"n",
  "status":"por pagar",
  "idCliente":Number(cliente.id),
  "tipoPago":"",
  "idPago":""

 }


/*/




 return (
        <div className="flex-row-reverse   carrito rounded" style={{backgroundColor:"#1f2937",right:"3%"}} >
            <form className="card p-2">
          <div className="input-group">
            <input type="text" value={inputValue}  onChange={handleInputChange} className="form-control" placeholder="Buscar Cliente "/>
            <button type="button" onClick={()=>{buscarCliente(inputValue),trigger(true)}} className="btn btn-primary">Buscar</button>
          </div>
          <div className=" " style={{maxHeight: "1px;"}} >
          {mostrar?( 
          <div className="scrollCarrito   bg-dark align-items-center mb-3">
         {clientes.map((items)=> <center><button className="btn btn-primary w-100" onClick={()=>{trigger(false),seleccionarCliente(items)}} value={items.id} key={items.id}>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-person-circle m-2" viewBox="0 0 16 16">
  <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
  <path fillRule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
</svg>
 {items.nombre}</button>
 </center>
 )
         }
        
        </div>):<></>}</div>
        </form>
        
        <h4 className="d-flex justify-content-between align-items-center mb-2">
        <span className="text-md p-2 text-white d-block">{'\t'+cliente.nombre}</span>
          </h4>
          <h4 className="d-flex justify-content-between align-items-center mb-2">
   
          
          <span className="badge  rounded-pill">CI:{cliente.ci}</span>
          <span className="badge  rounded-pill">WALLET:{wallet.toFixed(2)}$</span>

        </h4>
         <center> <h4 className="d-flex  justify-content-between align-items-center mb-2">
          <span className="badge  align-items-center  rounded-pill">Total:{total.toFixed(2)}$</span>
          </h4></center>
          <ul className="list-group mb-3 scrollCarrito">
          {props.pedido.map((items:ProductosEntity)=>(
            <li key={items.id} className="list-group-item d-flex justify-content-between lh-sm">
            <div>
          
              <h6 className="my-2 mr-2 nombreProductoCar">{items.nombre}</h6>
          

            </div>
            <div>
            
           
              </div>
              <h6 className="m-3 ml-5 p-2">{"\t"}{"\t"} {items.cantidad}X</h6>
            <h5 className="text-success mt-3">{items.precio * items.cantidad}$</h5>
            <div className="p-2 "><button className="btn btn-success " onClick={()=> props.aumento(items)} >+</button>{'\t'}<button onClick={()=>props.descremento(items)} className="p-2 btn btn-danger">-</button></div>
          </li>
          ))}
       
          
         
        </ul>
        <center><div className="list-group-item bg-secondary d-flex justify-content-between">
        <button className="btn  w-100 btn-primary p-2 rounded " onClick={()=>crearOrden({
  id:"x",
  total:Number(total),
  sede:String(sede),
  fechaPedido:"n",
  fechaPago:"n",
  status:"por pagar",
  idCliente:Number(cliente.id),
  tipoPago:"",
  idPago:""

 }
          ,llenarLista())}>CREAR ORDEN</button>
        </div></center>

        
      </div>
    

    )


}