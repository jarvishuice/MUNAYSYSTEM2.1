
import Tabs from '@mui/joy/Tabs';
import TabList from '@mui/joy/TabList';
import Tab from '@mui/joy/Tab';
import TabPanel from '@mui/joy/TabPanel';
import { FormRegClient } from '../controller/Components/formRegistroCliente';
import { ClientesTable } from '../controller/Components/tableClientes';

export  function ClientesMaster() {
  return (
    <Tabs aria-label="Basic tabs" defaultValue={0}>
      <TabList>
        <Tab>Clientes</Tab>
        <Tab>Registrar Cliente</Tab>
       
      </TabList>
      <TabPanel value={0}>

       <ClientesTable></ClientesTable>
      </TabPanel>
      <TabPanel value={1}>
      <FormRegClient></FormRegClient>
      </TabPanel>
    
    </Tabs>
  );
}