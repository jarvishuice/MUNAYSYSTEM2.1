
import Table from '@mui/joy/Table';

import Button from '@mui/joy/Button';
import Modal from '@mui/joy/Modal';
import ModalClose from '@mui/joy/ModalClose'
import Sheet from '@mui/joy/Sheet';
import { ConsumoDetalladoEntity, OrdenesDetalladasEntity } from '../../core/Entities/ordenes/ordenesEntity';
import { useEffect, useState } from 'react';
import { OrdenesDAO } from '../../core/Implements/Ordenes/ordenesDAO';

import React from 'react';



const sede =localStorage.getItem("sede")??" "
export  function TableOrder() {
const[ordenes,setOrdenes]= useState<OrdenesDetalladasEntity[]|null>([])
useEffect(()=>{
    async function fechtOrdenes(sede:string) {
       try{ const controladorOrdenes = new OrdenesDAO();
        const data = await controladorOrdenes.ordenesToday(sede);
        setOrdenes(data);
        console.log(JSON.stringify(data)+`data`);
       }catch (error){
        console.error(error);
        }
    }fechtOrdenes(sede)
},[localStorage.getItem("sede")])

const [detalles,setDetalles]=useState<ConsumoDetalladoEntity[]|null>([])
async function fechtDetalles(idOrden:string){
  try{
    const controladorOrdenes = new OrdenesDAO();
    const data= await controladorOrdenes.consumoDetallado(idOrden);
    setDetalles(data)
  }
  catch(error){
    console.error(error)
  }
}
console.log(detalles)

//state nmodal 
const [open, setOpen] = React.useState<boolean>(false);
//


  return (
    <div>
     
      <Sheet sx={{ height: '75vh', overflow: 'auto' }}>
        
        <Table
          aria-label="table with sticky header"
          stickyHeader
          stickyFooter
          stripe="odd"
          hoverRow
        >
          <thead>
            <tr>
              <th>Id</th>
              <th>Cliente</th>
              <th>total$</th>
              <th>status</th>
              <th>Fecha</th>
              <th>Hora</th>
              <th> Detalles</th>
            </tr>
          </thead>
          <tbody>
            {ordenes&&ordenes.map((row) => (
               
             <tr key={row.idOrden}>
                           <td>{row.idOrden}</td>
                <td>{row.cliente}</td>
                <td>{row.total}</td>
                <td>{row.status}</td>
                <td>{String(row.fecha)}</td>
                <td>{row.hora}</td>
                <td><React.Fragment> <Button  variant="outlined" color="neutral" onClick={() => {fechtDetalles(row.idOrden);setOpen(true)}} > detalles</Button>  
                <Modal
        aria-labelledby="close-modal-title"
        open={open}
        onClose={(_event: React.MouseEvent<HTMLButtonElement>, reason: string) => {
          console.log(reason);
          setOpen(false);
        }}
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Sheet
          variant="outlined"
          sx={{
            minWidth: 300,
            borderRadius: 'md',
            p: 3,
          }}
        >
          <ModalClose variant="outlined" />
      
          <Table aria-label="basic table">
           <thead>
            <th> Producto</th>
            <th> Cantidad</th>
            <th>Precio</th>
            <th>Total</th>
            </thead> 
            <tbody>
    {detalles && detalles.map((items)=>{
     return (<tr key={items.nombre+items.cantidad}> 
                  <td>{items.nombre}</td>
                  <td>{items.cantidad}</td>
                  <td>{items.precio}</td>
                  <td>{items.total}</td>
     </tr>)
    })}</tbody></Table>
        </Sheet>
      </Modal>
                
                
                 </React.Fragment>
              
                
             </td>
               
 
              </tr> 
        
            ))}     
          </tbody>
        
        </Table>
      </Sheet>
    </div>
  );
}