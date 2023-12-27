import * as React from 'react';
import Box from '@mui/joy/Box';
import Button from '@mui/joy/Button';
import Card from '@mui/joy/Card';
import CardActions from '@mui/joy/CardActions';
import Chip from '@mui/joy/Chip';
import Divider from '@mui/joy/Divider';
import List from '@mui/joy/List';
import ListItem from '@mui/joy/ListItem';
import Typography from '@mui/joy/Typography';
import KeyboardArrowRight from '@mui/icons-material/KeyboardArrowRight';
import { Input } from '@mui/joy';
import { useState } from 'react';
import { PATHMUNAYSYSY } from '../../Config/routes/pathsMuanaysys';
const sede= localStorage.getItem('sede')??"InicieSeccion";
const paths =  new PATHMUNAYSYSY()
const API=  paths.PathAPI()
const prefijo='Reports'

export  function CardReportByfecha() {
    const [ano, setAno] = useState('');

  const handleAno= (event: React.ChangeEvent<HTMLInputElement>) => {
    setAno(event.target.value);
  };
  const [mes, setMes] = useState('');

  const handleMes= (event: React.ChangeEvent<HTMLInputElement>) => {
    setMes(event.target.value);
  };
  const [dia, setDia] = useState('');

  const handleDia= (event: React.ChangeEvent<HTMLInputElement>) => {
    setDia(event.target.value);
  };

  function buildReport(year:string,month:string,day:string){
   try{
     const YEAR = parseInt(year);
     const MONTH = parseInt(month);
     const DAY= parseInt(day);
     window.location.href=`${API}${prefijo}/coffeshop/cierreByFecha/${sede}?ano=${YEAR}&mes=${MONTH}&day=${DAY}`
     
   }
   catch(error){

    alert("HA introduccido algun dato errado ");
   }


  }

  return (
    <Box
      sx={{
        width: '100%',
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(min(100%, 300px), 1fr))',
        gap: 2,
        
      }}
    >
      <Card size="lg"  variant="outlined">
        <Chip size="sm" variant="outlined" color="neutral">
          BASIC
        </Chip>
        <Typography level="h3">Reporte de cierre de jornada Historicos</Typography>
        <Divider inset="none" />
        <List size="sm" sx={{ mx: 'calc(-1 * var(--ListItem-paddingX))' }}>
          <ListItem>
          <Input  type ="number" onChange={handleAno} slotProps={{
          input: {
          
            min: 2023,
           
            step:1,
          },
        }} value={ano} placeholder="ANO" variant="outlined" color="primary"  />
          </ListItem>
          <ListItem>
            <Input   type ="number" onChange={handleMes} value={mes}placeholder="MES" variant="outlined" color="primary"  slotProps={{
          input: {
          
            min: 1,
           max:12,
            step:1,
          },
        }} />
          </ListItem>
          <ListItem>
          <Input onChange={handleDia}  value={dia} placeholder="DIA" variant="outlined" type='number'  color="primary" slotProps={{
          input: {
          
            min: 1,
            max:31,
            step:1,
          },
        }}  />
           
          </ListItem>
          
        </List>
        <Divider inset="none" />
        <CardActions>
          <Typography level="title-lg" sx={{ mr: 'auto' }}>
         {`${dia}-${mes}-${ano}`}
           
          </Typography>
          <Button
            variant="soft"
            color="neutral"
            endDecorator={<KeyboardArrowRight />}
            onClick={()=>buildReport(ano,mes,dia)}
          >
            Generar reporte
          </Button>
        </CardActions>
      </Card>
      
    </Box>
  );
}