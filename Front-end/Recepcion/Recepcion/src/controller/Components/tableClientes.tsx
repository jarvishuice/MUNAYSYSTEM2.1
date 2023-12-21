
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridToolbarContainer, GridToolbarExport } from '@mui/x-data-grid';
import { useEffect, useState } from 'react';
import { IconButton } from '@mui/joy';
import { ClientesEntity } from '../../core/Entities/clients/clients';
import { ClientesDAO } from '../../core/Implements/clients/clientesDAO';
import SaveIcon from '@mui/icons-material/Save';
function CustomToolbar() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }

 async function GurdarCambios(cliente:ClientesEntity):Promise<ClientesEntity|null>{
     /**
    * Convierte un visitante a cliente 
    * 
    * @param cliente Entidad de vivitsante que hereda de la clase clientes 
    * @returns  clienteEntity
    * 
    */
  try {
    const ControladorClientes = new ClientesDAO();
    const data = await ControladorClientes.updateCliente(cliente);
  
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
  alert(`Cambios del cliente ${JSON.stringify(params.row.id)} realizado con exito !!!` );
  GurdarCambios({id:parseInt(JSON.stringify(params.row.id)),nombre:JSON.stringify(params.row.nombre).replace(/['"]+/g, ''),
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
    width: 90,
    editable: false,
  },
  {
    field: 'nombre',
    headerName: 'Nombre',
    width: 200,
    editable: true,
  },


  {
    field: 'correo',
    headerName: 'Correo',
   
    width: 200,
    editable: true,
    
  },

  {
    field: 'tlf',
    headerName: 'TLF',
   
    width: 200,
    editable: true,
    
  },
  {  field: 'fechaingreso',
  headerName: ' Ingreso',

  width: 150,
  editable: true,
  },
  {
    field: 'ci',
    headerName: 'CI /Rif',
 
    width: 100,
    editable: true,
  },
  {
    field: 'direccion',
    headerName: ' Direccion',

    width: 200,
    editable: true,
  },
  {
    field: '',
    headerName: 'Guardar ',
 
    width: 30,
    editable: false,
    renderCell:(params)=>(
      <IconButton color="primary"  variant="solid" size="sm" onClick={()=>botonera(params)} ><SaveIcon></SaveIcon> </IconButton>
    )
  },
  
];



export  function ClientesTable() {
   /**
   * Initializes a state variable called `visitas` using the `useState` hook.
   * Defines an asynchronous function called `fecthVisita` that fetches data from an API using an instance of the `VisitasDAO` class.
   * The fetched data is then set to the `visitas` state variable using the `setVisitas` function.
   * The `fecthVisita` function is called once when the component mounts using the `useEffect` hook.
   */
  const[clientes,setClientes]=useState<ClientesEntity[]|any> ([])

    /**
   * Fetches data from an API using an instance of the @class`VisitasDAO`  
   * and sets the fetched data to the `visitas` state variable.
   * 
   * @returns {Promise<void>} 
   * - A promise that resolves once the data is fetched and set to the state variable.
   */
  async function fecthClientes(): Promise<void> {
    try {
        const ControladorClientes = new ClientesDAO();
        const data = await ControladorClientes.getAllClientes();
        setClientes(data);
      } catch (error) {
        console.error(error);
      }
}
useEffect(() => {
  fecthClientes();
}, []);

const rows = clientes


  return (
    <Box sx={{ height: "100vh", width: '100%' }}>
      <DataGrid

  slots={{
    toolbar: CustomToolbar,
  }} editMode='cell'
rows={rows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 30,
            },
          },
        }}
        pageSizeOptions={[7]}
       
        disableRowSelectionOnClick
      />
    </Box>
  );
}
