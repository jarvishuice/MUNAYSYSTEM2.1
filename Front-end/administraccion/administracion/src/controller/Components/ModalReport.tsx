import * as React from 'react';
import Button from '@mui/joy/Button';
import Modal from '@mui/joy/Modal';
import ModalClose from '@mui/joy/ModalClose';
import AssessmentIcon from '@mui/icons-material/Assessment';
import Sheet from '@mui/joy/Sheet';
import { IconButton } from '@mui/joy';
import { PATHMUNAYSYSY } from '../../Config/routes/pathsMuanaysys';
const sede= localStorage.getItem('sede')??"InicieSeccion";
const paths =  new PATHMUNAYSYSY()
const API=  paths.PathAPI()
const prefijo='Reports'

const PreCierre=`${API}${prefijo}/coffeshop/precierre/${sede}`
const Cierre=`${API}${prefijo}/coffeshop/cierre/${sede}`

export  function ModalReports() {
  const [open, setOpen] = React.useState<boolean>(false);
  return (
    <React.Fragment>
      <IconButton variant="outlined" color="neutral" onClick={() => setOpen(true)}>
        <AssessmentIcon> Report</AssessmentIcon>
      </IconButton>
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
          <br />
         <Button onClick={()=>window.location.href=`${PreCierre}`}> Reporte Preciere</Button>
         <Button onClick={()=>window.location.href=`${Cierre}`}> Cierre de Jornada</Button>

        </Sheet>
      </Modal>
    </React.Fragment>
  );
}