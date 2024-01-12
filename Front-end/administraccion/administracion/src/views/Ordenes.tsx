import {  useState } from "react";
import { DetalleDeudaCliente, DeudaClientesEntity } from "../core/Entities/clients/dedudaClientes";
import { ModalFormPago } from "../controller/Components/ModalFormPago";
import Tabs from '@mui/joy/Tabs';
import TabList from '@mui/joy/TabList';
import Tab from '@mui/joy/Tab';
import TabPanel from '@mui/joy/TabPanel';
import { Ordenes } from "../controller/Components/ORDENES";
import { CarritoOrdenes } from "../controller/Components/CarritoOrdenes";
import { OrdenesTable } from "../controller/Components/TableOrdenes";

export function OrdenesCompleto(){
  return (
    <Tabs sx={{}} aria-label="Basic tabs" defaultValue={0}>
<TabList>
  <Tab>Deudas Coffeshop</Tab>
  <Tab>Ordenes</Tab>
  <Tab>Pagos</Tab>
 
</TabList>
<TabPanel value={0}>

 <ORDENES></ORDENES>
</TabPanel>
<TabPanel value={1}>
<OrdenesTable/>
</TabPanel>
</Tabs>
  )
}



export  function ORDENES() {
  //const sede = localStorage.getItem('sede') ?? 'por favor inicie sesión para poder crear una orden';
/**
   * Detalles de las órdenes
   */
const [detalles, setDetalles] = useState<DetalleDeudaCliente[]>([]);

/*const RegistroDetalles =  (detalle:DetalleDeudaCliente[]) => {
    setDetalles(detalle);
 
};*/




//==================================================================
  // Estado selector del deudor
  const [deudor, setDeudor] = useState<DeudaClientesEntity>({ idCliente: 8, ci: "0000000", nombre: "seleccione un cliente", cantidadOrdenes: 0, deuda: 0 });

  const SelectDeudor = (DEUDOR: DeudaClientesEntity) => {
 
    setDeudor(DEUDOR);

    
  }

  // Estado para mostrar el Modal
  const [isModalOpen, setIsModalOpen] = useState(false);

  

  return (
    <>
      <main className="main ">
        <div className="row g-5">
          <ModalFormPago isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} cliente={deudor} />
          <center>
            {/* <div className="col-md-7 col-lg-8  ">
              <div className=" ">
                <BusquedaOrdenes   ></BusquedaOrdenes></div>


              <BotoneraCategoria  ></BotoneraCategoria></div>
            */}
          </center>
          <Ordenes selectorDeudor={SelectDeudor} detallesDeudor={setDetalles}/>
          <div className="mt-4 col-sm-2 col-md-4 col-lg-4 order-md-reverse">
            <CarritoOrdenes activarModal={() => setIsModalOpen(true)} deudor={deudor} detalles={detalles} />
          </div>
        </div>
      </main>
    </>
  );
}
