
//debo de sacar el wallet fuction para porderlo actualizar sin recarga 
import React, {useEffect, useState } from 'react';

import '../../formPay.css'

import { TasaDollarDAO } from '../../core/Implements/finance/tasaDollarDAO';
import { CuentasEntity } from '../../core/Entities/cuentas/cuentasEntity';
import { CuentasDAO } from '../../core/Implements/Cuentas/cuentasDAO';
import { PagosEntity } from '../../core/Entities/pagos/pagosEntity';
import { PagosDAO } from '../../core/Implements/pagos/pagosDAO';
import { DeudasClientesDAO } from '../../core/Implements/clients/deudasClientesDAO';
import { AbonosDAO } from '../../core/Implements/abonos/abonosDAO'


/**
 * Description placeholder
 * @date 31/1/2024 - 3:18:40 p. m.
 *
 * @export
 * @param {*} props
 * @returns {JSX.Element}
 */
export function ModalFormPago(props:any){
  const sede= localStorage.getItem('sede')??'cfm'
  const reinicio=()=>{fecthWallet()}
  //estado wallet 
  async function fecthWallet() {
    try {
        const controladorAbonos = new AbonosDAO();
        const data = await controladorAbonos.consultasaldoAbono(props.cliente.idCliente);
        setAbono(data);
      } catch (error) {
        console.error(error);
      }
  }
  fecthWallet();
  const[abono,setAbono] = useState<number>(0);
  useEffect (()=>{
    async function fecthWallet() {
        try {
          const controladorAbonos = new AbonosDAO();
          const data = await controladorAbonos.consultasaldoAbono(props.cliente.idCliente);
            setAbono(data);
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
    const contorladorPagos = new PagosDAO();
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
  if(montoValue > props.cliente.deuda - abono){
    const  x=confirm(`El cliente desea abonar ${ montoValue -(props.cliente.deuda - abono)} `)
    if (x===true){
      pago.monto=montoValue;
    Rwallet=montoValue -(props.cliente.deuda - abono)}
    else{
    Rwallet=0
     pago.monto=props.cliente.deuda - abono
     Dwallet=abono
    }
  }   
  

  try{
    const controladorDeudaClientes = new DeudasClientesDAO();
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
const [montoValue, setMontoValue] = useState<number >(props.cliente.deuda - abono);

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
/**
 * Esta funcion restablc los datos  de referencia y el monto que 
 * 
 * @date 31/1/2024 - 3:22:37 p. m.
 * @author jarvishuice 
 */
function restablecer(){
  setEReferencia('');
  setMontoValue(0);
  
}

//control de visualizacon del modal 
if (!props.isOpen) return null;
//=======
 return(
      <main className="page payment-page  " tabIndex={-1}>
        <section className="payment-form dark">
          <div className="container">
            <div className="block-heading">
              <h2>Pagos</h2>
              
            </div>
            <form>
              <div className="products">
                <h3 className="title">Informacion del cliente</h3>
                <div className="item">
                  <span className="price">{props.cliente.nombre}</span>
                  <p className="item-name">Cliente </p>
                
                </div>
                <div className="item">
                  <span className="price">${abono.toFixed(2)}</span>
                  <p className="item-name">Abonado </p>
                  
                </div>
                <div className="item">
                  <span className="price">${props.cliente.deuda.toFixed(2)}</span>
                  <p className="item-name">Total </p>
                  
                </div>
                <div className="item">
                  <span className="price">BS.{tasa.toFixed(2)}</span>
                  <p className="item-name">TasaBCV </p>
                  
                </div>
                <div className="total">Total A pagar Bs<span className="price">Bs.{((props.cliente.deuda - abono) * tasa).toFixed(2)}</span></div>
                <div className="total">Total A pagar <span className="price">${(props.cliente.deuda - abono).toFixed(2)}</span></div>
              </div>
              <div className="card-details">
                <h3 className="title">Informacion de pago</h3>
                <div className="row">
                  <div className="form-group col-sm-7">
                    <label htmlFor="card-holder"> forma de pago</label>
                    <select id="card-holder" value={fpago} onChange={handleChangefpago} className="form-control" placeholder="Card Holder" aria-label="Card Holder" aria-describedby="basic-addon1">
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
                    <input id="cvc" type="number"  step="0.01" value={montoValue} onChange={handleChange}  placeholder={`${props.cliente.deuda - abono}`} className="form-control" aria-label="Card Holder" aria-describedby="basic-addon1"/>
                  </div>
                  
                    <button type="button" className={"btn  btn-success "} disabled={(montoValue >= props.cliente.deuda - abono)?false:true} onClick={()=>{
                        SaldarDeudas(0,abono,{id:'f',
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
                    
                    <button type="button" className={"btn btn-warning "} disabled={montoValue < (props.cliente.deuda - abono) ?false:true} onClick={()=>{Multipago({
                        id:"f",
                        fecha:"f",
                        monto:montoValue??0.0,
                        motivo:"Multipago",
                        idcliente:props.cliente.idCliente,
                        idformadepago:fpago,
                        referencia:ERferencia,
                        idtaza:"d",
                        sede:sede,



                    }),reinicio(),restablecer()}}>Abonos</button>
                    <button type="button" onClick={props.onClose} className="btn btn-danger">Cerrar</button>

                </div>
              </div>
            </form>
          </div>
        </section>
      </main>

    )



}