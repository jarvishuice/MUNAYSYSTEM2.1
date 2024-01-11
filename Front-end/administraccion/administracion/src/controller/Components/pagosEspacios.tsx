
//debo de sacar el wallet fuction para porderlo actualizar sin recarga 
import React, {useEffect, useState } from 'react';
import "../../Espacios.css"
import { WalletDAO } from '../../core/Implements/wallet/walletDAO';
import { WalletEspaciosDAO } from '../../core/Implements/wallet/walletEspaciosDAO';
import { TasaDollarDAO } from '../../core/Implements/finance/tasaDollarDAO';
import { CuentasEntity } from '../../core/Entities/cuentas/cuentasEntity';
import { CuentasDAO } from '../../core/Implements/Cuentas/cuentasDAO';
import { PagosEntity } from '../../core/Entities/pagos/pagosEntity';
import { PagosEspaciosDAO } from '../../core/Implements/pagos/pagosEspaciosDAO';

import { DeudasClientesEspaciosDAO } from '../../core/Implements/clients/deudasClientesEspaciosDAO';

export function PagosEspacios(props:any){
const sede= localStorage.getItem('sede')??'cfm'
const reinicio=()=>{fecthWallet()}
//estado wallet 
async function fecthWallet() {
  try {
      const controladorWallet = new WalletEspaciosDAO();
      const data = await controladorWallet.consultasaldoWallet(props.cliente.idCliente);
      setWallet(data);
    } catch (error) {
      console.error(error);
    }
}
fecthWallet();
const[wallet,setWallet] = useState<number>(0);
useEffect (()=>{
  async function fecthWallet() {
      try {
          const controladorWallet = new WalletDAO();
          const data = await controladorWallet.consultasaldoWallet(props.cliente.idCliente);
          setWallet(data);
        } catch (error) {
          console.error(error);
        }
  }
  fecthWallet();
},[props.cliente.id]);
//==========================================================================


//Extractor de la tasa del bcv
const [tasa,setTasa]= useState<number>(0);
useEffect (()=>{
    async function fecthTasa() {
        try {
            const controladorTasa = new TasaDollarDAO();
            const data = await controladorTasa.ObtenerTazaActual();
            setTasa(data);
          } catch (error) {
            console.error(error);
          }
    }
    fecthTasa();
  },[]);
//=========================
//ExtractorFormas de pagos 
const [payForm,setPayForm]=useState<CuentasEntity[]>([])
useEffect (()=>{
    async function fecthPlanCuentas() {
        try {
            const controladorCuentas =  new CuentasDAO ();
            const data = await controladorCuentas.getCuentasBySede(sede);
            setPayForm(data);
          } catch (error) {
            console.error(error);
          }
    }
    fecthPlanCuentas();
  },[]);
//FUncion  para registrar multipago
async function Multipago (pagoData:PagosEntity){
  try {
    const contorladorPagos = new PagosEspaciosDAO();
    const data = await contorladorPagos.RegMultipago(pagoData);
    if (data != null ){
       alert(`Pago registrado de m,anera correcta bajo la modalidad de multipago con el #${data.id}`)
      reinicio()
    }
    
  } catch (error) {
    console.error(error);
  }



}
//funcion para saldar deudas de los clientes
async function SaldarDeudas(Rwallet:number,Dwallet:number,pago:PagosEntity) {
  if(montoValue > props.cliente.deuda - wallet){
    const  x=confirm(`El cliente desea abonar ${ montoValue -(props.cliente.deuda - wallet)} `)
    if (x===true){
      pago.monto=montoValue;
    Rwallet=montoValue -(props.cliente.deuda - wallet)}
    else{
    Rwallet=0
     pago.monto=props.cliente.deuda - wallet
     Dwallet=wallet
    }
  }   
  

  try{
    const controladorDeudaClientes = new DeudasClientesEspaciosDAO();
    const  data= await controladorDeudaClientes.SaldarDeudaClientes(Rwallet,Dwallet,pago)
    if (data != null){
    alert(`deuda pagada con el id de pago ${data.id}`);
    reinicio()
    window.location.reload();
    }
  
  }
  catch (error){
    alert(`Error al intentar saldar la deuda detail ${(error)}`)
    console.error(error)
  }
}
//
//estado para extraer el  monto de pago
const [montoValue, setMontoValue] = useState<number >(props.cliente.deuda - wallet);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setMontoValue(parseFloat(e.target.value));
  };

