//import { PropaneSharp } from "@mui/icons-material";
import { IconButton, Drawer, Box, Typography, ModalClose, List, ListItemButton, Avatar, Divider} from "@mui/joy";
import React from "react";
//import { Inicio } from "../../views/INICIO";
//import { POS } from "../../views/POS";
import Menu from '@mui/icons-material/Menu';
import LogoutIcon from '@mui/icons-material/Logout';
import HomeIcon from '@mui/icons-material/Home';
import LocalGroceryStoreIcon from '@mui/icons-material/LocalGroceryStore';
import ReceiptIcon from '@mui/icons-material/Receipt';
import '../../App.css';

import { Inicio } from "../../views/INICIO";
import { POS } from "../../views/POS";
import {  OrdenesCompleto } from "../../views/Ordenes";
import GroupIcon from '@mui/icons-material/Group';
import HowToRegIcon from '@mui/icons-material/HowToReg';
import { Visitantes } from "../../views/Visitantes";
import { ClientesMaster } from "../../views/ClientesMAster";
import AddLocationAltIcon from '@mui/icons-material/AddLocationAlt';
import { ModalReports } from "./ModalReport";
import { ESPACIOS } from "../../views/ESPACIOS";
import AddHomeWorkIcon from '@mui/icons-material/AddHomeWork';


export function Navegacion(props:any){
  const logoNest='https://www.nestvzla.com/Nest/Static/Home_files/logonest.png';
  const [open, setOpen] = React.useState(false);
  const foto:string=localStorage.getItem('fotoPerfil')??'https://img.freepik.com/premium-vector/account-icon-user-icon-vector-graphics_292645-552.jpg?size=338&ext=jpg&ga=GA1.1.1546980028.1703116800&semt=ais';
  const usuario:string =localStorage.getItem("usuario")??'Inicie seccion';
  const sede:string=localStorage.getItem("sede")??'Inicie seccion';
  return (
    <div style={{backgroundColor:"#1f2937"}}>
 <React.Fragment>
 
  <IconButton variant="outlined" style={{height:"4rem"}}  onClick={() => setOpen(true)}>
    <Menu />
    
  </IconButton>
  
  <img className="SIDEBARLOGO"  style={{'width':'5rem'}}  src={logoNest}/>
  <div className="nest"><AddLocationAltIcon/>  {sede} </div>
  <Drawer  size='sm'    open={open} onClose={() => setOpen(false)}>
    <Box
      sx={{
        display: 'flex',
        alignItems: 'center',
        gap: 0.5,
        ml: 'auto',
        mt: 1,
        mr: 2,
      
       
      }}
    >
      <Typography
        component="label"
        htmlFor="close-icon"
        fontSize="sm"
        fontWeight="lg"
        sx={{ cursor: 'pointer' }}
      >
        Close
      </Typography>
      <ModalClose id="close-icon" sx={{ position: 'initial' }} />
    </Box>
 
    
    <List
      size="lg"
      component="nav"
      sx={{
        flex: 'none',
        fontSize: 'xl',
        '& > div': { justifyContent: 'center' },
      }}
    >
      <center><Avatar alt="Foto perfil"  sx={{'--Avatar-size':'8rem'}}   src={foto} />
      <Typography fontSize="lg" fontWeight='lg' >{usuario}</Typography></center>
      <Divider sx={{color:"primary",height:'1px'}}/>
      <ListItemButton onClick={()=> props.setComponente(<Inicio/>)} > { <HomeIcon/>} Inicio</ListItemButton>
      <ListItemButton onClick={()=> props.setComponente(<POS/>)} >{<LocalGroceryStoreIcon/>}POS</ListItemButton>
      <ListItemButton onClick={()=> props.setComponente(<OrdenesCompleto/>)} >{<ReceiptIcon/>}Ordenes</ListItemButton>
      <ListItemButton onClick={()=> props.setComponente(<ClientesMaster/>)} >{<GroupIcon/>}Clientes</ListItemButton>
      <ListItemButton onClick={()=> props.setComponente(<Visitantes/>)} >{<HowToRegIcon/>}Visitantes</ListItemButton>
      <ListItemButton onClick={()=> props.setComponente(<ESPACIOS></ESPACIOS>)}>{<AddHomeWorkIcon></AddHomeWorkIcon>} Espacios </ListItemButton>
      <ListItemButton > <ModalReports></ModalReports>     </ListItemButton>
      <ListItemButton>{<LogoutIcon/>}Salir</ListItemButton>
    </List>
  </Drawer>
</React.Fragment>
</div>
)



}