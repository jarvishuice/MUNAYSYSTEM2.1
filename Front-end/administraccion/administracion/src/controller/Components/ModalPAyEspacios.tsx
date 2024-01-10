import * as React from 'react';
import Button from '@mui/joy/Button';
import Modal from '@mui/joy/Modal';
import ModalClose from '@mui/joy/ModalClose';

import Sheet from '@mui/joy/Sheet';
import WorkHistoryIcon from '@mui/icons-material/WorkHistory';
import { DetallesDeudasEspacios } from './DetalleDeudasEspacios';
import { Grid } from '@mui/joy';
import { PagosEspacios } from './pagosEspacios';
/**
 * `ModalPayEspacios` es un componente React que muestra un modal con detalles de pago.
 *
 * @param {any} props - Las propiedades pasadas a este componente. Espera un objeto `deudaCliente`.
 *
 * @returns {JSX.Element} Un fragmento de React que contiene un botón y un modal.
 * Al hacer clic en el botón, se abre el modal que muestra los detalles de pago y deudas.
 *
 * El modal contiene dos componentes principales:
 * 1. `PagosEspacios`: Muestra el formulario para que el cliente pueda pagar. Recibe `props.deudaCliente` como prop.
 * 2. `DetallesDeudasEspacios`: Muestra los detalles de las deudas del cliente. Recibe `props.deudaCliente` como prop.
 *
 * El modal se puede cerrar haciendo clic fuera de él o en el botón de cierre en la esquina superior derecha.
 */
export function ModalPayEspacios(props: any): JSX.Element {
  const [open, setOpen] = React.useState<boolean>(false);

  return (
    <React.Fragment>
      <Button color="primary" startDecorator={<WorkHistoryIcon />} size="sm" onClick={() => setOpen(true)}>
        DETALLES
      </Button>
      <Modal
        aria-labelledby="modal-title"
        aria-describedby="modal-desc"
        open={open}
        onClose={() => setOpen(false)}
        sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', }}
      >
        <Sheet
          variant="outlined"
          sx={{
            width: "60%",
            borderRadius: 'md',
            p: 4,
            boxShadow: 'lg',
            marginTop: 12,

          }}
        >


          <ModalClose variant="plain" sx={{ m: 1 }} />
          <Grid style={{ maxHeight: '550px', overflow: 'auto' }} container spacing={2} sx={{ flexGrow: 2 }}>
            <Grid xs={6}><PagosEspacios cliente={props.deudaCliente} />

            </Grid>
            <Grid xs={5}><DetallesDeudasEspacios deudor={props.deudaCliente}>
            </DetallesDeudasEspacios>

            </Grid>
          </Grid>
        </Sheet>
      </Modal>
    </React.Fragment>
  );
}