
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridToolbarContainer, GridToolbarExport, } from '@mui/x-data-grid';
import { useEffect, useState } from 'react';
import { Button } from '@mui/joy';
import { VisitantesDAO } from '../../core/Implements/visitantes/visitantesDAO';
import { ClientesEntity } from '../../core/Entities/clients/clients';
import { ClientesDAO } from '../../core/Implements/clients/clientesDAO';
function CustomToolbar() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }

 async function convertirVisitante(visitante:ClientesEntity):Promise<ClientesEntity|null>{
     /**
    * Convierte un visitante a cliente 
    * 
    * @param visitante Entidad de vivitsante que hereda de la clase clientes 
    * @returns  clienteEntity
    * 
    */
  try {
    const ControladorClientes = new ClientesDAO();
    const data = await ControladorClientes.CrearCliente(visitante);
    alert("Visitante conevertido a cliente con el siguiente ID:"+JSON.stringify(data?.id));
    return data as ClientesEntity;
   
  } catch (error) {
    console.error(error);
    return null

  }

}
/**
 * Triggers the conversion of visitor information when a button is clicked.
 * Retrieves data from the clicked row in a table and passes it to the `convertirVisitante` function.
 * @param params - An object containing the data of the clicked row in the table.
 * @returns A Promise that resolves to a `ClientesEntity` object or `null`.
 */
function botonera(params:any){

  convertirVisitante({id:0,nombre:JSON.stringify(params.row.nombre).replace(/['"]+/g, ''),
  apellido:" ",correo:JSON.stringify(params.row.correo).replace(/['"]+/g, ''),
  tlf:JSON.stringify(params.row.tlf).replace(/['"]+/g, ''),fechaingreso:JSON.stringify(params.row.id).replace(/['"]+/g, ''),
  fechacambio:" ",
  codigo:0,
  credito:0,
  ci:JSON.stringify(params.row.ci).replace(/['"]+/g, ''),
identificacion:JSON.stringify(params.row.identificacion).replace(/['"]+/g, ''),
direccion:JSON.stringify(params.row.direccion).replace(/['"]+/g, ''),
deuda:0});

}
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
      <Button color="primary"  variant="solid" size="sm" onClick={()=>botonera(params)}> Convertir </Button>
    )
  },
  
];



export  function VisitantesTable() {
   /**
   * Initializes a state variable called `visitas` using the `useState` hook.
   * Defines an asynchronous function called `fecthVisita` that fetches data from an API using an instance of the `VisitasDAO` class.
   * The fetched data is then set to the `visitas` state variable using the `setVisitas` function.
   * The `fecthVisita` function is called once when the component mounts using the `useEffect` hook.
   */
  const[visitante,setVisitantes]=useState<ClientesEntity[]|[]> ([])
  
    /**
   * Fetches data from an API using an instance of the @class`VisitasDAO`  
   * and sets the fetched data to the `visitas` state variable.
   * 
   * @returns {Promise<void>} 
   * - A promise that resolves once the data is fetched and set to the state variable.
   */
  async function fecthVisita(): Promise<void> {
    try {
        const ControladorVisitante = new VisitantesDAO();
        const data = await ControladorVisitante.getAllVisitante();
        setVisitantes(data);
      } catch (error) {
        console.error(error);
      }
}
useEffect(() => {
  fecthVisita();
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
