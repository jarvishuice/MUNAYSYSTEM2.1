import { Tabs, TabList, Tab, TabPanel } from "@mui/joy";
import { POSESPACIOS } from "./POS_ESPACIOS";

export function ESPACIOS(){
return(<Tabs aria-label="Basic tabs" defaultValue={0}>
<TabList>
  <Tab>POS</Tab>
  <Tab>ORDENES</Tab>
  <Tab>Registrar Visitante</Tab>
  <Tab>Visitantes</Tab>
</TabList>
<TabPanel value={0}>
<POSESPACIOS></POSESPACIOS>
</TabPanel>
<TabPanel value={1}>
<h1></h1>
</TabPanel>
<TabPanel value={2}>
 <h1></h1>
</TabPanel>
<TabPanel value={3}> 
 <h1>d</h1>
</TabPanel>
</Tabs>)


}