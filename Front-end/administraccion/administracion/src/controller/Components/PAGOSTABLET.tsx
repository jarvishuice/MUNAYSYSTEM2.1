
import { GridColDef, DataGrid, GridToolbarContainer, GridToolbarExport } from "@mui/x-data-grid";
import { useState,useEffect } from "react";

import { PagosDetailEntity } from "../../core/Entities/pagos/pagosEntity";
import { PagosDAO } from "../../core/Implements/pagos/pagosDAO";
import { ModalEditPay } from "./modalEditPay";
import { Box } from "@mui/joy";
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
        <ModalEditPay x={params}></ModalEditPay>
      )
    },
    
  ];
export function TABLEPAY(){
    const[pays,setPays]=useState<PagosDetailEntity[]|any> ([])
    async function fecthClientes(): Promise<void> {
        try {
            const ControladorPays = new PagosDAO();
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