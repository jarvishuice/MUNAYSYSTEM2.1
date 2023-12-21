import Box from '@mui/joy/Box';
import { CardIndicador } from './cardIndicador';
import { useEffect, useState } from 'react';
import { MetricCoffeshopEntity } from '../../core/Entities/metric/coffeshop/MetricCoffeshopEntity';
import { MetricCoffeshopDAO } from '../../core/Implements/metric/coffeshop/MetricCoffeshopDAO';
import '../../App.css'
import { TableOrder } from './tableOrder';
export function DashBoard(){
  const [metric,setMetric]=useState<MetricCoffeshopEntity|null>()
  const sede= localStorage.getItem('sede')??"j"
  useEffect(()=>{
    async function fechtMetric(sede:string) 
    {
     try{
      const controladorMetric = new MetricCoffeshopDAO()
      const data = await controladorMetric.ExtraerMetricasBySede(sede);
      setMetric(data);
     } 
     catch(error){
      console.error(error);
     }
    };
    fechtMetric(sede)},[sede])




  
    return (   <> <div className='offset-md-2   mt-2'>
      <Box className="mt-2"
        sx={{
          width: '100%',
          maxWidth: '100%',
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))',
          gap: 3,
        }}
      >
    <CardIndicador indicadorName="Ventas dia" meta={200} valor={metric?.ventasDiarias} />
    <CardIndicador indicadorName="Deuda" meta={metric?.deudas} valor={metric?.deudas}/>
    <CardIndicador indicadorName="Ventas  mes" meta={2800} valor={metric?.ventasMensual}/>



        </Box> 
        
  
        
        </div> <div className='  mt-2 w-80'>
           
       <TableOrder></TableOrder></div> </>)
}
