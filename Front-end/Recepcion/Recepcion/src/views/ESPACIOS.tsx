import { Tabs, TabList, Tab, TabPanel } from "@mui/joy";
import { POSESPACIOS } from "./POS_ESPACIOS";
import { OrdenesEspacios } from "../controller/Components/ORDENESESPACIOS";

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
<OrdenesEspacios></OrdenesEspacios>
</TabPanel>

</Tabs>)


}