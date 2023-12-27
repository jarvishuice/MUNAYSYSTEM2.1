
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridToolbarContainer, GridToolbarExport, } from '@mui/x-data-grid';
import { useEffect, useState } from 'react';
import { Button } from '@mui/joy';
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
    field: 'idOrden',
    headerName: 'Id',
    width: 10,
    editable: false,
  },
  {
    field: 'cliente',
    headerName: 'Nombre',
    width: 150,
    editable: false,
  },
  {
    field: 'total',
    headerName: 'Total',
   
    width: 100,
    editable: false,
    
  },

  {
    field: 'fecha',
    headerName: 'Fecha de apertura',
   
    width: 100,
    editable: false,
    
  },
  {  field: 'hora',
  headerName: ' Hora',

  width: 150,
  editable: false,
  },
  {
    field: 'status',
    headerName: 'Estado',
 
    width: 100,
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
  const[ordenes,setOrdenes]=useState<OrdenesDetalladasEntity[]|[]> ([])
  
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
        setOrdenes(data);
      } catch (error) {
        console.error(error);
      }
}
useEffect(() => {
  fecthOrdenes();
}, []);

const rows = ordenes;

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
              pageSize: 30,
            },
          },
        }}
        pageSizeOptions={[30]}
     
        disableRowSelectionOnClick
      />
    </Box>
  );
}
