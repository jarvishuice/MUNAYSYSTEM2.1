
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridToolbarContainer, GridToolbarExport, } from '@mui/x-data-grid';
import { useEffect, useState } from 'react';
import { Button } from '@mui/joy';
import { VisitantesDAO } from '../../core/Implements/visitantes/visitantesDAO';
import { ClientesEntity } from '../../core/Entities/clients/clients';
import { ClientesDAO } from '../../core/Implements/clients/clientesDAO';
import { OrdenesDAO } from '../../core/Implements/Ordenes/ordenesDAO';
import { OrdenesDetalladasEntity } from '../../core/Entities/ordenes/ordenesEntity';
const sede = localStorage.getItem("sede")??"inicie seccion";
function CustomToolbar() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }


/**
 * Triggers the conversion of visitor information when a button is clicked.
 * Retrieves data from the clicked row in a table and passes it to the `convertirVisitante` function.
 * @param params - An object containing the data of the clicked row in the table.
 * @returns A Promise that resolves to a `ClientesEntity` object or `null`.
 */

const columns: GridColDef[] = [
  {
    field: 'id',
    headerName: 'Id',
    width: 10,
    editable: false,
  },
  {
    field: 'nombre',
    headerName: 'Nombre',
    width: 150,
    editable: false,
  },

  {
    field: 'apellido',
    headerName: 'Apellido',
   
    width: 10,
    editable: false,
    
  },
  {
    field: 'correo',
    headerName: 'Correo',
   
    width: 100,
    editable: false,
    
  },

  {
    field: 'tlf',
    headerName: 'TLF',
   
    width: 100,
    editable: false,
    
  },
  {  field: 'fechaingreso',
  headerName: ' Ingreso',

  width: 150,
  editable: false,
  },
  {
    field: 'ci',
    headerName: 'CI /Rif',
 
    width: 100,
    editable: false,
  },
  {  field: 'status',
  headerName: ' Estado',
 
  width: 110,
  editable: false,

  },{
    field: 'direccion',
    headerName: ' Direccion',

    width: 110,
    editable: false,
  },
  {
    field: 'convertir',
    headerName: 'Convertir ',
 
    width: 110,
    editable: false,
    renderCell:(params)=>(
      <Button color="primary"  variant="solid" size="sm" onClick={()=>alert(params)}> Convertir </Button>
    )
  },
  
];



export  function OrdenesTable() {
   /**
   * Initializes a state variable called `visitas` using the `useState` hook.
   * Defines an asynchronous function called `fecthVisita` that fetches data from an API using an instance of the `VisitasDAO` class.
   * The fetched data is then set to the `visitas` state variable using the `setVisitas` function.
   * The `fecthVisita` function is called once when the component mounts using the `useEffect` hook.
   */
  const[visitante,setVisitantes]=useState<OrdenesDetalladasEntity[]|null> ([])
  
    /**
   * Fetches data from an API using an instance of the @class`VisitasDAO`  
   * and sets the fetched data to the `visitas` state variable.
   * 
   * @returns {Promise<void>} 
   * - A promise that resolves once the data is fetched and set to the state variable.
   */
  async function fecthOrdenes(): Promise<void> {
    try {
        const ControladorOrdenes = new OrdenesDAO();
        const data = await ControladorOrdenes.getOrdenesBySede(sede);
        setVisitantes(data);
      } catch (error) {
        console.error(error);
      }
}
useEffect(() => {
  fecthOrdenes();
}, []);

const rows = visitante

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
        pageSizeOptions={[7]}
     
        disableRowSelectionOnClick
      />
    </Box>
  );
}
