import * as React from 'react';
import EditIcon from '@mui/icons-material/Edit';
import Modal from '@mui/joy/Modal';
import ModalClose from '@mui/joy/ModalClose';
import { CuentasDAO } from '../../core/Implements/Cuentas/cuentasDAO';
import Sheet from '@mui/joy/Sheet';
import { IconButton } from '@mui/joy';
import { CuentasEntity } from '../../core/Entities/cuentas/cuentasEntity';
import SaveAsIcon from '@mui/icons-material/SaveAs';
import { PagosEspaciosDAO } from "../../core/Implements/pagos/pagosEspaciosDAO";
import {PagosEntity} from "../../core/Entities/pagos/pagosEntity";

import { GridColDef, DataGrid, GridToolbarContainer, GridToolbarExport } from "@mui/x-data-grid";
import { useState,useEffect } from "react";

import { PagosDetailEntity } from "../../core/Entities/pagos/pagosEntity";


import { Box } from "@mui/joy";
const sede = localStorage.getItem("sede") ?? "inicia seccion"

const controlador = new PagosEspaciosDAO()




export namespace GestorPayEspacios{
   export function  ModalEditPay(props:any){
        const [open, setOpen] = React.useState<boolean>(false);
        const j = props.x;
            console.log(j);
    async function Modificar(pagoData:PagosEntity){
        try{
            const data = await controlador.editPay(pagoData)
            
            alert(` pago modificado con el siguiente estatus: ${data as Boolean}`)
            setOpen(false);
        }
        catch(error){
            alert(error);
            setOpen(false);
        }
       // console.log(controlador);
       // alert("este es el json:  "+typeof(pagoData)+ JSON.stringify(pagoData))
    }
    
    
    const [payForm,setPayForm]=React.useState<CuentasEntity[]>([])
    React.useEffect (()=>{
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
    
      const [fpago,setFPago]= React.useState<number>(1);
     const handleChangefpago=(e: React.ChangeEvent<HTMLSelectElement>)=>{
        setFPago(parseInt(e.target.value));
    
     }
    
    
     const [date, setDate] = React.useState<string>('');
      const [time, setTime] = React.useState<string>('');
    
      const handleDateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setDate(event.target.value);
      };
    
      const handleTimeChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setTime(event.target.value);
      };
    
    
     
        return (
          <React.Fragment>
            <IconButton color="primary"  variant="solid" size="sm" onClick={()=>setOpen(true)} ><EditIcon/> </IconButton>
            
             
          
            <Modal
              aria-labelledby="modal-title"
              aria-describedby="modal-desc"
              open={open}
              onClose={() => setOpen(false)}
              sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}
            >
              <Sheet
                variant="outlined"
                sx={{
                  maxWidth: 500,
                  borderRadius: 'md',
                  p: 3,
                  boxShadow: 'lg',
                }}
              >
                <ModalClose variant="plain" sx={{ m: 1 }} />
    
                <h2> Editar Pago #{j.row.id}</h2>
                <div className="form-group col-sm-7">
                        <label htmlFor="card-holder"> forma de pago</label>
                        <select id="card-holder" value={fpago} onChange={handleChangefpago} className="form-control mt-2 "  aria-label="Card Holder" aria-describedby="basic-addon1">
                        {payForm.map((items=>(
                            <option value={items.id}>{items.metodo}</option>
                        )))}
                        </select>
                      </div>
                      <div className="form-group col-sm-7">
          <label htmlFor="date-input">Fecha</label>
          <input
            type="date"
            id="date-input"
            value={date}
            onChange={handleDateChange}
            className="form-control mt-2"
          />
          <label htmlFor="time-input">Hora</label>
          <input
            type="time"
            id="time-input"
            value={time}
            onChange={handleTimeChange}
            className="form-control mt-2"
          />
        </div>
    
        <IconButton color="primary"  className="mt-2 " variant="solid" size="sm" onClick={()=> Modificar({id:j.row.id,fecha:`${date} ${time}:00`,monto:j.row.monto,motivo:j.row.motivo,idcliente:j.row.idcliente, idformadepago:fpago,referencia:j.row.referencia,idtaza:"jjj",sede:j.row.sede})}><SaveAsIcon/> Guardar Cambios  </IconButton>
    
              </Sheet>
            </Modal>
          </React.Fragment>
        );
    
    }
    function CustomToolbar() {
        return (
          <GridToolbarContainer>
            <GridToolbarExport />
          </GridToolbarContainer>
        );
      }
      /*function botonera(params:any){
        alert(`Cambios del cliente ${JSON.stringify(params.row.id)} realizado con exito !!!` );
      
      
      }*/
    const columns: GridColDef[] = [
        {
          field: 'id',
          headerName: 'Id',
          width: 90,
          editable: false,
        },
        {
          field: 'fecha',
          headerName: 'Fecha',
          width: 150,
          editable: false,
        },
      
      
        {
          field: 'monto',
          headerName: 'Monto',
         
          width: 60,
          editable: false,
          
        },
      
        {
          field: 'motivo',
          headerName: 'Motivo',
         
          width: 200,
          editable: false,
          
        },
        {  field: 'cliente',
        headerName: ' Cliente',
      
        width: 200,
        editable: false,
        },
        {
          field: 'formaDepago',
          headerName: 'Metodo',
       
          width: 200,
          editable: false,
        },
        {
          field: 'referencia',
          headerName: ' Referencia',
      
          width: 100,
          editable: false,
        },
        {
            field: 'tasa',
            headerName: ' Tasa',
        
            width: 60,
            editable: false,
          },
          {
            field: 'sede',
            headerName: ' Sede',
        
            width: 50,
            editable: false,
          },
          {
            field: 'idcliente',
            headerName: ' cliente ID',
        
            width: 10,
            editable: false,
          },
          {
            field: 'idformadepago',
            headerName: '# forma pay ',
        
            width: 10,
            editable: false,
          },
        {
          field: '',
          headerName: 'Editar ',
       
          width: 30,
          editable: false,
          renderCell:(params)=>(
            <GestorPayEspacios.ModalEditPay x={params}></GestorPayEspacios.ModalEditPay>
          )
        },
        
      ];
    export function TABLEPAY(){
        const[pays,setPays]=useState<PagosDetailEntity[]|any> ([])
        async function fecthClientes(): Promise<void> {
            try {
                const ControladorPays = new PagosEspaciosDAO();
                const data = await ControladorPays.getAllPayDetail();
                setPays(data);
              } catch (error) {
                console.error(error);
              }
        }
        useEffect(() => {
            fecthClientes();
          }, []);
        const rows = pays
    
        return (<Box sx={{ height: "100vh", width: '100%' }}>
        <DataGrid
    
    slots={{
      toolbar: CustomToolbar,
    }} editMode='cell'
    rows={rows}
          columns={columns}
          initialState={{
            pagination: {
              paginationModel: {
                pageSize: 50,
              },
            },
          }}
          pageSizeOptions={[7]}
         
          disableRowSelectionOnClick
        />
      </Box>
    );
    
    }



}