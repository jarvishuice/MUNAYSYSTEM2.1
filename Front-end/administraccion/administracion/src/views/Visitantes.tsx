
import Tabs from '@mui/joy/Tabs';
import TabList from '@mui/joy/TabList';
import Tab from '@mui/joy/Tab';
import TabPanel from '@mui/joy/TabPanel';
import { FormRegVisitante } from '../controller/Components/registroVisitante';
import { RegistroVISITA } from '../controller/Components/registroVisita';
import { VisitasTable } from '../controller/Components/VisitasTable';
import { VisitantesTable } from '../controller/Components/tableVisitantes';

export  function Visitantes() {
  return (
    <Tabs aria-label="Basic tabs" defaultValue={0}>
      <TabList>
        <Tab>Visitas</Tab>
        <Tab>Registrar Visita</Tab>
        <Tab>Registrar Visitante</Tab>
        <Tab>Visitantes</Tab>
      </TabList>
      <TabPanel value={0}>
       <VisitasTable/>
      </TabPanel>
      <TabPanel value={1}>
    <RegistroVISITA/>
      </TabPanel>
      <TabPanel value={2}>
       <FormRegVisitante></FormRegVisitante>
      </TabPanel>
      <TabPanel value={3}> 
        <VisitantesTable></VisitantesTable>
      </TabPanel>
    </Tabs>
  );
}