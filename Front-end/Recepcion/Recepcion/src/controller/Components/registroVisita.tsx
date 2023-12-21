import BusquedaVisitante from "./busquedaVisitante";

import Button from '@mui/joy/Button';
import Card from '@mui/joy/Card';
import CardContent from '@mui/joy/CardContent';
import CardActions from '@mui/joy/CardActions';
import Divider from '@mui/joy/Divider';
import Typography from '@mui/joy/Typography';
import { ClientesEntity } from "../../core/Entities/clients/clients";
import { useState } from "react";
import BusquedaClientesVisitas from "./BusquedaCleintesVisitas";
import { VisitasEntity } from "../../core/Entities/visistas/visitasEntity";
import { VisitasDAO } from "../../core/Implements/visitas/visitasDAO";


export function RegistroVISITA() {
    async function RegisterVisitas (visita:VisitasEntity){
        try {
          const contorladorVisitas = new VisitasDAO();
          const data = await contorladorVisitas.crearVisita(visita);
          if (data != null ){
             alert(`Visita generada  de manera correcta`);
            window.location.reload();
          }
          
        } catch (error) {
          console.error(error);
        }
      
      
      
      }
  /**
   * Renders a form for registering a visitor.
   *
   * @returns The JSX element representing the visitor registration form.
   */
  const [visitante, setVisitante] = useState<ClientesEntity | undefined>(undefined);

  /**
   * Sets the selected visitor in the component's state and displays an alert with the visitor's name.
   *
   * @param persona - The selected visitor.
   */
  const insertarVisitante = (persona: ClientesEntity) => {
    setVisitante(persona);
    alert("Ha seleccionado al visitante: " + persona.nombre);
  };



  const [motivo,setMotivo]=useState<string>('visita')
  /** 
   * Updates the selected reason for the visit in the component's state.
   *
   * @param evento - The change event from the dropdown.
   */
  const seleccionMotivo=(evento:React.ChangeEvent<HTMLSelectElement>)=>{
 setMotivo(evento.target.value);
 
  }

const [cliente,setCliente]=useState<ClientesEntity|undefined>({
    "id": 8,
    "nombre": "CLIENTE CONTADO",
    "apellido": "None",
    "correo": "clientecontado@gmail.com",
    "tlf": "None",
    "fechaingreso": "2022-10-25 14:39:01",
    "fechacambio": null,
    "codigo": null,
    "credito": null,
    "ci": "10000002",
    "identificacion": "None",
    "direccion": "Caracas null",
    "deuda": null
  })




const insertCliente=(client:ClientesEntity)=>{
    setCliente(client);
    
}



  return (
    <div className="container">
      <div className="row">
        <div className="col">
          <h6> Visitante:</h6>
          <div className="d-flex">
            <BusquedaVisitante setVisitante={insertarVisitante}></BusquedaVisitante>
          </div>
        </div>
        <div className="col">
        <h6> Cliente:</h6>
          <div className="d-flex">
           <BusquedaClientesVisitas insertarPersona={insertCliente}></BusquedaClientesVisitas>
          </div>
        </div>
        <div className="col"> 
        <h6> Motivo:</h6>
          <div className="d-flex">
            <select className="form-select me-2" value={motivo} onChange={seleccionMotivo} aria-label="Motivo">
           
              <option value="visita">Visita</option>
              <option value="recorrido">Recorrido</option>
            </select>
         
          </div>
        </div>
      </div>
      <center>
        <Card
          variant="solid"
          color="primary"
          invertedColors
          sx={{
            boxShadow: 'lg',
            width: 400,
            maxWidth: '100%',
            // to make the demo resizeable
            overflow: 'auto',
            resize: 'horizontal',
          }}
        >
          <CardContent>
            <Typography level="title-lg">Visitante: {visitante === undefined ? '\n' : visitante.nombre}</Typography>
            <Typography level="title-lg">CI: {visitante === undefined ? '\n' : visitante.ci}</Typography>
            <Typography level="title-lg">tlf: {visitante === undefined ? '\n' : visitante.tlf}</Typography>
            <Divider orientation="horizontal" />
            <Typography level="title-lg">Motivo: {motivo}</Typography>
            <Divider orientation="horizontal"></Divider>
            <Typography level="title-lg"> Receptor: {cliente === undefined ? '\n' : cliente.nombre}</Typography>
          </CardContent>
          <CardActions>
            <Button variant="solid"  onClick={()=>RegisterVisitas({"id":" o","idVisitante":visitante!=undefined?visitante.id:0,"idCliente":cliente!= undefined?`${cliente.id}`:'0',"fIngreso":" f","fSalida": " f","status":'activa',"sede":localStorage.getItem('sede')??"sede","motivo":motivo})}>Registrar visita</Button>
          </CardActions>
        </Card>
      </center>
    </div>
  );
}