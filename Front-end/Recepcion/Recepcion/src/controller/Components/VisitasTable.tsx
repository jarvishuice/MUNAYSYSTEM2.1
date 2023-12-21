
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridToolbarContainer, GridToolbarExport,  } from '@mui/x-data-grid';
import { DetailVisitasEntity } from '../../core/Entities/visistas/visitasEntity';
import { useEffect, useState } from 'react';
import { VisitasDAO } from '../../core/Implements/visitas/visitasDAO';
import { Button } from '@mui/joy';
function CustomToolbar() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }

 async function salida(idVisit:string ):Promise<boolean>{
     /**
    * Marca una visita como completada 
    * 
    * @param idVisit -este es el id de la visita que se quiere vfinalizar 
    * @returns un boleano indicado si la visita se finalizo con exito o no 
    * 
    */
  try {
    const ControladorVisitas = new VisitasDAO();
    const data = await ControladorVisitas.salidaVisita(idVisit);
    if (data === true){
      alert("Visita culminada con exito ")
    
    }
    return data as boolean;
   
  } catch (error) {
    console.error(error);
    return false

  }

}
function botonera(params:any){
 
  salida(JSON.stringify(params.row.id).replace(/['"]+/g, ''));

}
const columns: GridColDef[] = [
  {
    field: 'id',
    headerName: 'Id',
    width: 100,
    editable: false,
  },
  {
    field: 'visitante',
    headerName: 'visitante',
    width: 150,
    editable: false,
  },

  {
    field: 'correo',
    headerName: 'Correo',
   
    width: 150,
    editable: false,
    
  },
  {
    field: 'ci',
    headerName: 'Cedula/Rif',
   
    width: 150,
    editable: false,
    
  },

  {
    field: 'cliente',
    headerName: ' Cliente A visitar',
   
    width: 110,
    editable: false,
    
  },
  {  field: 'fIngreso',
  headerName: ' Entrada',

  width: 150,
  editable: false,
  },
  {
    field: 'fSalida',
    headerName: 'Salida',
 
    width: 150,
    editable: false,
  },
  {  field: 'status',
  headerName: ' Estado',
 
  width: 110,
  editable: false,

  },{
    field: 'sede',
    headerName: ' sede',

    width: 110,
    editable: false,
  },

  {
    field: 'motivo',
    headerName: 'motivo ',
 
    width: 110,
    editable: false,
  },
  {
    field: 'salir',
    headerName: 'salir ',
 
    width: 110,
    editable: false,
    renderCell:(params)=>(
      <Button color="danger" disabled={params.row.status==='activa'?false:true} size="lg" onClick={()=>botonera(params)}> Salir </Button>
    )
  },
  
];



export  function VisitasTable() {
   /**
   * Initializes a state variable called `visitas` using the `useState` hook.
   * Defines an asynchronous function called `fecthVisita` that fetches data from an API using an instance of the `VisitasDAO` class.
   * The fetched data is then set to the `visitas` state variable using the `setVisitas` function.
   * The `fecthVisita` function is called once when the component mounts using the `useEffect` hook.
   */
  const[visitas,setVisitas]=useState<DetailVisitasEntity[]|[]> ([])
  
    /**
   * Fetches data from an API using an instance of the @class`VisitasDAO`  
   * and sets the fetched data to the `visitas` state variable.
   * 
   * @returns {Promise<void>} 
   * - A promise that resolves once the data is fetched and set to the state variable.
   */
  async function fecthVisita(): Promise<void> {
    try {
        const ControladorVisitas = new VisitasDAO();
        const data = await ControladorVisitas.getVisitasDetailToday(localStorage.getItem('sede')??'sede');
        setVisitas(data);
      } catch (error) {
        console.error(error);
      }
}
useEffect(() => {
  fecthVisita();
}, []);

const rows = visitas

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