//
// Estado para ela extracion del( metodo de pago
const [fpago,setFPago]= useState<number>(1);
 const handleChangefpago=(e: React.ChangeEvent<HTMLSelectElement>)=>{
    setFPago(parseInt(e.target.value));

 }


//
//estado para extracion de la referencia
const [ERferencia,setEReferencia]=useState<string>(' ')
const handleChangeReferencia=(e:React.ChangeEvent<HTMLInputElement>)=>{
setEReferencia(e.target.value)
}
//

//control de visualizacon del modal 

//=======
return(  <main className="page payment-page  " >
<section className="payment-form dark">
  <div className="container">
   
    <form>
      <div className="products">
        <h3 className="title">Informacion del cliente</h3>
        <div className="item">
          <span className="price">{props.cliente.nombre}</span>
          <p className="item-name">Cliente </p>
        
        </div>
        <div className="item">
          <span className="price">${wallet.toFixed(2)}</span>
          <p className="item-name">Wallet </p>
          
        </div>
        <div className="item">
          <span className="price">${props.cliente.deuda.toFixed(2)}</span>
          <p className="item-name">Total </p>
          
        </div>
        <div className="item">
          <span className="price">BS.{tasa.toFixed(2)}</span>
          <p className="item-name">TasaBCV </p>
          
        </div>
        <div className="total">Total A pagar Bs<span className="price">Bs.{((props.cliente.deuda - wallet) * tasa).toFixed(2)}</span></div>
        <div className="total">Total A pagar <span className="price">${(props.cliente.deuda - wallet).toFixed(2)}</span></div>
      </div>
      <div className="card-details">
        <h3 className="title">Informacion de pago</h3>
        <div className="row">
          <div className="form-group col-sm-7">
            <label htmlFor="card-holder"> forma de pago</label>
            <select id="card-holder" value={fpago} onChange={handleChangefpago} className="form-control" aria-label="Card Holder" aria-describedby="basic-addon1">
            {payForm.map((items=>(
                <option value={items.id}>{items.metodo}</option>
            )))}
            </select>
          </div>
          
          <div className="form-group col-sm-8">
            <label htmlFor="card-number">Referencia</label>
            <input id="card-number" onChange={handleChangeReferencia} value={ERferencia} type="text" className="form-control" placeholder="Referencia" aria-label="Card Holder" aria-describedby="basic-addon1"/>
          </div>
          <div className="form-group col-sm-4">
            <label htmlFor="cvc" >Monto</label>
            <input id="cvc" type="number"  step="0.01" value={montoValue} onChange={handleChange}  placeholder={`${props.cliente.deuda - wallet}`} className="form-control" aria-label="Card Holder" aria-describedby="basic-addon1"/>
          </div>
          
            <button type="button" style={{width:"30%"}} className={"btn btn-success botonPagosEspacios "} disabled={(montoValue >= props.cliente.deuda - wallet)?false:true} onClick={()=>{
                SaldarDeudas(0,wallet,{id:'f',
                fecha:"f",
                monto:montoValue,
                motivo:"pago",
                idcliente:props.cliente.idCliente,
                idformadepago:fpago,
                referencia:ERferencia,
                idtaza:"d",
                sede:sede,


                });
            }}>Pagar</button>
            
            <button type="button" style={{width:"30%",marginLeft:"5px"}} className={"btn btn-warning "} disabled={montoValue < (props.cliente.deuda - wallet) ?false:true} onClick={()=>{Multipago({
                id:"f",
                fecha:"f",
                monto:montoValue??0.0,
                motivo:"Multipago",
                idcliente:props.cliente.idCliente,
                idformadepago:fpago,
                referencia:ERferencia,
                idtaza:"d",
                sede:sede,



            }),reinicio()}}>MultiPago</button>
            <button type="button" style={{width:"30%",marginLeft:"5px"}} onClick={props.onClose} className="btn btn-danger">Cerrar</button>

        </div>
      </div>
    </form>
  </div>
</section>
</main>
)




}