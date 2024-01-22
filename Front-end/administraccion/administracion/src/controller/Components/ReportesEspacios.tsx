
import { Card, Button, Divider,FormControl, FormLabel } from '@mui/joy';
import { PATHMUNAYSYSY } from '../../Config/routes/pathsMuanaysys';
import { useState } from 'react';

export function PDFViewer() {
const sede= localStorage.getItem("sede")??"inicia seccion ";
   const paths =  new PATHMUNAYSYSY()
   const API=  paths.PathAPI()
   const prefijo=`Espacios/Report/${sede}`
    console.log(`${API}${prefijo}`)
    const [mes,setMes]= useState<number>(1);
    const [year,setYear]= useState<number>(2024)
    return (<>
    <center>
        <Card sx={{ width: 320 }}>
                    <Button onClick={ ()=> window.location.href=`${API}${prefijo}`}>
        REPORTE DEL DIA 
                    </Button>
        <Divider></Divider>
        <FormControl>
      <FormLabel><h2>Reportes Mensuales</h2></FormLabel>
      <Divider></Divider>
      <FormLabel>Mes</FormLabel>
     <select value= {mes} onChange={(e)=>setMes(Number(e.target.value))}>
    
  <option value="1">Enero</option>
  <option value="2">Febrero</option>
  <option value="3">Marzo</option>
  <option value="4">Abril</option>
  <option value="5">Mayo</option>
  <option value="6">Junio</option>
  <option value="7">Julio</option>
  <option value="8">Agosto</option>
  <option value="9">Septiembre</option>
  <option value="10">Octubre</option>
  <option value="11">Noviembre</option>
  <option value="12">Diciembre</option>
</select>


     <FormLabel>Year</FormLabel>
     <input value={year} onChange={(e)=> setYear(Number(e.target.value))} type="number" min={2023} step={"1"} />



    </FormControl>
        <Button onClick={()=>window.location.href =`${API}Espacios/Report/Mensual/${sede}/${mes}/${year}`}> Generar reporte del {mes}-{year} </Button>
      </Card></center>
      </>
    );
}

