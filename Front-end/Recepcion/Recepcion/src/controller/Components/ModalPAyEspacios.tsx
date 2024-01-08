import * as React from 'react';
import Button from '@mui/joy/Button';
import Modal from '@mui/joy/Modal';
import ModalClose from '@mui/joy/ModalClose';

import Sheet from '@mui/joy/Sheet';
import WorkHistoryIcon from '@mui/icons-material/WorkHistory';
import { DetallesDeudasEspacios } from './DetalleDeudasEspacios';
export  function ModalPayEspacios(props:any) {
  const [open, setOpen] = React.useState<boolean>(false);
  return (
    <React.Fragment>
      <Button color="primary" startDecorator={<WorkHistoryIcon/>}  size="sm"onClick={() => setOpen(true)}>
       DETALLES
      </Button>
      <Modal
        aria-labelledby="modal-title"
        aria-describedby="modal-desc"
        open={open}
        onClose={() => setOpen(false)}
        sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}
      >
        <Sheet
          variant="outlined"
          sx={{
            maxWidth: 500,
            borderRadius: 'md',
            p: 3,
            boxShadow: 'lg',
          }}
        >
            
            
          <ModalClose variant="plain" sx={{ m: 1 }} />

          <DetallesDeudasEspacios deudor={props.deudaCliente}></DetallesDeudasEspacios>
        </Sheet>
      </Modal>
    </React.Fragment>
  );
}