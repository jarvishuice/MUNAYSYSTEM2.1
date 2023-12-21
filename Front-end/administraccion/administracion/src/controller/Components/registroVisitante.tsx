import Box from '@mui/joy/Box';

import Card from '@mui/joy/Card';
import CardActions from '@mui/joy/CardActions';
import CardContent from '@mui/joy/CardContent';

import Divider from '@mui/joy/Divider';
import FormControl from '@mui/joy/FormControl';
import FormLabel from '@mui/joy/FormLabel';
import Input from '@mui/joy/Input';
import Typography from '@mui/joy/Typography';
import Button from '@mui/joy/Button';
import InfoOutlined from '@mui/icons-material/InfoOutlined';
import EmailIcon from '@mui/icons-material/Email';
import PhoneIcon from '@mui/icons-material/Phone';
import BadgeIcon from '@mui/icons-material/Badge';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import { useState } from 'react';
import { ClientesEntity } from '../../core/Entities/clients/clients';

import { VisitantesDAO } from '../../core/Implements/visitantes/visitantesDAO';
async function RegisterCliente (cliente:ClientesEntity){
  try {
    const contorladorVisitantes = new VisitantesDAO();
    const data = await contorladorVisitantes.crearVisitante(cliente);
    if (data != null ){
       alert(`Visitante registrado de manera correcta`);
      window.location.reload();
    }
    
  } catch (error) {
    console.error(error);
  }



}
//import CreditCardIcon from '@mui/icons-material/CreditCard';
export function FormRegVisitante(){
  /*
  * param
 */ 
const [nombre,setNombre]=useState<string>('')
const handleChangeNombre = (e: React.ChangeEvent<HTMLInputElement>) => {
  setNombre(e.target.value);
};
const [correo,setCorreo]=useState<string>('')
const handleChangeCorreo = (e: React.ChangeEvent<HTMLInputElement>) => {
  setCorreo(e.target.value);
};

const [telefono,setTelefono]=useState<string>('')
const handleChangeTelefono = (e: React.ChangeEvent<HTMLInputElement>) => {
  setTelefono(e.target.value);
};
const [ci,setCi]=useState<string>('')
const handleChangeCi = (e: React.ChangeEvent<HTMLInputElement>) => {
  setCi(e.target.value);
};
 const [direccion,setDireccion]= useState<string>('')
 const handleChangeDireccion = (e: React.ChangeEvent<HTMLInputElement>) => {
  setDireccion(e.target.value);
};

return (  <Box
    sx={{
      py: 2,
      display: 'grid',
      gap: 2,
      alignItems: 'center',
      flexWrap: 'wrap',
    }}
  >
<Card
      variant="outlined"
      sx={{
        maxHeight: 'max-content',
        maxWidth: '100%',
        mx: 'auto',
        // to make the demo resizable
        overflow: 'auto',
        resize: 'horizontal',
      }}
    >
      <Typography level="title-lg" startDecorator={<InfoOutlined />}>
Registro de Visitantes
      </Typography>
      <Divider inset="none" />
      <CardContent
        sx={{
          display: 'grid',
          gridTemplateColumns: 'repeat(2, minmax(80px, 1fr))',
          gap: 1.5,
        }}
      >
        <FormControl sx={{ gridColumn: '1/-1' }}>
          <FormLabel>Nombre</FormLabel>
          <Input  onChange={handleChangeNombre} value={nombre} endDecorator={<AccountCircleIcon/>}/>
        </FormControl>
        <FormControl>
          <FormLabel>Correo</FormLabel>
          <Input  onChange={handleChangeCorreo} value={correo} type="email"  endDecorator={<EmailIcon></EmailIcon>} />
        </FormControl>
        <FormControl>
          <FormLabel>TELEFONO</FormLabel>
          <Input onChange={handleChangeTelefono} value={telefono} endDecorator={<PhoneIcon />} />
        </FormControl>
        <FormControl sx={{ gridColumn: '1/-1' }}>
          <FormLabel>CEDULA/RIF</FormLabel>
          <Input onChange={handleChangeCi}  value={ci} endDecorator={<BadgeIcon/>}placeholder="222.." />
        </FormControl>
        <FormControl sx={{ gridColumn: '1/-1' }}>
          <FormLabel>DIRECCION</FormLabel>
          <Input onChange={handleChangeDireccion} value={direccion} placeholder="Av ....." endDecorator={<LocationOnIcon/>} />
        </FormControl>
        
        <CardActions sx={{ gridColumn: '1/-1' }}>
          <Button variant="solid" color="primary" onClick={()=>RegisterCliente({
            id:Number(1),
            nombre:nombre,
            apellido:" ",
            correo:correo,
            tlf:telefono,
            fechaingreso:" ",
            fechacambio:" ",
            codigo:Number(0),
            credito: Number(0),
            ci:ci,
            identificacion:" ",
            direccion:direccion,
            deuda:Number(0)




          })}> 
Registrar Visitante
          </Button>
        </CardActions>
      </CardContent>
    </Card>



  </Box>)



}

