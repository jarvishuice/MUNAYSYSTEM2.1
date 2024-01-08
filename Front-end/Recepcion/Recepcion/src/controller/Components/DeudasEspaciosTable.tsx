
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridToolbarContainer, GridToolbarExport, } from '@mui/x-data-grid';
import { useEffect, useState } from 'react';
import { Button } from '@mui/joy';
import { DeudasClientesEspaciosDAO } from '../../core/Implements/clients/deudasClientesEspaciosDAO';
import { DeudaClientesEntity } from '../../core/Entities/clients/dedudaClientes';
function CustomToolbar() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }


function botonera(params:any){
 
  alert(JSON.stringify(params.row.id).replace(/['"]+/g, ''));

}
const columns: GridColDef[] = [
  {
    field: 'idCliente',
    headerName: 'ID',
    width: 10,
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
    headerName: 'DEUDA$',
   
    width: 110,
    editable: false,
    
  },
  
  {
    field: 'salir',
    headerName: 'salir ',
 
    width: 110,
    editable: false,
    renderCell:(params)=>(
      <Button color="danger"  size="lg" onClick={()=>botonera(params)}> DETALLES </Button>
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
