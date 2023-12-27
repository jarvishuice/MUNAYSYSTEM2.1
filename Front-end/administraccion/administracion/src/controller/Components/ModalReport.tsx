import * as React from 'react';
import Button from '@mui/joy/Button';
import Modal from '@mui/joy/Modal';
import ModalClose from '@mui/joy/ModalClose';
import AssessmentIcon from '@mui/icons-material/Assessment';
import Sheet from '@mui/joy/Sheet';
import { IconButton } from '@mui/joy';


export default function BasicModal() {
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
         <Button href=''> Reprote Preciere</Button>

        </Sheet>
      </Modal>
    </React.Fragment>
  );
}