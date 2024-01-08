
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridToolbarContainer, GridToolbarExport, } from '@mui/x-data-grid';
import { useEffect, useState } from 'react';
import { DeudasClientesEspaciosDAO } from '../../core/Implements/clients/deudasClientesEspaciosDAO';
import { DeudaClientesEntity } from '../../core/Entities/clients/dedudaClientes';
import { ModalPayEspacios } from './ModalPAyEspacios';
function CustomToolbar() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }


function botonera(params:any){
 
  alert("DEudas "+ JSON.stringify(params));

}

const columns: GridColDef[] = [
  {
    field: 'idCliente',
    headerName: 'ID',
    width: 100,
    editable: false,
  },
  {
    field: 'ci',
    headerName: 'CI/RIF',
    width: 200,
    editable: false,
  },

  {
    field: 'nombre',
    headerName: 'NOMBRE',
    width: 350,
    editable: false,
    
  },
  {
    field: 'cantidadOrdenes',
    headerName: '#ORDENES',
   
    width: 150,
    editable: false,
    
  },

  {
    field: 'deuda',
    headerName: 'DEUDAS$',
   
    width: 110,
    editable: false,
    
  },
  
  {
    field: 'Detalles',
    headerName: 'DETALLES',
 
    width: 200,
    editable: false,
    renderCell:(params)=>(
    <ModalPayEspacios onClick={()=>botonera(params)} deudaCliente={{  
      idCliente:Number(JSON.stringify(params.row.idCliente).replace(/['"]+/g, '')),
      ci:String(JSON.stringify(params.row.ci).replace(/['"]+/g, '')),
      nombre:String(JSON.stringify(params.row.nombre).replace(/['"]+/g, '')),
      cantidadOrenes:Number(JSON.stringify(params.row.cantidadOrdenes).replace(/['"]+/g, '')),
      deuda:Number(JSON.stringify(params.row.deuda).replace(/['"]+/g, ''))
    }}  ></ModalPayEspacios>
    )
  },
  
];



export  function DeudasEspaciosTable() {
   /**
   * Initializes a state variable called `visitas` using the `useState` hook.
   * Defines an asynchronous function called `fecthVisita` that fetches data from an API using an instance of the `VisitasDAO` class.
   * The fetched data is then set to the `visitas` state variable using the `setVisitas` function.
   * The `fecthVisita` function is called once when the component mounts using the `useEffect` hook.
   */
  const[deudas,setDeudas]=useState<DeudaClientesEntity[]|[]> ([])
  
    /**
   * Fetches data from an API using an instance of the @class`VisitasDAO`  
   * and sets the fetched data to the `visitas` state variable.
   * 
   * @returns {Promise<void>} 
   * - A promise that resolves once the data is fetched and set to the state variable.
   */
  async function fecthVisita(): Promise<void> {
    try {
        const ControladorDeudasEspacios = new DeudasClientesEspaciosDAO();
        const data = await ControladorDeudasEspacios.DeudasClientesBysede(localStorage.getItem('sede')??'sede');
        setDeudas(data);
      } catch (error) {
        console.error(error);
      }
}
useEffect(() => {
  fecthVisita();
}, []);

const rows = deudas ;

  return (
    <Box sx={{ height: "100vh", width: '100%' }}>
      <DataGrid

  slots={{
    toolbar: CustomToolbar,
  }}

rows={rows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 10,
            },
          },
        }}
        getRowId={(row) => row.idCliente}
        pageSizeOptions={[7]}
     
        disableRowSelectionOnClick
      />
    </Box>
  );
}
