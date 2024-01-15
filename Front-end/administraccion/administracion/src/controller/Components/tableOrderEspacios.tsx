
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridToolbarContainer, GridToolbarExport, } from '@mui/x-data-grid';
import { useEffect, useState } from 'react';
import { IconButton } from '@mui/joy';
import { OrdenesEspaciosDAO } from '../../core/Implements/Ordenes/OrdenesEspaciosDAO';
import { OrdenesDetalladasEntity } from '../../core/Entities/ordenes/ordenesEntity';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
const sede = localStorage.getItem("sede")??"inicie seccion";
function CustomToolbar() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }

 

async function deleteORder(idOrder:string){
  try {
    const ControladorOrdenes = new OrdenesEspaciosDAO();
    const data = await ControladorOrdenes.deleteOrden(idOrder);
    alert(`Orden #${idOrder} eliminada: ${data}`);
    window.location.reload()
  } catch (error) {
   alert(error);
  }
}
function mostrarCElda(params:any){

  deleteORder(JSON.stringify(params.row.idOrden).replace(/['"]+/g, ''));


}

const columns: GridColDef[] = [
  {
    field: 'idOrden',
    headerName: 'Id',
    width: 250,
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
    headerName: 'Eliminar ',
 
    width: 110,
    editable: false,
    renderCell:(params)=>(
    <IconButton size={"lg"} color="danger" onClick={()=>mostrarCElda(params)}> 
  <DeleteForeverIcon /> 
   </IconButton>
    )
  },
  
];



export  function TableOrderEspacios() {
   
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
        const ControladorOrdenes = new OrdenesEspaciosDAO();
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
    getRowId={(row)=>row.idOrden}
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
