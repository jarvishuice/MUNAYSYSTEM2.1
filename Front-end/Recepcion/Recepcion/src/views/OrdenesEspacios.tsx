import { useState } from "react";
import { DetalleDeudaCliente, DeudaClientesEntity } from "../core/Entities/clients/dedudaClientes";
import { ModalFormPago } from "../controller/Components/ModalFormPago";

import { CarritoOrdenes } from "../controller/Components/CarritoOrdenes";
import { OrdenesEspacios } from "../controller/Components/ORDENESESPACIOS";

export function ORDENES() {
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
          <OrdenesEspacios selectorDeudor={SelectDeudor} detallesDeudor={setDetalles}/>
          <div className="mt-4 col-sm-2 col-md-4 col-lg-4 order-md-reverse">
            <CarritoOrdenes activarModal={() => setIsModalOpen(true)} deudor={deudor} detalles={detalles} />
          </div>
        </div>
      </main>
    </>
  );
}
