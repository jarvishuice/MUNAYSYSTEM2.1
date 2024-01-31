
import { useEffect, useState } from 'react';

import { DetalleDeudaCliente, DeudaClientesEntity } from '../../core/Entities/clients/dedudaClientes';
import { DeudasClientesDAO } from '../../core/Implements/clients/deudasClientesDAO';
export function Ordenes(props:any){
  const sede = localStorage.getItem('sede') ?? 'por favor inicie sesión para poder crear una orden';
const [deudas,setDeudas]= useState<DeudaClientesEntity[]>([]);


/**
 * Extrae las deudas del clientes 
 * @date 31/1/2024 - 3:31:05 p. m.
 *
 * @async
 * @returns {*}
 */
async function fecthDeuda() {
      try {
          const ControladorDeudas = new DeudasClientesDAO();
          const data = await ControladorDeudas.DeudasClientesBysede(localStorage.getItem('sede'));
          setDeudas(data);
        } catch (error) {
          console.error(error);
        }
  }
  useEffect(() => {
    fecthDeuda();
  }, []);

const [SC,setSC]=useState<number>(8)
const SSC=(id:number)=>{
  setSC(id);
}
localStorage.setItem('prueba',SSC.name)

const [detalles,setDetalles]=useState<DetalleDeudaCliente[]>([{fechaPedido:" ",producto:" ",cantidad:0,precio:0,total:'1',sede:sede,idOrden:"3333"},])

async function DETALLESDEUDAS(idCliente:number) {
  try {
    const controladorDeudas = new DeudasClientesDAO();
    const data = await controladorDeudas.DetalleDeudaClientes(sede, idCliente);
    setDetalles(data);
    trigger(true)

    console.log(data);
  } catch (error) {
    console.error(error);
  }
  
}
useEffect(()=>{
  DETALLESDEUDAS(SC)
},[])
const [mostrar,setMostrar] = useState<Boolean>(false);
 const trigger=(gatillo:Boolean)=>{
   setMostrar(gatillo);


 }
 console.log(mostrar)

 const [inputValue,setInputValue] =useState<String|any>("")
const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  const [nombre, setNombre] = useState(inputValue);
  const buscarProducto = (valor: string | any) => {
      setNombre(valor);
    };
 const [clientes,setClientes]  =useState<DeudaClientesEntity[]>(deudas)
 useEffect(()=>{
  /**
   * busqueda del cliente
   * @date 31/1/2024 - 3:31:37 p. m.
   *
   * @param {string} nombe
   */
  function filtarCliente(nombe:string) {
    if(nombre === ""){
setClientes(deudas)

    }
    else{  
    const contenedor=deudas.filter((person:DeudaClientesEntity) =>
    person.nombre.toLowerCase().includes(nombe.toLowerCase()));
    console.log(contenedor+"j")
    //setDeudas(contenedor)
    setClientes(contenedor);
    console.log(JSON.stringify(clientes));
  }}filtarCliente(nombre);


 },[nombre]) 


return (


  <div className="container-fluid  vh-10 col-sm-4 col-md-7 col-sx-8 col-lg-7 m-0 mt-1 vh-100 " >
          <div className=" offset-md-1   mt-2 ">
            <input className=" w-50 me-1" onChange={handleInputChange} value={inputValue} key='1' type="search" placeholder={inputValue} aria-label="Search"/>
        <button className="btn btn-outline-primary " key='2' onClick={()=>{buscarProducto(inputValue)}} type="submit">Buscar</button>
      {/*  { mostrar ?(
     <div className="row w-50  bg-primary border-bottom text-white align-content-center overflow-scroll  " >
      
      {clientes && clientes.map((x) => (
        <center><li key={x.nombre} onClick={()=>{{props.selectorDeudor(x),DETALLESDEUDAS(x.idCliente),trigger(false)}}}>
     
          {x.nombre}</li></center>

      ))}
      </div>):<div></div>}*/}

        </div>
    <div className="row p-3 scrollable" >
   
  {clientes.length >=1 ?clientes.map((items:DeudaClientesEntity)=>{
    
     return <div className="col-md-4 p-1" onClick={()=>{props.selectorDeudor(items)}}  key={items.idCliente}>
     
        <div className="card"  >
          
          <div className="card-body">
         
           
       
         
     
            <p className="nombreProducto">{items.nombre}.</p>
            <h6 className="card-title mt-4">CEDULA:{items.ci}</h6>
           <center> <h4 className="card-title mt-4 ">{items.deuda - items.abono}$ </h4></center>
            <h6>#ORDENES: {"\t"}{items.cantidadOrdenes}</h6>
            <center><button className='btn btn-primary mt-2' onClick={()=>{DETALLESDEUDAS(items.idCliente),props.detallesDeudor(detalles)}}> DETALLES</button></center>
          </div>
        </div>
      </div>}):deudas.map((items:DeudaClientesEntity)=>{
    
    return <div className="col-md-4 p-1" onClick={()=>{props.selectorDeudor(items)}}  key={items.idCliente}>
    
       <div className="card"  >
         
         <div className="card-body">
        
          
      
        
    
           <p className="nombreProducto">{items.nombre}.</p>
           <h6 className="card-title mt-4">CEDULA:{items.ci}</h6>
          <center> <h4 className="card-title mt-4 ">{items.deuda - items.abono}$ </h4></center>
           <h6>#ORDENES: {"\t"}{items.cantidadOrdenes}</h6>
           <center><button className='btn btn-primary mt-2' onClick={()=>{DETALLESDEUDAS(items.idCliente),props.detallesDeudor(detalles)}}> DETALLES</button></center>
         </div>
       </div>
     </div>})}
      {detalles.map((items:DetalleDeudaCliente)=>{
        return <>{props.detallesDeudor(detalles)}{items.idOrden}</>

      })}
     
    </div>
  </div>

    );
}